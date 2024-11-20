let nav_toggle = document.getElementById('nav-toggle');

nav_toggle.addEventListener('click', function() {
  let nav = document.getElementById('nav-list');
  nav.classList.toggle('hidden');
  console.log("click")
});