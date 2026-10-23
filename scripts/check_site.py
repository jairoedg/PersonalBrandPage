#!/usr/bin/env python3
"""Check the static site in site/ before publishing.

Standard library only. Not published (lives outside site/).

Usage:
    python3 scripts/check_site.py              static checks
    python3 scripts/check_site.py --browser    static checks, then browser checks in local Chrome
    python3 scripts/check_site.py --browser --shots DIR
    python3 scripts/check_site.py --strict     deploy gate: placeholder markers are errors (D-017)

Exit code: 0 = no errors, 1 = errors found, 2 = could not run.
Warnings never fail the run. Local runs report placeholders as warnings; the deploy
workflow runs with --strict so no placeholder can be published.
"""

import argparse
import base64
import datetime
import json
import os
import re
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import threading
import time
import urllib.parse
import urllib.request
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
BLUEPRINT = ROOT / "docs" / "00-foundation" / "01-personal-brand-blueprint.md"

TITLE_SUFFIX = " — Jairo Enrique Diaz"
# The Primary nav shows Contact as the "Let’s talk" pill (D-027); the footer keeps "Contact".
NAV_LINKS = {"Primary": ["Projects", "How I Can Help", "Leadership", "Career Journey", "About", "Let’s talk"],
             "Footer": ["Projects", "How I Can Help", "Leadership", "Career Journey", "About", "Contact"]}
# First path segment -> Primary nav link that should carry aria-current="page".
SECTIONS = {"projects": "Projects", "how-i-can-help": "How I Can Help", "leadership": "Leadership",
            "career-journey": "Career Journey", "about": "About", "contact": "Let’s talk"}
STYLESHEETS = ["fonts.css", "tokens.css", "base.css"]
PROJECT_CARDS = 10
# D-021 contact values.
CONTACT_EMAIL = "mailto:jairodiaz@yahoo.com"
CONTACT_LINKEDIN = "https://www.linkedin.com/in/jairo-enrique-diaz"
CONTACT_PHONE = "tel:+573107901197"
CV_FILE = "CV_JairoDiaz%20-%20Project%20Manager.pdf"
# --strict (deploy): placeholder markers fail the run instead of warning (D-017).
STRICT = False
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
FOCUSABLE = {"a", "button", "input", "select", "textarea"}


# ---------- Minimal DOM ----------

