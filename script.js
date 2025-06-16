document.addEventListener('DOMContentLoaded', function() {

    function loadHTML(url, elementId, callback) {
        fetch(url)
            .then(response => response.text())
            .then(data => {
                document.getElementById(elementId).innerHTML = data;
                if (callback) callback();
            })
            .catch(error => console.error('Error loading HTML:', error));
    }

    function initializeMenu() {
        const menuToggle = document.getElementById('menuToggle');
        const mainNav = document.getElementById('mainNav');
        const navLinks = mainNav.querySelectorAll('a'); 

        if (menuToggle && mainNav) { 
            function toggleMenu() {
                mainNav.classList.toggle('menu-open');
                menuToggle.classList.toggle('open');
                document.body.classList.toggle('no-scroll', mainNav.classList.contains('menu-open'));
            }

            menuToggle.addEventListener('click', toggleMenu);

            navLinks.forEach(link => {
                link.addEventListener('click', function() {
                    if (mainNav.classList.contains('menu-open')) {
                        toggleMenu(); 
                    }
                });
            });
        }
    }

    loadHTML('header.html', 'header-placeholder', initializeMenu);

    // loadHTML('footer.html', 'footer-placeholder', null);
});