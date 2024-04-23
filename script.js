//Script for the slider menu on the chatbot page 
document.addEventListener('DOMContentLoaded', function() {
    // Check if the menuToggle and sideMenu elements exist
    const menuToggle = document.getElementById('menuToggle');
    const sideMenu = document.getElementById('sideMenu');
    const closeMenu = document.getElementById('closeMenu');

    // Add event listeners only if the elements exist
    if (menuToggle && sideMenu && closeMenu) {
        menuToggle.addEventListener('click', function() {
            sideMenu.style.left = '0';
        });

        closeMenu.addEventListener('click', function() {
            sideMenu.style.left = '-350px';
        });
    }

    // Check if the image element exists
    const image = document.querySelector('.header1 img');
    if (image) {
        image.addEventListener('click', stopAnimation);
    }

    function stopAnimation() {
        if (image) {
            image.style.animation = 'none';
        }
    }
});

// Script for the FAQ page
// Check if the faq-question elements exist
document.querySelectorAll('.faq-question').forEach(item => {
    item.addEventListener('click', () => {
        const answer = item.nextElementSibling;
        if (answer) {
            if (answer.style.display === 'none') {
                answer.style.display = 'block';
            } else {
                answer.style.display = 'none';
            }
        }
    });
});