class Node:
    def __init__(self, tag, attrs, parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def text(self):
        return "".join(c if isinstance(c, str) else c.text() for c in self.children)

    def iter(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.iter()

    def find_all(self, tag=None, cls=None, **attrs):
        for n in self.iter():
            if tag and n.tag != tag:
                continue
            if cls and cls not in n.attrs.get("class", "").split():
                continue
            if all(n.attrs.get(k.replace("_", "-")) == v for k, v in attrs.items()):
                yield n

    def find(self, *a, **k):
        return next(self.find_all(*a, **k), None)

    def ancestor(self, tag):
        p = self.parent
        while p is not None and p.tag != tag:
            p = p.parent
        return p


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#document", {})
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


class Page:
    def __init__(self, path):
        self.path = path
        self.rel = path.relative_to(SITE).as_posix()
        self.source = path.read_text(encoding="utf-8")
        builder = TreeBuilder()
        builder.feed(self.source)
        self.dom = builder.root
        self.ids = [n.attrs["id"] for n in self.dom.iter() if "id" in n.attrs]

    @property
    def section(self):
        first = self.rel.split("/")[0]
        return SECTIONS.get(first) if "/" in self.rel else None


# ---------- Report ----------

class Report:
    def __init__(self):
        self.errors, self.warnings, self.passed = [], [], 0

    def check(self, ok, where, message, warn=False):
        if ok:
            self.passed += 1
        else:
            (self.warnings if warn else self.errors).append(f"{where}: {message}")
        return ok


# ---------- Static checks ----------

def resolve(page, url):
    """Return (target path, fragment) for an internal URL. Percent-encoding (e.g. %20) is decoded."""
    path, _, frag = url.partition("#")
    if not path:
        return page.path, frag
    target = (page.path.parent / urllib.parse.unquote(path)).resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target, frag


def check_page(page, r, all_ids):
    w = page.rel
    d = page.dom
    html_el = d.find("html")
    r.check(html_el is not None and html_el.attrs.get("lang") == "en", w, 'missing <html lang="en">')
    r.check(any("charset" in m.attrs for m in d.find_all("meta")), w, "missing <meta charset>")
    r.check(d.find("meta", name="viewport") is not None, w, "missing viewport <meta>")

    title = d.find("title")
    t = norm(title.text()) if title else ""
    r.check(t.endswith(TITLE_SUFFIX) and len(t) > len(TITLE_SUFFIX), w,
            f'<title> should be "… — Jairo Enrique Diaz" (found "{t}")')

    # Headings: one h1, no skipped levels.
    heads = [n for n in d.iter() if re.fullmatch(r"h[1-6]", n.tag)]
    h1s = [h for h in heads if h.tag == "h1"]
    r.check(len(h1s) == 1, w, f"expected exactly one <h1>, found {len(h1s)}")
    prev = 0
    for h in heads:
        lvl = int(h.tag[1])
        r.check(lvl <= prev + 1, w, f"heading level skips from h{prev} to h{lvl} at \"{norm(h.text())[:40]}\"")
        prev = lvl

    # Skip link first, main#main present.
    focusables = [n for n in d.iter() if (n.tag in FOCUSABLE and (n.tag != "a" or "href" in n.attrs))
                  or (n.attrs.get("tabindex") not in (None, "-1"))]
    first = focusables[0] if focusables else None
    r.check(first is not None and "skip-link" in first.attrs.get("class", "") and first.attrs.get("href") == "#main",
            w, "first focusable element must be the skip link to #main")
    r.check(d.find("main", id="main") is not None, w, 'missing <main id="main">')

    # Navigation.
    expected_current = page.section
    for label in ("Primary", "Footer"):
        nav = d.find("nav", aria_label=label)
        if not r.check(nav is not None, w, f'missing <nav aria-label="{label}">'):
            continue
        links = list(nav.find_all("a"))
        r.check([norm(a.text()) for a in links] == NAV_LINKS[label], w,
                f"{label} nav links should be {', '.join(NAV_LINKS[label])}")
        current = [norm(a.text()) for a in links if a.attrs.get("aria-current") == "page"]
        if label == "Primary":
            want = [expected_current] if expected_current else []
            r.check(current == want, w, f'Primary nav aria-current should be on {want or "nothing"} (found {current or "nothing"})')
    site_name = d.find("a", cls="site-name")
    if page.rel == "index.html":
        r.check(site_name is not None and site_name.attrs.get("aria-current") == "page", w,
                'Home: the site name link should have aria-current="page"')

    # Stylesheets and third-party loads.
    sheets = [n.attrs.get("href", "") for n in d.find_all("link") if n.attrs.get("rel") == "stylesheet"]
    r.check([s.rsplit("/", 1)[-1] for s in sheets] == STYLESHEETS, w,
            f"stylesheets should load in the order {' → '.join(STYLESHEETS)}")
    for n in d.iter():
        for attr in ("src", "href"):
            v = n.attrs.get(attr, "")
            if n.tag != "a" and re.match(r"^(https?:)?//", v):
                r.check(False, w, f"third-party load <{n.tag} {attr}=\"{v}\">")

    # Ids.
    seen = set()
    for i in page.ids:
        r.check(i not in seen, w, f'duplicate id="{i}"')
        seen.add(i)

    # Links and references.
    missing = []
    for n in d.iter():
        attr = "href" if n.tag in ("a", "link") else "src" if n.tag in ("img", "script", "source") else None
        url = n.attrs.get(attr) if attr else None
        if url is None:
            continue
        if n.tag == "a":
            r.check(norm(n.text()) or n.attrs.get("aria-label"), w, f'link to "{url}" has no text')
        if re.match(r"^(mailto:|tel:|https?:|//)", url):
            continue
        if not r.check(not url.startswith("/"), w, f'root-relative URL "{url}" breaks under /<repo>/ on GitHub Pages'):
            continue
        target, frag = resolve(page, url)
        if not target.exists():
            missing.append(target)
            continue
        r.passed += 1
        if frag:
            key = target.relative_to(SITE).as_posix() if target.is_relative_to(SITE) else str(target)
            r.check(frag in all_ids.get(key, ()), w, f'link "{url}": no id="{frag}" on the target page')
    # Footer year (manual update each January).
    footer = d.find("footer")
    m = re.search(r"©\s*(\d{4})", footer.text()) if footer else None
    year = datetime.date.today().year
    r.check(m is not None and int(m.group(1)) == year, w,
            f"footer year is {m.group(1) if m else 'missing'}; update it by hand to {year}", warn=True)

    # Unapproved-content markers.
    text = norm(d.find("body").text()) if d.find("body") else ""
    markers = len(re.findall(r"\bPlaceholder\b|\bDraft:", text, re.I))
    r.check(markers == 0, w, f"{markers} placeholder/draft marker(s) on the page", warn=not STRICT)
    return missing


def check_decisions(pages, r):
    """Content decisions made by Jairo during the build (keep in sync with the decision record)."""
    home = pages.get("index.html")
    projects = pages.get("projects/index.html")
    if r.check(home is not None, "index.html", "Home page is missing"):
        body = norm(home.dom.find("body").text())
        r.check("approximately 60" in body and "about 60" not in body, "index.html",
                'DFA card should say "approximately 60", not "about 60"')
        lead = home.dom.find("p", cls="lead")
        if BLUEPRINT.exists():
            line = next((l.strip() for l in BLUEPRINT.read_text(encoding="utf-8").splitlines()
                         if l.startswith("Jairo positions himself")), None)
            r.check(line is not None and lead is not None and norm(lead.text()) == norm(line), "index.html",
                    "positioning must match the blueprint sentence word for word")
        else:
            r.check(False, "index.html", f"cannot verify positioning: {BLUEPRINT} not found", warn=True)
        previews = list(home.dom.find_all("article", cls="story-card"))
        r.check(len(previews) == 3, "index.html", f"expected 3 Home preview cards, found {len(previews)}")

    if not r.check(projects is not None, "projects/index.html", "Projects page is missing"):
        return
    cards = list(projects.dom.find_all("article", cls="story-card"))
    r.check(len(cards) == PROJECT_CARDS, "projects/index.html", f"expected {PROJECT_CARDS} cards, found {len(cards)}")
    detail = {p for p in pages if p.startswith("projects/") and p != "projects/index.html"}
    linked = set()
    for c in cards:
        a = c.find("a")
        name = norm(a.text()) if a else "(card without link)"
        where = f"projects/index.html card \"{name[:40]}\""
        r.check(a is not None and c.find("h2") is not None, where, "title must be an <h2> with a link")
        r.check(c.find("p", cls="story-card__meta") is not None, where, "missing context line")
        r.check(c.find("p", cls="story-card__role") is not None, where, "missing role")
        r.check(any(p.attrs.get("class") is None for p in c.find_all("p")), where, "missing summary")
        out = c.find("p", cls="story-card__outcome")
        r.check(out is not None and norm(out.text()).startswith("Outcome:"), where, 'missing "Outcome:" line')
        if a is not None:
            linked.add("projects/" + a.attrs.get("href", ""))
        if a is not None and "Tigo" in name:
            r.check(out is not None and "Tableau" in out.text(), where, "Tigo outcome should mention Tableau")
    r.check(linked == detail, "projects/index.html",
            f"cards and detail pages differ (no page: {sorted(linked - detail)}, no card: {sorted(detail - linked)})")

    for rel in sorted(detail):
        back = pages[rel].dom.find("p", cls="back-link")
        r.check(back is not None and back.find("a", href="./") is not None, rel, 'missing "Back to Projects" link at the top')

    avianca = pages.get("projects/avianca-data-warehouse.html")
    if r.check(avianca is not None, "projects/avianca-data-warehouse.html", "Avianca page is missing"):
        note = avianca.dom.find("aside", id="note")
        r.check(note is not None and norm(note.text()) == "Jairo left before the migration began.",
                avianca.rel, 'footnote should read "Jairo left before the migration began."')
        r.check(avianca.dom.find("a", href="#note") is not None, avianca.rel, 'missing "See note" link to #note')

    # D-021: approved contact values, in the A10 order Email → LinkedIn → Phone, then the CV.
    contact = pages.get("contact/index.html")
    if r.check(contact is not None, "contact/index.html", "Contact page is missing"):
        hrefs = [a.attrs.get("href", "") for a in contact.dom.find("main").find_all("a")]
        want = [CONTACT_EMAIL, CONTACT_LINKEDIN, CONTACT_PHONE]
        found = [h for h in hrefs if h in want]
        r.check(found == want, contact.rel, "contact links must be Email, LinkedIn, Phone (approved values, in that order)")
        cv = [a for a in contact.dom.find_all("a") if a.attrs.get("href", "").endswith(CV_FILE)]
        r.check(len(cv) == 1 and norm(cv[0].text()) == "Download CV (PDF)", contact.rel,
                f'expected one "Download CV (PDF)" link to …/{CV_FILE}')


def run_static(r):
    pages = {p.rel: p for p in (Page(f) for f in sorted(SITE.rglob("*.html")))}
    all_ids = {rel: set(p.ids) for rel, p in pages.items()}
    missing = {}
    for p in pages.values():
        for target in check_page(p, r, all_ids):
            missing.setdefault(target, set()).add(p.rel)
    for target, sources in sorted(missing.items()):
        shown = target.relative_to(SITE).as_posix() if target.is_relative_to(SITE) else str(target)
        r.check(False, shown, f"link target does not exist (linked from {len(sources)} page(s))")
    check_decisions(pages, r)
    return pages


# ---------- Browser checks (local Chrome over the DevTools protocol) ----------

WIDTHS = (320, 768, 1024)
KEYBOARD_WIDTH = 1024
ROW_TOLERANCE = 24  # px; links within this vertical distance count as one row (read left to right)
CHROME_CANDIDATES = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                     "/Applications/Chromium.app/Contents/MacOS/Chromium"]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class CDP:
    """Just enough of a WebSocket client to talk to Chrome's DevTools protocol."""

    def __init__(self, ws_url):
        u = urllib.parse.urlparse(ws_url)
        self.sock = socket.create_connection((u.hostname, u.port), timeout=30)
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f"GET {u.path} HTTP/1.1\r\nHost: {u.hostname}:{u.port}\r\nUpgrade: websocket\r\n"
                           f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        self.buf = bytearray()
        while b"\r\n\r\n" not in self.buf:
            self.buf += self._recv_chunk()
        header, _, rest = bytes(self.buf).partition(b"\r\n\r\n")
        if b" 101 " not in header.split(b"\r\n", 1)[0]:
            raise ConnectionError("DevTools WebSocket handshake failed")
        self.buf = bytearray(rest)
        self.next_id = 0

    def _recv_chunk(self):
        chunk = self.sock.recv(1 << 16)
        if not chunk:
            raise ConnectionError("DevTools connection closed")
        return chunk

    def _take(self, n):
        while len(self.buf) < n:
            self.buf += self._recv_chunk()
        out = bytes(self.buf[:n])
        del self.buf[:n]
        return out

    def _send(self, text, opcode=0x1):
        payload = text.encode() if isinstance(text, str) else text
        n = len(payload)
        head = bytearray([0x80 | opcode])
        if n < 126:
            head.append(0x80 | n)
        elif n < 1 << 16:
            head += bytes([0x80 | 126]) + struct.pack(">H", n)
        else:
            head += bytes([0x80 | 127]) + struct.pack(">Q", n)
        mask = os.urandom(4)
        self.sock.sendall(bytes(head) + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(payload)))

    def _recv(self):
        data = bytearray()
        while True:
            b1, b2 = self._take(2)
            n = b2 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._take(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._take(8))[0]
            mask = self._take(4) if b2 & 0x80 else None
            payload = self._take(n)
            if mask:
                payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
            opcode = b1 & 0x0F
            if opcode == 0x8:
                raise ConnectionError("DevTools connection closed")
            if opcode == 0x9:
                self._send(payload, opcode=0xA)
                continue
            data += payload
            if b1 & 0x80:
                return data.decode()

    def call(self, method, **params):
        self.next_id += 1
        self._send(json.dumps({"id": self.next_id, "method": method, "params": params}))
        while True:
            msg = json.loads(self._recv())
            if msg.get("id") == self.next_id:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error'].get('message')}")
                return msg.get("result", {})

    def eval(self, expression):
        res = self.call("Runtime.evaluate", expression=expression, returnByValue=True, awaitPromise=True)
        if "exceptionDetails" in res:
            raise RuntimeError(f"page script failed: {res['exceptionDetails'].get('text')}")
        return res["result"].get("value")

    def key(self, name, code, vk):
        for kind in ("keyDown", "keyUp"):
            self.call("Input.dispatchKeyEvent", type=kind, key=name, code=code, windowsVirtualKeyCode=vk)

    def close(self):
        self.sock.close()


