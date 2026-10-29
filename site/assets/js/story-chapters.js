/*
 * Project Story chapters (D-035).
 *
 * Progressive enhancement: the HTML shows all four chapters one after another, and each
 * chapter button is a plain link to its chapter. This script turns the buttons into tabs
 * and shows one chapter at a time.
 *
 * - The page opens on the first chapter, or on the chapter a URL fragment points into
 *   (a chapter, or a section card inside it), scrolled to that target.
 * - Tabs: each tab's name is the chapter title and its summary is the description.
 *   Arrow keys, Home and End move between tabs and select them.
 * - "Next: …" selects the next chapter and moves focus to its tab.
 * - Below 1024px the buttons stack above the chapter, so after a tap (or Enter/Space) the
 *   selected chapter scrolls into view; "Next" does the same. The scroll is instant when the
 *   visitor prefers reduced motion. Arrow keys only switch tabs and never scroll.
 * - In-page links (such as footnotes) select the chapter holding their target.
 * - Hidden chapters use hidden="until-found" where supported, so find-in-page still
 *   reaches their text and selects the chapter.
 * - Printing shows every chapter (base.css, @media print).
 */
(function () {
  "use strict";

  var story = document.querySelector(".story--chapters");
  var list = story && story.querySelector(".chapter-tabs");
  if (!list) return;

  var untilFound = "onbeforematch" in document.body;
  var stacked = window.matchMedia("(max-width: 1023px)");
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  var tabs = Array.prototype.slice.call(list.querySelectorAll(".chapter-tab"));
  var panels = tabs.map(function (tab) {
    return document.getElementById(tab.getAttribute("href").slice(1));
  });

  story.classList.add("story--tabs");
  list.setAttribute("role", "tablist");
  list.setAttribute("aria-label", "Story chapters");

  tabs.forEach(function (tab, i) {
    var panel = panels[i];
    tab.setAttribute("role", "tab");
    tab.setAttribute("aria-controls", panel.id);
    tab.setAttribute("aria-labelledby", tab.id + "-title");
    tab.setAttribute("aria-describedby", tab.id + "-summary");
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("aria-labelledby", tab.id);

    tab.addEventListener("click", function (event) {
      event.preventDefault();
      select(i);
      showChapter(i);
    });
    panel.addEventListener("beforematch", function () { select(i); });
  });

  function select(index) {
    tabs.forEach(function (tab, i) {
      var on = i === index;
      tab.setAttribute("aria-selected", on ? "true" : "false");
      tab.setAttribute("tabindex", on ? "0" : "-1");
      if (on) panels[i].removeAttribute("hidden");
      else panels[i].setAttribute("hidden", untilFound ? "until-found" : "");
    });
  }

  list.addEventListener("keydown", function (event) {
    var current = tabs.indexOf(document.activeElement);
    if (current < 0) return;
    var next = { ArrowRight: current + 1, ArrowDown: current + 1, ArrowLeft: current - 1,
                 ArrowUp: current - 1, Home: 0, End: tabs.length - 1 }[event.key];
    if (next === undefined) {
      // A link role="tab" would not answer Space on its own.
      if (event.key === " ") { event.preventDefault(); select(current); showChapter(current); }
      return;
    }
    event.preventDefault();
    next = (next + tabs.length) % tabs.length;
    select(next);
    tabs[next].focus();
  });

  // On stacked layouts the chosen chapter starts below the buttons, out of sight: bring it up.
  function showChapter(index) {
    if (!stacked.matches) return;
    panels[index].scrollIntoView({ behavior: reducedMotion.matches ? "auto" : "smooth", block: "start" });
  }

  function indexFor(node) {
    for (var i = 0; i < panels.length; i++) {
      if (panels[i].contains(node)) return i;
    }
    return -1;
  }

  function targetOf(hash) {
    var id = hash ? decodeURIComponent(hash.slice(1)) : "";
    return id ? document.getElementById(id) : null;
  }

  // Select the chapter holding target, then scroll to it and move focus there.
  function reveal(target) {
    var index = indexFor(target);
    if (index < 0) return false;
    select(index);
    if (panels[index] === target) {
      tabs[index].focus();
      list.scrollIntoView();
    } else {
      if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
      target.focus();
      target.scrollIntoView();
    }
    return true;
  }

  // "Next: …" moves to the following chapter and its tab.
  story.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest(".chapter__next");
    if (!link) return;
    var index = indexFor(link);
    if (index < 0 || index + 1 >= tabs.length) return;
    event.preventDefault();
    select(index + 1);
    tabs[index + 1].focus({ preventScroll: true });
    if (stacked.matches) showChapter(index + 1);
    else list.scrollIntoView();
  });

  // Other in-page links (footnotes, shared section links) open the chapter they point into.
  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest('a[href^="#"]');
    if (!link || link.classList.contains("chapter-tab") || link.classList.contains("chapter__next")) return;
    var target = targetOf(link.hash);
    if (!target || indexFor(target) < 0) return;
    event.preventDefault();
    history.pushState(null, "", link.hash);
    reveal(target);
  });

  window.addEventListener("hashchange", function () {
    var target = targetOf(location.hash);
    if (target) reveal(target);
  });

  // Initial state: a fragment into a chapter wins; otherwise the first chapter.
  var initial = targetOf(location.hash);
  if (initial && indexFor(initial) >= 0) {
    select(indexFor(initial));
    initial.scrollIntoView();
  } else {
    select(0);
  }
})();
