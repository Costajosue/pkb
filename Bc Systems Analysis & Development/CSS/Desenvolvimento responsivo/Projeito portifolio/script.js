const menuMobile = document.querySelector('.menu-mobile');
const navUl = document.querySelector('nav ul');

menuMobile.addEventListener('click', () => {
  navUl.style.display = navUl.style.display === 'flex' ? 'none' : 'flex';
});