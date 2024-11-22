let nav_toggle = document.getElementById('nav-toggle');
let nav = document.getElementById('nav-list');

nav.classList.add('hidden');

nav_toggle.addEventListener('click', function() {
  nav.classList.toggle('hidden');
  console.log("click")
});