def find_chrome(explicit):
    for c in [explicit, os.environ.get("CHROME"), *CHROME_CANDIDATES]:
        if c and Path(c).exists():
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        if shutil.which(name):
            return shutil.which(name)
    return None


def load(cdp, url, width):
    cdp.call("Emulation.setDeviceMetricsOverride", width=width, height=760, deviceScaleFactor=1, mobile=False)
    cdp.eval("window.__checkSiteOld = true")
    cdp.call("Page.navigate", url=url)
    deadline = time.time() + 15
    while time.time() < deadline:
        try:
            if cdp.eval("!window.__checkSiteOld && document.readyState === 'complete'"):
                break
        except RuntimeError:
            pass  # navigation in progress
        time.sleep(0.05)
    else:
        raise RuntimeError(f"timed out loading {url}")
    cdp.eval("document.fonts.ready.then(() => true)")


FOCUS_INFO = """(() => {
  const el = document.activeElement;
  if (!el || el === document.body) return null;
  const own = getComputedStyle(el), r = el.getBoundingClientRect();
  // Story cards ring the whole card instead of the title link (base.css).
  const card = own.outlineStyle === 'none' ? el.closest('.story-card') : null;
  const cs = card ? getComputedStyle(card) : own;
  return { text: (el.textContent || el.getAttribute('aria-label') || el.tagName).trim().replace(/\\s+/g, ' '),
           skip: el.classList.contains('skip-link'), visible: el.matches(':focus-visible'),
           style: cs.outlineStyle, width: parseFloat(cs.outlineWidth) || 0,
           x: Math.round(r.left + scrollX), y: Math.round(r.top + scrollY) };
})()"""

