import re

with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Treatments Section (#treatments)
old_treatments_pattern = r'(<section id="treatments" aria-labelledby="explained-title">.*?</section>)'

new_treatments = """<section id="treatments" aria-labelledby="explained-title">
            <div class="container">
                <div class="text-center max-w-3xl mx-auto mb-4">
                    <span class="hf-eyebrow mb-2">TREATMENTS EXPLAINED</span>
                    <div class="nemonic-separator mx-auto mb-3">
                        <div class="nemonic-line"></div>
                        <img src="logo-header.png" alt="nemonic" class="nemonic-icon" />
                        <div class="nemonic-line"></div>
                    </div>
                    <h2 class="hf-heading mb-3" id="explained-title">Understanding the <span
                            class="scribble">Treatments</span></h2>
                </div>

                <div class="dz-carousel-track-wrapper">
                    <div class="dz-carousel-track" role="region" aria-label="Under-eye darkness treatments">
                        <!-- 1. Tear Trough restoration -->
                        <article class="dz-treatment-card" id="t-tear-trough">
                            <div class="dz-card-media">
                                <img src="images/home/Under-eye-Hollowness.webp" alt="Tear Trough Restoration treatment"
                                    class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Tear Trough Restoration &ndash; For Softening Under-Eye Hollowness</h3>
                                    <p class="dz-card-text">Carefully placed hyaluronic acid fillers help restore volume beneath the eyes, softening hollowness and shadows that can contribute to a tired appearance.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Hyaluronic acid &middot; Restores volume &middot; Softens shadows</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 2. Illuminé Eye Infusion -->
                        <article class="dz-treatment-card" id="t-illumine-eye">
                            <div class="dz-card-media">
                                <img src="images/pigmentation/Illumine-Skin-Infusion.webp" alt="Illuminé Eye Infusion treatment"
                                    class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Illuminé Eye Infusion</h3>
                                    <p class="dz-card-text">An advanced micro-infusion treatment that delivers customised anti-pigmentation serums enriched with peptides and antioxidants into the skin. Designed to support hydration, radiance and promote smooth-looking skin.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">30 mins &middot; 24k Gold technology &middot; No downtime</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 3. Lumi-Eyes Protocol -->
                        <article class="dz-treatment-card" id="t-lumi-eyes">
                            <div class="dz-card-media">
                                <img src="images/home/Volume-Loss.webp" alt="Lumi-Eyes Protocol treatment"
                                    class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Lumi-Eyes Protocol</h3>
                                    <p class="dz-card-text">An injectable treatment using polynucleotide-based formulations to support under-eye skin quality, hydration and the appearance of fine lines and crepiness.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Polynucleotide &middot; Skin quality &middot; Fine lines &amp; crepiness</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 4. Eyecon Protocol -->
                        <article class="dz-treatment-card" id="t-eyecon">
                            <div class="dz-card-media">
                                <img src="images/pigmentation/chemical-peel.webp" alt="Eyecon Protocol treatment"
                                    class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Eyecon Protocol</h3>
                                    <p class="dz-card-text">A specialised under-eye protocol combining targeted professional treatments to improve the appearance of pigmentation, fine lines and tired-looking skin.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Targeted protocol &middot; Pigment &amp; lines &middot; Refreshing</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 5. Under-Eye Skin Boosters -->
                        <article class="dz-treatment-card" id="t-skin-boosters">
                            <div class="dz-card-media">
                                <img src="images/pigmentation/Skin-Boosters.webp" alt="Under-Eye Skin Boosters treatment"
                                    class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Under-Eye Skin Boosters &ndash; For Hydration and Skin Quality</h3>
                                    <p class="dz-card-text">Selected injectable formulations help improve hydration, elasticity and skin quality, particularly where thin, dehydrated skin contributes to a tired appearance.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Hyaluronic acid &middot; Deep hydration &middot; Elasticity</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 6. Anti Wrinkle injections -->
                        <article class="dz-treatment-card" id="t-anti-wrinkle">
                            <div class="dz-card-media">
                                <img src="images/home/Fine-Lines-Wrinkles.webp" alt="Anti Wrinkle Injections treatment"
                                    class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Anti Wrinkle injections</h3>
                                    <p class="dz-card-text">Targeted neuromodulator injections help soften expression-related lines around the eyes, including crow's feet, for a more rested appearance.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Neuromodulator &middot; Crow's feet &middot; Expression softening</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 7. PRP -->
                        <article class="dz-treatment-card" id="t-prp">
                            <div class="dz-card-media">
                                <img src="images/pigmentation/Microneedling-with-Regenerative.webp"
                                    alt="PRP For Skin Rejuvenation" class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">PRP &ndash; For Skin Rejuvenation</h3>
                                    <p class="dz-card-text">A concentration of platelets derived from the individual's own blood. It may be used as part of a skin-rejuvenation approach to support skin quality and improve the appearance of fine lines and delicate under-eye skin.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Autologous platelets &middot; Cellular rejuvenation &middot; Fine lines</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 8. Laser De-puffing (Endo) -->
                        <article class="dz-treatment-card" id="t-laser-depuffing">
                            <div class="dz-card-media">
                                <img src="images/pigmentation/Advanced-Pigment-Laser.webp"
                                    alt="Laser De-puffing Endo treatment" class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Laser De-puffing (Endo)</h3>
                                    <p class="dz-card-text">A minimally invasive laser-based procedure intended to address selected under-eye tissue fullness and improve contour and skin firmness.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Minimally invasive &middot; Laser contouring &middot; Improves firmness</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 9. Advanced Depigmentation Peels -->
                        <article class="dz-treatment-card" id="t-depigmentation-peels">
                            <div class="dz-card-media">
                                <img src="images/pigmentation/Advanced-Depigmentation-Peels.webp"
                                    alt="Advanced Depigmentation Peels" class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Advanced Depigmentation Peels</h3>
                                    <p class="dz-card-text">Carefully selected peel formulations help improve superficial pigmentation and uneven tone around the eyes, with protocols tailored to this delicate area.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Tailored formulations &middot; Superficial pigment &middot; Delicate eye area</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>

                        <!-- 10. Medical-Grade Skincare -->
                        <article class="dz-treatment-card" id="t-skincare">
                            <div class="dz-card-media">
                                <img src="images/pigmentation/Medical-Grade-Skin-Brightening.webp"
                                    alt="Medical-Grade Skincare for delicate under-eye skin" class="dz-card-img" loading="lazy" />
                            </div>
                            <div class="dz-card-body">
                                <div class="dz-card-main">
                                    <h3 class="dz-card-title">Medical-Grade Skincare &ndash; For Delicate Under-Eye Skin</h3>
                                    <p class="dz-card-text">Targeted skincare formulations may help maintain hydration, support the skin barrier, and improve the appearance of fine lines and dryness around the eyes.</p>
                                    <div class="dz-card-explore-wrap">
                                        <span class="dz-card-link pg-card-meta">Medical skincare &middot; Barrier support &middot; Hydration &amp; dryness</span>
                                    </div>
                                </div>
                                <div class="dz-card-footer">
                                    <a href="contact" class="dz-card-book-btn">
                                        <span>Book Now</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                    <a href="#" class="dz-card-more-btn">
                                        <span>Read More</span>
                                        <img src="nemonic1.png" class="btn-icon" alt="" />
                                    </a>
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ═══════════════════════════════════════════════════════════
             THE D'ZEN APPROACH / WHY D'ZEN
             ═══════════════════════════════════════════════════════════ -->
        <section class="hf-why-section" id="why-dzen" aria-labelledby="why-title">
            <div class="container">
                <div class="text-center max-w-3xl mx-auto mb-4">
                    <span class="hf-eyebrow mb-2">THE D’ZEN APPROACH</span>
                    <div class="nemonic-separator mx-auto mb-3">
                        <div class="nemonic-line"></div>
                        <img src="logo-header.png" alt="nemonic" class="nemonic-icon" />
                        <div class="nemonic-line"></div>
                    </div>
                    <h2 class="hf-heading mb-3" id="why-title">Why D’Zen for <span class="scribble">Under-Eye Darkness</span></h2>
                    <p class="hf-lead">
                        Because brighter eyes begin with a more considered approach.
                    </p>
                </div>

                <div class="hf-why-minimal-grid bx-why-grid" id="whyTrack">
                    <div class="hf-why-minimal-item">
                        <span class="pg-rec__tag mb-2 d-inline-block" style="color: var(--gold, #C5A880); font-size: 0.75rem; letter-spacing: 2px;">SCIENCE &amp; SERENITY</span>
                        <h3 class="hf-why-minimal-title">Understanding before brightening</h3>
                        <div class="hf-why-minimal-divider"></div>
                        <p class="hf-why-minimal-desc">
                            Under-eye darkness can be caused by pigmentation, thin skin, visible blood vessels or structural hollowness. We believe in understanding what lies beneath before deciding what to treat.
                        </p>
                    </div>
                    <div class="hf-why-minimal-item">
                        <span class="pg-rec__tag mb-2 d-inline-block" style="color: var(--gold, #C5A880); font-size: 0.75rem; letter-spacing: 2px;">INNER &amp; OUTER</span>
                        <h3 class="hf-why-minimal-title">Looking beyond the eye area</h3>
                        <div class="hf-why-minimal-divider"></div>
                        <p class="hf-why-minimal-desc">
                            The delicate skin around the eyes can reflect genetics, skin quality, allergies, lifestyle and overall well-being. Our approach considers these wider influences alongside targeted aesthetic care.
                        </p>
                    </div>
                    <div class="hf-why-minimal-item">
                        <span class="pg-rec__tag mb-2 d-inline-block" style="color: var(--gold, #C5A880); font-size: 0.75rem; letter-spacing: 2px;">ENHANCEMENT &amp; RESTRAINT</span>
                        <h3 class="hf-why-minimal-title">Refresh without changing your expression</h3>
                        <div class="hf-why-minimal-divider"></div>
                        <p class="hf-why-minimal-desc">
                            The aim is to soften darkness, address hollowness and improve skin quality while preserving the natural contours and character of your eyes.
                        </p>
                    </div>
                </div>

                <div class="text-center mt-5">
                    <p style="font-family: 'Playfair Display', Georgia, serif; font-style: italic; font-size: 1.25rem; color: #DFC09C; max-width: 650px; margin: 0 auto; line-height: 1.6;">
                        &ldquo;The goal isn't to change your eyes. It's to help them look as refreshed as you feel.&rdquo;
                    </p>
                </div>
            </div>

            <!-- Curvy separator: Dark → Cream (#FDF8F3) -->
            <div class="section-separator" aria-hidden="true" style="margin-top: 30px;">
                <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                    <path fill="#FDF8F3" d="M0,60 C380,150 1060,-30 1440,60 L1440,120 L0,120 Z"></path>
                </svg>
            </div>
        </section>"""

content, count = re.subn(old_treatments_pattern, new_treatments, content, count=1, flags=re.DOTALL)
assert count == 1, "Treatments replacement failed"

# 2. Update Video Showcase section
old_video = """                    <h2 class="hf-heading mb-3">
                        Watch Pigmentation Care in <span class="scribble">Action</span>
                    </h2>
                    <p class="hf-lead">
                        Explore pigmentation treatment highlights and expert insights from D’Zen Derma on YouTube.
                    </p>"""

new_video = """                    <h2 class="hf-heading mb-3">
                        Watch Under-Eye Care in <span class="scribble">Action</span>
                    </h2>
                    <p class="hf-lead">
                        Explore under-eye treatment highlights and expert insights from D’Zen Derma on YouTube.
                    </p>"""

assert old_video in content, "old_video not found"
content = content.replace(old_video, new_video, 1)

# Video card title and alt
content = content.replace('data-title="Pigmentation at D&rsquo;Zen Derma"', 'data-title="Under-Eye Care at D&rsquo;Zen Derma"', 1)
content = content.replace('alt="Pigmentation at D&rsquo;Zen Derma"', 'alt="Under-Eye Care at D&rsquo;Zen Derma"', 1)

# 3. Update FAQs section
old_faq_pattern = r'(<section id="faq">.*?</section>)'

new_faq = """<section id="faq">
            <div class="container">
                <div class="text-center max-w-3xl mx-auto mb-3">
                    <span class="hf-eyebrow mb-2">CLEAR ANSWERS</span>
                    <div class="nemonic-separator mx-auto mb-3">
                        <div class="nemonic-line"></div>
                        <img src="logo-header.png" alt="nemonic" class="nemonic-icon" />
                        <div class="nemonic-line"></div>
                    </div>
                    <h2 class="hf-heading mb-3">Frequently Asked <span class="scribble">Questions</span></h2>
                    <p class="hf-lead">Everything you need to know about under-eye darkness, hollowness and treatment.</p>
                </div>

                <div class="row g-4 g-lg-5 align-items-start pg-faq-row">
                    <div class="col-lg-7 pg-faq-list" id="pgFaqList">
                        <!-- FAQ 1 -->
                        <details class="hf-faq-item" name="undereye-faq" open>
                            <summary class="hf-faq-summary">
                                <span>What causes under-eye hollowness?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                Under-eye hollowness can be caused by genetics, facial anatomy, age-related volume loss, changes in fat distribution, and thinning of the skin beneath the eyes.
                            </div>
                        </details>

                        <!-- FAQ 2 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Why do my eyes look sunken or tired even when I sleep well?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                The appearance of tired eyes may be related to natural under-eye anatomy, volume distribution, shadows, pigmentation, or skin thinning rather than lack of sleep.
                            </div>
                        </details>

                        <!-- FAQ 3 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Is under-eye hollowness the same as dark circles?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                No. Hollowness refers to a depression or loss of volume beneath the eyes, while dark circles refer to darker colouring in the under-eye area. However, hollowness can create shadows that make dark circles appear more prominent.
                            </div>
                        </details>

                        <!-- FAQ 4 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Can under-eye hollowness be improved?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                Depending on its cause, the appearance of under-eye hollowness may be improved with selected procedures that address volume, skin quality, or associated concerns. Suitability depends on individual anatomy and assessment.
                            </div>
                        </details>

                        <!-- FAQ 5 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Is under-eye hollowness caused by ageing?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                Ageing can contribute to under-eye hollowness through changes in facial fat, skin elasticity, and underlying support. However, it can also be present in younger individuals due to genetics and natural facial structure.
                            </div>
                        </details>

                        <!-- FAQ 6 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Can under-eye hollowness occur at a young age?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                Yes. Some people naturally have deeper tear troughs or less volume beneath the eyes due to their facial anatomy and genetics.
                            </div>
                        </details>

                        <!-- FAQ 7 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>How many sessions are required to improve under-eye hollowness?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                The number of sessions depends on the selected procedure, degree of hollowness, skin quality, and individual goals. Some options may involve one session, while others may require multiple sessions.
                            </div>
                        </details>

                        <!-- FAQ 8 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Are procedures for under-eye hollowness safe?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                The under-eye area is delicate and contains important blood vessels and structures. All procedures require careful assessment and an experienced medical professional. Each procedure has its own risks, and suitability should be determined during consultation.
                            </div>
                        </details>

                        <!-- FAQ 9 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Does under-eye hollowness cause dark circles?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                Hollowness can create shadows beneath the eyes, making the area appear darker. Pigmentation, visible blood vessels, and skin thinning can also contribute to dark circles.
                            </div>
                        </details>

                        <!-- FAQ 10 -->
                        <details class="hf-faq-item" name="undereye-faq">
                            <summary class="hf-faq-summary">
                                <span>Can under-eye hollowness return after improvement?</span>
                                <div class="hf-faq-icon">+</div>
                            </summary>
                            <div class="hf-faq-body">
                                Natural ageing and changes in facial volume continue over time. The longevity of improvement depends on the procedure, individual anatomy, and natural ageing process.
                            </div>
                        </details>

                        <div class="pg-faq-more">
                            <button type="button" class="dz-cta" id="pgFaqMore" aria-controls="pgFaqList"
                                aria-expanded="false">
                                <span>Read More FAQs</span>
                                <img src="nemonic1.png" class="btn-icon" alt="" />
                            </button>
                        </div>
                    </div>

                    <!-- Enquiry form -->
                    <div class="col-lg-5">
                        <div class="contact-form-card pg-faq-form">
                            <div class="form-header mb-4">
                                <span class="pg-form-eyebrow">ONLINE ENQUIRY</span>
                                <h3 class="pg-form-title">Ask About Under-Eye Care</h3>
                                <p class="pg-form-sub">Share your concern and our team will call you back to plan your skin assessment.</p>
                            </div>

                            <form accept-charset="UTF-8" action="https://app.formester.com/forms/nebkRsfEL/submissions"
                                method="POST" id="pgEnquiryForm" novalidate>
                                <input type="hidden" name="page" value="Under-Eye Darkness" />
                                <div class="row g-3">
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <input type="text" class="form-control" id="pgName" name="name"
                                                placeholder="Your Full Name" autocomplete="name" required>
                                            <label for="pgName">Full Name*</label>
                                            <div class="invalid-feedback">Full name should contain only letters and spaces (min 2 characters).</div>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <input type="tel" class="form-control" id="pgPhone" name="phone"
                                                placeholder="Phone Number" inputmode="numeric" maxlength="10"
                                                autocomplete="tel" required>
                                            <label for="pgPhone">Phone Number*</label>
                                            <div class="invalid-feedback">Phone number must contain only numbers and be exactly 10 digits.</div>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <input type="email" class="form-control" id="pgEmail" name="email"
                                                placeholder="Your Email" autocomplete="email">
                                            <label for="pgEmail">Email Address</label>
                                            <div class="invalid-feedback">Please enter a valid email address.</div>
                                        </div>
                                    </div>
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <textarea class="form-control" placeholder="Tell us about your concern"
                                                id="pgMessage" name="message"></textarea>
                                            <label for="pgMessage">Tell us about your concern</label>
                                        </div>
                                    </div>
                                    <div class="col-12 mt-3">
                                        <button type="submit" class="dz-cta w-100 justify-content-center"
                                            id="pgSubmitBtn">
                                            <span>Book Consultation</span>
                                            <img src="nemonic1.png" class="btn-icon" alt="" />
                                        </button>
                                        <div class="pg-form-note">
                                            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#8B4513"
                                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                                                aria-hidden="true">
                                                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                                                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                            </svg>
                                            <span>Your information is strictly confidential &amp; will never be shared.</span>
                                        </div>
                                    </div>
                                </div>
                            </form>

                            <div id="pgEnquirySuccess" class="text-center py-4" hidden>
                                <div class="pg-success-icon">
                                    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#8B4513"
                                        stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
                                        <polyline points="20 6 9 17 4 12"></polyline>
                                    </svg>
                                </div>
                                <span class="pg-form-eyebrow">MESSAGE RECEIVED</span>
                                <h3 class="pg-form-title">Thank You</h3>
                                <p class="pg-form-sub mb-0">Your enquiry has been submitted. Our patient care team will get back to you within 24 hours.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

content, count = re.subn(old_faq_pattern, new_faq, content, count=1, flags=re.DOTALL)
assert count == 1, "FAQ replacement failed"

# 4. Update Related Concerns section
old_related_first_card = """                        <!-- TODO: link each card to its concern page once created -->
                        <a href="acne-scars.html" class="hf-related-card">
                            <h3 class="hf-related-card__title">Acne Scars</h3>
                            <div class="hf-related-card__divider"></div>
                            <p class="hf-related-card__desc">Smooth uneven texture left behind by past breakouts.</p>
                            <span class="hf-related-card__action">
                                <span>Learn More</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M5 12h14" />
                                    <path d="m12 5 7 7-7 7" />
                                </svg>
                            </span>
                        </a>"""

new_related_first_card = """                        <a href="pigmentation.html" class="hf-related-card">
                            <h3 class="hf-related-card__title">Pigmentation</h3>
                            <div class="hf-related-card__divider"></div>
                            <p class="hf-related-card__desc">Even skin tone and fade stubborn marks with doctor-led protocols.</p>
                            <span class="hf-related-card__action">
                                <span>Learn More</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M5 12h14" />
                                    <path d="m12 5 7 7-7 7" />
                                </svg>
                            </span>
                        </a>
                        <a href="acne-scars.html" class="hf-related-card">
                            <h3 class="hf-related-card__title">Acne Scars</h3>
                            <div class="hf-related-card__divider"></div>
                            <p class="hf-related-card__desc">Smooth uneven texture left behind by past breakouts.</p>
                            <span class="hf-related-card__action">
                                <span>Learn More</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M5 12h14" />
                                    <path d="m12 5 7 7-7 7" />
                                </svg>
                            </span>
                        </a>"""

assert old_related_first_card in content, "old_related_first_card not found"
content = content.replace(old_related_first_card, new_related_first_card, 1)

with open('under-eye-darkness.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Part 2: Treatments, Why D'Zen approach, Video showcase, FAQs and Related Services updated successfully.")
