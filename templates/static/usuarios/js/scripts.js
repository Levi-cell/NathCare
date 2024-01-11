const path = window.location.pathname;

const links = document.querySelectorAll('.navegacao-principal li a');

links.forEach(link => {
  if (link.getAttribute('href') === path) {
    link.classList.add('active');
    link.style.color = '#009738';
  }
});