# checkVisibility() also excludes content in closed story sections (hidden="until-found", D-025).
COUNT_FOCUSABLE = """[...document.querySelectorAll('a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])')]
  .filter(e => !e.disabled && e.getClientRects().length > 0 && (!e.checkVisibility || e.checkVisibility())).length"""


def keyboard_pass(cdp, url, rel, r):
    where = f"{rel} (keyboard @{KEYBOARD_WIDTH}px)"
    load(cdp, url, KEYBOARD_WIDTH)
    expected = cdp.eval(COUNT_FOCUSABLE)
    stops = []
    for i in range(expected + 1):
        cdp.key("Tab", "Tab", 9)
        info = cdp.eval(FOCUS_INFO)
        if info is None or (i > 0 and info["skip"]):
            break
        stops.append(info)
    r.check(bool(stops) and stops[0]["skip"], where, "first Tab should reach the skip link")
    r.check(len(stops) == expected, where, f"Tab reached {len(stops)} of {expected} focusable elements")
    for s in stops:
        r.check(s["visible"] and s["style"] != "none" and s["width"] >= 2, where,
                f'no visible focus outline on "{s["text"][:40]}"')
    for a, b in zip(stops, stops[1:]):
        same_row = abs(b["y"] - a["y"]) <= ROW_TOLERANCE
        down = b["y"] > a["y"] + ROW_TOLERANCE
        # Up and to the right = the top of the next column (e.g. a card with its own link list).
        next_column = b["y"] < a["y"] - ROW_TOLERANCE and b["x"] > a["x"] + ROW_TOLERANCE
        r.check(down or (same_row and b["x"] > a["x"]) or next_column, where,
                f'focus order jumps back from "{a["text"][:30]}" to "{b["text"][:30]}"')

    load(cdp, url, KEYBOARD_WIDTH)
    cdp.key("Tab", "Tab", 9)
    cdp.key("Enter", "Enter", 13)
    time.sleep(0.1)
    r.check(cdp.eval("document.activeElement.id") == "main", where, "skip link should move focus to <main>")


