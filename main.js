// Main JS logic for Navigation & Intersection Observers
document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Logistics
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const drawerCloseBtn = document.querySelector('.drawer-close');
    const mobileDrawer = document.querySelector('.mobile-drawer');
    const backdrop = document.querySelector('.backdrop');

    function toggleMenu() {
        const isOpen = mobileDrawer.classList.contains('open');
        if (isOpen) {
            mobileDrawer.classList.remove('open');
            backdrop.classList.remove('open');
        } else {
            mobileDrawer.classList.add('open');
            backdrop.classList.add('open');
        }
    }

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', toggleMenu);
    if (drawerCloseBtn) drawerCloseBtn.addEventListener('click', toggleMenu);
    if (backdrop) backdrop.addEventListener('click', toggleMenu);

    // 2. Intersection Observer for Scroll Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // 15% visibility triggers it
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);

                // Trigger counter animation if it's a stat number
                if (entry.target.classList.contains('stat-num')) {
                    animateCounter(entry.target);
                }
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    animatedElements.forEach(el => scrollObserver.observe(el));

    // 3. Counter Animation Function
    function animateCounter(el) {
        const targetStr = el.getAttribute('data-target').replace(/,/g, '');
        const target = parseInt(targetStr, 10);

        if (isNaN(target) || target <= 0) {
            el.innerText = targetStr; // fallback if target is 0 or invalid
            return;
        }

        const duration = 2000; // ms
        const fps = 60;
        const totalFrames = Math.round((duration / 1000) * fps);
        let frame = 0;

        const timer = setInterval(() => {
            frame++;
            const progress = frame / totalFrames;
            const current = Math.round(target * progress);

            if (frame >= totalFrames) {
                el.innerText = target;
                clearInterval(timer);
            } else {
                el.innerText = current;
            }
        }, 1000 / fps);
    }

    // 4. Parallax Effect on Hero
    const parallaxEl = document.querySelector('.parallax-img');
    if (parallaxEl) {
        window.addEventListener('scroll', () => {
            // Disable on mobile roughly
            if (window.innerWidth > 768) {
                let scrollPosition = window.pageYOffset;
                parallaxEl.style.transform = `translateY(${scrollPosition * 0.5}px)`;
            }
        });
    }
});
