// Shared menu. The HTML is already on each page so it never flashes in late.
document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menuToggle');
    const mainNav = document.getElementById('mainNav');
    if (menuToggle && mainNav) {
        function closeMenu() {
            mainNav.classList.remove('menu-open');
            menuToggle.setAttribute('aria-expanded', 'false');
        }
        menuToggle.addEventListener('click', function () {
            const open = mainNav.classList.toggle('menu-open');
            menuToggle.setAttribute('aria-expanded', String(open));
        });
        mainNav.querySelectorAll('a').forEach(link => {
            if (link.getAttribute('href') === (location.pathname.split('/').pop() || 'index.html')) {
                link.setAttribute('aria-current', 'page');
            }
            link.addEventListener('click', closeMenu);
        });
        document.addEventListener('keydown', event => {
            if (event.key === 'Escape' && mainNav.classList.contains('menu-open')) {
                closeMenu();
                menuToggle.focus();
            }
        });
        document.addEventListener('click', event => {
            if (!event.target.closest('header')) closeMenu();
        });
        matchMedia('(min-width: 701px)').addEventListener('change', closeMenu);
    }

    // Background film. A blocked autoplay still leaves the poster image.
    const video = document.getElementById('droneVideo');
    if (!video) return;
    const section = document.querySelector('.flight-scroll');
    const hero = document.querySelector('.flight-hero');
    const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
    let wantsToPlay = !reducedMotion.matches;
    let visible = true;
    function playVideo() {
        video.play().catch(() => {}); // Autoplay may be blocked; the poster remains.
    }
    new IntersectionObserver(entries => {
        visible = entries[0].isIntersecting;
        if (visible && wantsToPlay && !document.hidden) playVideo(); else video.pause();
    }, { threshold: .05 }).observe(hero);
    document.addEventListener('visibilitychange', () => {
        if (!document.hidden && visible && wantsToPlay) playVideo(); else video.pause();
    });
    reducedMotion.addEventListener('change', () => {
        wantsToPlay = !reducedMotion.matches;
        if (wantsToPlay && visible) playVideo(); else video.pause();
        updateFilm();
    });
    // Keep the scroll handler light; change only transforms on the next frame.
    let scheduled = false;
    function updateFilm() {
        scheduled = false;
        const progress = reducedMotion.matches ? 0 : Math.max(0, Math.min(1, -section.getBoundingClientRect().top / innerHeight));
        hero.style.setProperty('--film-scale', 1 + progress * .08);
        hero.style.setProperty('--film-offset', (-progress * 55) + 'px');
    }
    addEventListener('scroll', () => {
        if (!scheduled) { scheduled = true; requestAnimationFrame(updateFilm); }
    }, { passive: true });
    updateFilm();
});
