document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const sideMenu = document.getElementById('sideMenu');
    const closeMenu = document.getElementById('closeMenu');

    menuToggle.addEventListener('click', function() {
        sideMenu.style.left = '0';
    });

    closeMenu.addEventListener('click', function() {
        sideMenu.style.left = '-350px';
    });
});

const image = document.querySelector('.header1 img');
image.addEventListener('click', stopAnimation);
function stopAnimation() {
  image.style.animation = 'none';
}


