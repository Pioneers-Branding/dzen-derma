/**
 * D'Zen Derma - Dynamic Partials Include Loader
 * Loads include/header.html and include/footer.html into #site-header and #site-footer.
 * When changes are made to header.html or footer.html, every page reflects them automatically.
 */
(function () {
    'use strict';

    // Fallback embedded markup for offline or direct file:/// access where CORS blocks fetch
    const EMBEDDED_HEADER = `<!-- ═══════ Floating Pill Navbar v3 ═══════ -->
<nav id="pill-nav" class="pnav" aria-label="Main navigation">
    <!-- Left: Book Now -->
    <div class="pnav__left">
        <a href="../newthree.html#book" class="pnav__cta">
            Book
            <img src="nemonic1.png" class="btn-icon" alt="icon" />
        </a>
    </div>

    <!-- Center: logo -->
    <a href="index.html" class="pnav__logo" aria-label="Home">
        <img src="photos/logo1.png" alt="D'Zen Derma" />
    </a>

    <!-- Right: hamburger -->
    <div class="pnav__right">
        <button class="pnav__burger" id="pnav-burger" aria-label="Open menu">
            <span></span><span></span><span></span>
        </button>
    </div>
</nav>

<!-- Mobile drawer -->
<div class="pnav-overlay" id="pnav-overlay"></div>
<aside class="pnav-drawer" id="pnav-drawer" aria-label="Menu">
    <button class="pnav-drawer__close" id="pnav-close" aria-label="Close menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round">
            <path d="M18 6L6 18M6 6l12 12" />
        </svg>
    </button>
    <ul class="pnav-drawer__list">
        <li><a href="our-philosophy.html">Who we are <span>→</span></a></li>
        <li><a href="treatments.html">Treatments <span>→</span></a></li>
        <li><a href="concerns.html">Concerns <span>→</span></a></li>
        <li><a href="treatments.html#cat-wellness">Medicine &amp; Wellness Programmes <span>→</span></a></li>
        <li><a href="dzen-signatures.html">Signature Treatments <span>→</span></a></li>
        <li><a href="pre-bridal.html">Bridal Programs <span>→</span></a></li>
        <li><a href="men.html">Men's Aesthetics <span>→</span></a></li>
        <li><a href="workshops-training.html">Workshops &amp; Training <span>→</span></a></li>
        <li><a href="media.html">Press &amp; Media <span>→</span></a></li>
    </ul>
</aside>`;

    const EMBEDDED_FOOTER = `<style>
    /* Shared clinic locations section (loaded on every page via footer include) */
    .clinic-locations-section .container {
        max-width: 1280px !important;
        width: 100% !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-left: 24px !important;
        padding-right: 24px !important;
    }
</style>

<!-- ═══════ Clinic Locations Section ═══════ -->
<section class="clinic-locations-section" id="locations" aria-labelledby="locations-heading"
    style="padding-top: 25px !important;">
    <div class="container">
        <div class="section-header text-center mb-4 mb-lg-4">
            <span class="section-subtitle">OUR CLINICS</span>
            <div class="nemonic-separator">
                <div class="nemonic-line"></div>
                <img loading="lazy" decoding="async" src="logo-header.png" alt="nemonic" class="nemonic-icon" />
                <div class="nemonic-line"></div>
            </div>
            <h2 id="locations-heading" class="section-title">Two Locations. One Philosophy</h2>
            <p class="section-desc mx-auto" style="max-width: 760px; color: #5C4A3A;">
                Experience D’Zen Derma in South Delhi and Gurugram, where clinical expertise meets personalised
                aesthetic and wellness care.
            </p>
        </div>

        <!-- Tab Pills for Mobile View -->
        <div class="clinic-tabs" role="tablist" aria-label="Select Clinic Location">
            <div class="clinic-tabs__pill">
                <button class="clinic-tab active" role="tab" aria-selected="true" data-clinic="0">
                    <img loading="lazy" decoding="async" class="clinic-tab__img"
                        src="images/delhi-location-img.jpg" alt="Delhi Clinic" />
                    <span class="clinic-tab__info">
                        <span class="clinic-tab__name">New Delhi</span>
                        <span class="clinic-tab__role">Lajpat Nagar</span>
                    </span>
                </button>
                <button class="clinic-tab" role="tab" aria-selected="false" data-clinic="1">
                    <img loading="lazy" decoding="async" class="clinic-tab__img"
                        src="images/gurgaon-location-img.png" alt="Gurgaon Clinic" />
                    <span class="clinic-tab__info">
                        <span class="clinic-tab__name">Gurgaon</span>
                        <span class="clinic-tab__role">Golf Course Rd</span>
                    </span>
                </button>
            </div>
        </div>

        <div class="row g-4 justify-content-center clinic-locations-grid">
            <!-- Delhi Clinic -->
            <div class="col-lg-6 col-md-6 clinic-loc-col active" data-clinic-index="0">
                <article class="clinic-loc-card">
                    <div class="clinic-loc-card__media">
                        <img loading="lazy" decoding="async" src="images/delhi-location-img.jpg"
                            alt="D'Zen Derma Clinic, Lajpat Nagar, New Delhi" class="clinic-loc-card__img" />
                    </div>
                    <div class="clinic-loc-card__body">
                        <span class="clinic-loc-card__eyebrow">NEW DELHI</span>
                        <h3 class="clinic-loc-card__title">D'Zen Derma, Lajpat Nagar</h3>
                        <ul class="clinic-loc-card__info">
                            <li>
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                                    <circle cx="12" cy="10" r="3" />
                                </svg>
                                <span>18A, Ring Rd, Near Havells, Vikram Vihar, Lajpat Nagar 4, New Delhi</span>
                            </li>
                            <li>
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <path
                                        d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z" />
                                </svg>
                                <a href="tel:+919773771610">+91-9773771610</a>
                            </li>
                            <li>
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <rect x="2" y="4" width="20" height="16" rx="2" />
                                    <path d="m22 7-10 6L2 7" />
                                </svg>
                                <a href="mailto:care@dzenderma.com">care@dzenderma.com</a>
                            </li>
                        </ul>
                        <div class="clinic-loc-card__actions">
                            <a href="https://www.google.com/maps/place/D'Zen+Derma+by+Dr.+Aarushi+Passi:+Cosmetic+%26+Integrative+Skin+Clinic+in+Lajpat+Nagar,+Delhi/@28.5607867,77.2357829,728m/data=!3m2!1e3!4b1!4m6!3m5!1s0x390ce3e6ec57fafb:0xdad55619fcec33ab!8m2!3d28.5607867!4d77.2383578!16s%2Fg%2F11vxtv92jj?entry=ttu&amp;g_ep=EgoyMDI2MTEwOC4wIKXMDSoASAFQAw%3D%3D"
                                target="_blank" rel="noopener" class="dz-cta">
                                <span>Get Directions</span>
                                <img loading="lazy" decoding="async" src="nemonic1.png" class="btn-icon"
                                    style="width: 14px; height: 14px; object-fit: contain;" alt="icon" />
                            </a>
                        </div>
                    </div>
                </article>
            </div>

            <!-- Gurgaon Clinic -->
            <div class="col-lg-6 col-md-6 clinic-loc-col" data-clinic-index="1">
                <article class="clinic-loc-card">
                    <div class="clinic-loc-card__media">
                        <img loading="lazy" decoding="async" src="images/gurgaon-location-img.png"
                            alt="D'Zen Derma Clinic, Golf Course Road, Gurgaon" class="clinic-loc-card__img" />

                    </div>
                    <div class="clinic-loc-card__body">
                        <span class="clinic-loc-card__eyebrow">GURUGRAM</span>
                        <h3 class="clinic-loc-card__title">D'Zen Derma, Golf Course Road</h3>
                        <ul class="clinic-loc-card__info">
                            <li>
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                                    <circle cx="12" cy="10" r="3" />
                                </svg>
                                <span>Golf Course Road, Near DLF Phase 1, Sector 28, Gurugram, Haryana</span>
                            </li>
                            <li>
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <path
                                        d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z" />
                                </svg>
                                <a href="tel:+919773771610">+91-9773771610</a>
                            </li>
                            <li>
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                                    stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                                    <rect x="2" y="4" width="20" height="16" rx="2" />
                                    <path d="m22 7-10 6L2 7" />
                                </svg>
                                <a href="mailto:care@dzenderma.com">care@dzenderma.com</a>
                            </li>
                        </ul>
                        <div class="clinic-loc-card__actions">
                            <a href="https://www.google.com/maps/place/D'Zen+Derma+by+Dr.+Aarushi+Passi:+Cosmetic+%26+Integrative+Skin+Clinic+in+Gurgaon/@28.4719351,77.0908131,729m/data=!3m2!1e3!4b1!4m6!3m5!1s0x390d1960b0f6defd:0x3b2b5d165c87cb08!8m2!3d28.4719304!4d77.093388!16s%2Fg%2F11ll_3fb86?entry=ttu&amp;g_ep=EgoyMDI2MTEwOC4wIKXMDSoASAFQAw%3D%3D"
                                target="_blank" rel="noopener" class="dz-cta">
                                <span>Get Directions</span>
                                <img loading="lazy" decoding="async" src="nemonic1.png" class="btn-icon"
                                    style="width: 14px; height: 14px; object-fit: contain;" alt="icon" />
                            </a>
                        </div>
                    </div>
                </article>
            </div>
        </div>
    </div>
</section>

    <!-- ═══════════════════════════════════════════════════════════
     CTA + FOOTER OVERLAP SECTION
     ═══════════════════════════════════════════════════════════ -->
<div class="footer-stack-root">
    <!-- CTA Card -->
    <div class="footer-cta-card-wrapper">
        <div class="footer-cta-card">
            <div class="section-header text-center mb-4">
                <span class="section-subtitle">BEGIN YOUR JOURNEY</span>
                <div class="nemonic-separator mx-auto mb-3">
                    <div class="nemonic-line"></div>
                    <img src="logo-header.png" alt="nemonic" class="nemonic-icon" />
                    <div class="nemonic-line"></div>
                </div>
            </div>
            <h2 class="footer-cta-heading">Ready to reveal your most radiant self?</h2>
            <p class="footer-cta-sub">Join thousands who've discovered the art of effortless confidence — crafted for your skin, your story.</p>
            <a href="../newthree.html#book" class="dz-cta footer-cta-btn">
                <span>Book a Consultation</span>
                <img src="nemonic1.png" class="btn-icon" alt="icon" />
            </a>
        </div>
    </div>

    <!-- Footer Reveal Wrapper -->
    <div class="footer-reveal-wrapper">
        <footer class="site-footer" aria-label="Site footer">
            <div class="footer-top">
                <!-- Brand column -->
                <div class="footer-brand">
                    <a href="index.html" class="footer-logo" aria-label="D'Zen Derma home">
                        <img src="photos/logo1.png" alt="D'Zen Derma" style="display: block; height: 64px; width: auto; margin: 0 0 18px;" />
                    </a>
                    <p class="footer-tagline">
                        Where the finest techniques in aesthetic medicine reveal your most luminous, confident self. Crafted for your skin, your story.
                    </p>
                    <div class="footer-socials">
                        <a href="https://instagram.com/dzenderma" class="footer-social-icon" aria-label="Instagram" target="_blank" rel="noopener">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                                <circle cx="12" cy="12" r="4"></circle>
                                <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" stroke="none"></circle>
                            </svg>
                        </a>
                        <a href="https://www.facebook.com/DZenDerma/" class="footer-social-icon" aria-label="Facebook" target="_blank" rel="noopener">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                            </svg>
                        </a>
                        <a href="https://www.youtube.com/@DZenDerma" class="footer-social-icon" aria-label="YouTube" target="_blank" rel="noopener">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path>
                                <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon>
                            </svg>
                        </a>
                    </div>
                </div>

                <!-- Nav columns -->
                <div class="footer-nav-col">
                    <ul class="footer-nav-list">
                        <li><a href="treatments.html">AESTHETICS</a></li>
                        <li><a href="treatments.html#cat-wellness">FUNCTIONAL MEDICINE</a></li>
                        <li><a href="treatments.html#cat-wellness">INTEGRATIVE WELLNESS &amp; LONGEVITY</a></li>
                        <li><a href="treatments.html#cat-anti-ageing">REGENERATIVE AESTHETICS</a></li>
                        <li><a href="workshops-training.html">DOCTOR EDUCATION &amp; WORKSHOPS</a></li>
                    </ul>
                </div>
                <div class="footer-nav-col">
                    <ul class="footer-nav-list">
                        <li><a href="our-philosophy.html">WHO WE ARE</a></li>
                        <li><a href="treatments.html">TREATMENTS</a></li>
                        <li><a href="concerns.html">CONCERNS</a></li>
                        <li><a href="#">TESTIMONIALS</a></li>
                        <li><a href="contact.html">CONTACT US</a></li>
                    </ul>
                </div>

                <!-- Contact info column -->
                <div class="footer-contact-col">
                    <div class="footer-contact-row">
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Gurgaon Clinic</span>
                            <span class="footer-contact-value">Golf Course Road, Sector 28, Gurugram</span>
                        </div>
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Delhi Clinic</span>
                            <span class="footer-contact-value">Vikram Vihar, Lajpat Nagar 4, New Delhi</span>
                        </div>
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Phone &amp; WhatsApp</span>
                            <a href="tel:+919773771610" class="footer-contact-value footer-contact-link">+91-9773771610</a>
                        </div>
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Email</span>
                            <a href="mailto:rahul@dzenderma.com" class="footer-contact-value footer-contact-link">rahul@dzenderma.com</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="footer-divider"></div>

            <div class="footer-disclaimer">
                <p class="footer-disclaimer-title">DISCLAIMER:</p>
                <p class="footer-disclaimer-text">This website's information is exclusively intended to educate and raise awareness about dermatology. This is not to be considered a substitute for professional medical advice or a prescription. Since each individual and case is unique, the outcomes of any of the treatments indicated on the page may vary.</p>
            </div>

            <div class="footer-bottom">
                <p class="footer-copyright">© 2026, D'Zen Derma | All Rights Reserved | All prices are exclusive of tax</p>
                <div class="footer-legal-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms &amp; Conditions</a>
                    <a href="#">Booking &amp; Cancellation Policy</a>
                </div>
            </div>

            <div class="footer-bottom-strip"></div>
        </footer>
    </div>
</div>

<!-- Embossed Brand Section -->
<section class="embossed-section" id="brandSection">
    <div class="embossed-grain"></div>
    <div class="embossed-lighting"></div>

    <!-- Book Now Pill Button -->
    <a href="../newthree.html#book" class="book-pill-btn" aria-label="Book appointment">
        BOOK NOW
        <img src="nemonic1.png" alt="icon" class="btn-icon">
    </a>

    <!-- Debossed Typography Block -->
    <div class="typography-stage">
        <h1 class="deboss-wordmark" id="wordmark">D'ZEN DERMA</h1>
        <p class="deboss-tagline">Elevating You Inside Out</p>
    </div>
</section>
`;

    // Initialize Pill Navigation interactions
    function initPillNav() {
        const nav = document.getElementById('pill-nav');
        if (!nav) return;

        const burger = document.getElementById('pnav-burger');
        const closeBtn = document.getElementById('pnav-close');
        const drawer = document.getElementById('pnav-drawer');
        const overlay = document.getElementById('pnav-overlay');

        if (!burger || !drawer) return;

        if (burger._hasPnavListener) return;
        burger._hasPnavListener = true;

        function openDrawer() {
            drawer?.classList.add('is-open');
            overlay?.classList.add('is-open');
            burger?.classList.add('is-active');
        }
        function closeDrawer() {
            drawer?.classList.remove('is-open');
            overlay?.classList.remove('is-open');
            burger?.classList.remove('is-active');
        }

        burger.addEventListener('click', function (e) {
            e.stopPropagation();
            if (drawer.classList.contains('is-open')) closeDrawer();
            else openDrawer();
        });

        closeBtn?.addEventListener('click', function (e) {
            e.stopPropagation();
            closeDrawer();
        });

        overlay?.addEventListener('click', function (e) {
            e.stopPropagation();
            closeDrawer();
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') closeDrawer();
        });

        // Scroll listener for sticky & opaque transition
        let ticking = false;
        function onScroll() {
            if (ticking) return;
            ticking = true;
            requestAnimationFrame(function () {
                const y = window.scrollY;
                nav.classList.toggle('is-scrolled', y > 30);
                ticking = false;
            });
        }

        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();

        // Highlight active page link in the drawer
        const currentFile = window.location.pathname.split('/').pop() || 'index.html';
        const drawerLinks = drawer.querySelectorAll('.pnav-drawer__list a');
        drawerLinks.forEach(function (link) {
            const href = link.getAttribute('href');
            if (href && (href === currentFile || href.endsWith('/' + currentFile))) {
                link.classList.add('active');
            }
        });
    }

    // Expose init function globally so script.js can also call it
    window.initPillNav = initPillNav;

    // Fetch and inject an include snippet
    async function loadPartial(containerId, filename, callback) {
        const container = document.getElementById(containerId);
        if (!container) return;

        // Skip if already populated
        if (container.children && container.children.length > 0) {
            if (typeof callback === 'function') callback();
            return;
        }

        let loaded = false;
        const isHttp = window.location.protocol === 'http:' || window.location.protocol === 'https:';

        if (isHttp) {
            const candidatePaths = [
                'include/' + filename,
                'includes/' + filename,
                '../include/' + filename,
                '../includes/' + filename
            ];
            for (const path of candidatePaths) {
                try {
                    const res = await fetch(path + '?v=' + Date.now());
                    if (res.ok) {
                        const html = await res.text();
                        container.innerHTML = html;
                        loaded = true;
                        break;
                    }
                } catch (err) {
                    // Try next candidate
                }
            }
        }

        // On file:/// or fallback, initialize embedded HTML if container is empty
        if (!loaded) {
            const fallback = filename === 'header.html' ? EMBEDDED_HEADER : EMBEDDED_FOOTER;
            if (fallback && (!container.innerHTML || container.innerHTML.trim() === '')) {
                container.innerHTML = fallback;
            }
        }

        if (typeof callback === 'function') {
            callback();
        }
    }

    // Clinic location tabs (Delhi / Gurgaon) — delegated so it works after the footer is injected
    function initClinicTabs() {
        // If the page already has its own locations section, drop the footer copy to avoid duplicates
        const footer = document.getElementById('site-footer');
        const footerSection = footer && footer.querySelector('.clinic-locations-section');
        if (footerSection) {
            const pageHasOwn = Array.prototype.some.call(
                document.querySelectorAll('.clinic-locations-section'),
                function (s) { return !footer.contains(s); }
            );
            if (pageHasOwn) footerSection.remove();
        }

        if (document._hasClinicTabListener) return;
        document._hasClinicTabListener = true;

        document.addEventListener('click', function (e) {
            const tab = e.target.closest('.clinic-tab');
            if (!tab) return;
            const section = tab.closest('.clinic-locations-section');
            if (!section) return;

            const target = parseInt(tab.getAttribute('data-clinic'), 10);
            section.querySelectorAll('.clinic-tab').forEach(function (t, i) {
                t.classList.toggle('active', i === target);
                t.setAttribute('aria-selected', i === target ? 'true' : 'false');
            });
            section.querySelectorAll('.clinic-locations-grid .clinic-loc-col').forEach(function (c, i) {
                c.classList.toggle('active', i === target);
            });
        });
    }

    // Run loader
    function initIncludes() {
        loadPartial('site-header', 'header.html', initPillNav);
        loadPartial('site-footer', 'footer.html', initClinicTabs);
    }

    // Run immediately if containers are already in DOM, else on DOMContentLoaded
    if (document.getElementById('site-header') || document.getElementById('site-footer')) {
        initIncludes();
    } else if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initIncludes);
    } else {
        initIncludes();
    }
})();
