/*
 * Print every <details> panel expanded (Career Journey, D-032).
 *
 * The panels are native <details>, so they open and close without this script.
 * CSS alone cannot force a closed <details> open on paper, so before printing this
 * opens each closed panel, and after printing it closes them again, leaving the
 * reader's own choice of open panels as it was.
 */
(function () {
  "use strict";

  var opened = [];

  window.addEventListener("beforeprint", function () {
    opened = Array.prototype.slice.call(document.querySelectorAll("details:not([open])"));
    opened.forEach(function (panel) {
      panel.open = true;
    });
  });

  window.addEventListener("afterprint", function () {
    opened.forEach(function (panel) {
      panel.open = false;
    });
    opened = [];
  });
})();
