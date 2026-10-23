/*
 * Expandable Project Story sections (D-025).
 *
 * Progressive enhancement: the HTML has every section visible, so a reader without
 * JavaScript gets the full story. This script turns each section heading into a
 * button that opens its section, with one section open at a time.
 *
 * - On load, the section named in the story's data-open-on-load opens (or the
 *   section a URL fragment points into).
 * - In-page links ("On this page", footnotes) open the section that holds their
 *   target, close the others, and move focus there.
 * - Closed panels use hidden="until-found" where supported, so find-in-page still
 *   reaches their text and opens the section.
 * - Printing expands every section (base.css, @media print).
 */
(function () {
  "use strict";

  var story = document.querySelector(".story");
  var sections = story ? Array.prototype.slice.call(story.querySelectorAll(".story-section")) : [];
  if (!sections.length) return;

  var untilFound = "onbeforematch" in document.body;
  story.classList.add("story--expandable");

  var items = sections.map(function (section) {
    var heading = section.querySelector("h2");

    // Move everything after the heading into a panel.
    var panel = document.createElement("div");
    panel.className = "story-section__panel";
    panel.id = heading.id + "-panel";
    while (heading.nextSibling) panel.appendChild(heading.nextSibling);
    section.appendChild(panel);

    // The heading text becomes the control; the triangle is decorative.
    var button = document.createElement("button");
    button.type = "button";
    button.className = "story-section__toggle";
    button.setAttribute("aria-controls", panel.id);
    var triangle = document.createElement("span");
    triangle.className = "story-section__triangle";
    triangle.setAttribute("aria-hidden", "true");
    button.appendChild(triangle);
    while (heading.firstChild) button.appendChild(heading.firstChild);
    heading.appendChild(button);

    var item = { section: section, button: button, panel: panel };
    button.addEventListener("click", function () {
      if (button.getAttribute("aria-expanded") === "true") setOpen(item, false);
      else openOnly(item);
    });
    panel.addEventListener("beforematch", function () { openOnly(item); });
    return item;
  });

  function setOpen(item, open) {
    item.button.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) item.panel.removeAttribute("hidden");
    else item.panel.setAttribute("hidden", untilFound ? "until-found" : "");
  }

  function openOnly(item) {
    items.forEach(function (other) { setOpen(other, other === item); });
  }

  function itemFor(node) {
    for (var i = 0; i < items.length; i++) {
      if (items[i].section.contains(node)) return items[i];
    }
    return null;
  }

  function targetOf(hash) {
    var id = hash ? decodeURIComponent(hash.slice(1)) : "";
    return id ? document.getElementById(id) : null;
  }

  // Open the section holding target, then move focus: to the heading button when the
  // target is the section heading, otherwise to the target itself.
  function reveal(target) {
    var item = itemFor(target);
    if (!item) return false;
    openOnly(item);
    if (target.contains(item.button)) {
      item.button.focus();
    } else {
      if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
      target.focus();
    }
    target.scrollIntoView();
    return true;
  }

  // Initial state: a fragment into a section wins; otherwise the story's first section.
  var initial = targetOf(location.hash);
  var initialItem = initial && itemFor(initial);
  if (initialItem) {
    openOnly(initialItem);
    initial.scrollIntoView();
  } else {
    var first = document.getElementById(story.getAttribute("data-open-on-load") || "");
    openOnly(itemFor(first) || items[0]);
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest('a[href^="#"]');
    var target = link && targetOf(link.hash);
    if (!target || !itemFor(target)) return;
    event.preventDefault();
    history.pushState(null, "", link.hash);
    reveal(target);
  });

  window.addEventListener("hashchange", function () {
    var target = targetOf(location.hash);
    if (target) reveal(target);
  });
})();