def run_browser(pages, r, args):
    chrome = find_chrome(args.chrome)
    if not r.check(chrome is not None, "browser", "Chrome/Chromium not found; pass --chrome PATH or set CHROME"):
        return
    shots = Path(args.shots).resolve() if args.shots else Path(tempfile.mkdtemp(prefix="check_site_shots_"))
    shots.mkdir(parents=True, exist_ok=True)

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(SITE)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{httpd.server_address[1]}/"

    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        debug_port = s.getsockname()[1]
    profile = tempfile.mkdtemp(prefix="check_site_chrome_")
    proc = subprocess.Popen([chrome, "--headless=new", f"--remote-debugging-port={debug_port}",
                             f"--user-data-dir={profile}", "--hide-scrollbars", "--no-first-run",
                             "--no-default-browser-check", "about:blank"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    cdp = None
    try:
        ws_url, deadline = None, time.time() + 20
        while not ws_url and time.time() < deadline:
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{debug_port}/json/list", timeout=2) as resp:
                    ws_url = next((t["webSocketDebuggerUrl"] for t in json.load(resp) if t.get("type") == "page"), None)
            except OSError:
                time.sleep(0.2)
        if not r.check(ws_url is not None, "browser", "could not connect to Chrome DevTools"):
            return
        cdp = CDP(ws_url)
        cdp.call("Page.enable")
        for rel in sorted(pages):
            url = base + rel
            for width in WIDTHS:
                load(cdp, url, width)
                sw, cw = cdp.eval("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
                r.check(sw <= cw, f"{rel} @{width}px", f"horizontal scroll ({sw}px of content in a {cw}px viewport)")
                png = cdp.call("Page.captureScreenshot", format="png", captureBeyondViewport=True)["data"]
                name = rel.removesuffix(".html").replace("/", "__")
                (shots / f"{name}-{width}.png").write_bytes(base64.b64decode(png))
            keyboard_pass(cdp, url, rel, r)
        print(f"Browser checks: {len(pages)} pages at {', '.join(map(str, WIDTHS))}px; keyboard at {KEYBOARD_WIDTH}px")
        print(f"Screenshots: {shots}")
    finally:
        if cdp:
            cdp.close()
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
        httpd.shutdown()
        shutil.rmtree(profile, ignore_errors=True)


# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--browser", action="store_true", help="also run browser checks in local Chrome")
    ap.add_argument("--shots", help="directory for screenshots (default: a new temp directory)")
    ap.add_argument("--chrome", help="path to Chrome or Chromium")
    ap.add_argument("--site", help="site directory to check (default: site/ in this repo)")
    ap.add_argument("--strict", action="store_true",
                    help="deploy gate: fail on placeholder/draft markers instead of warning (D-017)")
    args = ap.parse_args()

    global SITE, STRICT
    if args.site:
        SITE = Path(args.site).resolve()
    STRICT = args.strict

    if not SITE.is_dir():
        print(f"site/ not found at {SITE}")
        return 2
    r = Report()
    pages = run_static(r)
    print(f"Static checks: {len(pages)} pages")

    if args.browser:
        run_browser(pages, r, args)

    for title, items in (("ERRORS", r.errors), ("WARNINGS", r.warnings)):
        print(f"\n{title} ({len(items)})")
        for i in items:
            print(f"  - {i}")
    print(f"\nPassed: {r.passed} checks · Errors: {len(r.errors)} · Warnings: {len(r.warnings)}")
    return 1 if r.errors else 0


if __name__ == "__main__":
    sys.exit(main())
