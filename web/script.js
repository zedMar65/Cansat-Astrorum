let nav_toggle = document.querySelector('.nav-toggle');

nav_toggle.addEventListener('click', function() {
  let nav = document.querySelector('.nav');
  nav.classList.toggle('nav--visible');
});