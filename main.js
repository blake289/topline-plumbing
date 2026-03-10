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
        const target = parseInt(el.getAttribute('data-target'), 10);
        const duration = 1500; // ms
        const stepTime = Math.abs(Math.floor(duration / target));
        let current = 0;

        const timer = setInterval(() => {
            current += Math.ceil(target / (duration / 16)); // ~60fps
            if (current >= target) {
                el.innerText = target + "+";
                clearInterval(timer);
            } else {
                el.innerText = current + "+";
            }
        }, 16);
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
