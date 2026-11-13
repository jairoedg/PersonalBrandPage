/* Mobile menu (below 768px). Adds a Menu button that opens the page links in a panel under the
   header. Without this script the header stays as it is at every width. No framework (D-011). */
(function () {
  var header = document.querySelector('.site-header');
  if (!header) { return; }
  var toggle = header.querySelector('.nav-toggle');
  var list = header.querySelector('#site-menu');
  if (!toggle || !list) { return; }

  var label = toggle.querySelector('.nav-toggle__label');
  var icon = toggle.querySelector('.nav-toggle__icon');
  var MENU_ICON = '<path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h16"/>';
  var CLOSE_ICON = '<path d="M6 6l12 12"/><path d="M18 6L6 18"/>';
  var wide = window.matchMedia('(min-width: 768px)');

  function setOpen(open) {
    header.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    label.textContent = open ? 'Close' : 'Menu';
    icon.innerHTML = open ? CLOSE_ICON : MENU_ICON;
  }

  header.classList.add('has-menu');
  toggle.hidden = false;
  setOpen(false);

  toggle.addEventListener('click', function () {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });

  document.addEventListener('click', function (event) {
    if (!header.contains(event.target)) { setOpen(false); }
  });

  function onResize() {
    if (wide.matches) { setOpen(false); }
  }
  if (wide.addEventListener) { wide.addEventListener('change', onResize); }
  else { wide.addListener(onResize); }
})();
