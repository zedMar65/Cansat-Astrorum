let nav_toggle = document.getElementById('nav-toggle');
let nav = document.getElementById('nav-list');

nav_toggle.addEventListener('click', function() {
  nav.classList.toggle('extended');
  nav_toggle.classList.toggle('active');
  console.log("click")
});