with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the CSS override block
old_css = """        /* Related concerns */
        .dz-page-pigmentation .bx-related-track .hf-related-card {
            min-height: 0;
        }

        /* All four cards in one centred row; card content centred */
        @media (min-width: 992px) {
            html body.dz-page-pigmentation #related-services .bx-related-track {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 20px;
                max-width: 1140px;
                margin: 0 auto;
                overflow: visible;
                cursor: default;
            }

            html body.dz-page-pigmentation #related-services .bx-related-track .hf-related-card {
                flex: none;
                max-width: none;
                width: 100%;
            }
        }

        html body.dz-page-pigmentation #related-services .bx-related-track .hf-related-card {
            align-items: center;
            text-align: center;
        }

        html body.dz-page-pigmentation #related-services .bx-related-track .hf-related-card__divider {
            align-self: stretch;
        }

        html body.dz-page-pigmentation #related-services .bx-related-track .hf-related-card__action {
            justify-content: center;
        }"""

new_css = """        /* ── Related Concerns Section (Horizontal Scroll like laser-hair-removal.html) ── */
        html body #related-services.hf-related-section {
            position: relative;
            background: linear-gradient(35deg, #4b2b20 0%, #8b4513 100%) !important;
            isolation: isolate;
            overflow: hidden;
            color: #FAF9F6 !important;
            padding: 50px 0px 0px;
        }

        html body #related-services .hf-related-scroll-container {
            position: relative;
            margin-top: 15px;
        }

        html body #related-services .hf-related-track {
            display: flex;
            gap: 22px;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scroll-behavior: smooth;
            -webkit-overflow-scrolling: touch;
            padding: 12px 4px 16px 4px;
            scrollbar-width: none !important;
            -ms-overflow-style: none !important;
            cursor: grab;
            user-select: none;
            -webkit-user-select: none;
        }

        html body #related-services .hf-related-track::-webkit-scrollbar {
            display: none !important;
            height: 0 !important;
            width: 0 !important;
        }

        html body #related-services .hf-related-track.is-dragging {
            cursor: grabbing !important;
            scroll-snap-type: none !important;
            scroll-behavior: auto !important;
            user-select: none !important;
            -webkit-user-select: none !important;
        }

        html body #related-services .hf-related-track.is-dragging .hf-related-card {
            cursor: grabbing !important;
            pointer-events: none;
        }

        html body #related-services .hf-related-card {
            flex: 0 0 310px;
            max-width: 310px;
            scroll-snap-align: start;
            background: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid rgba(232, 201, 154, 0.35) !important;
            border-radius: 20px;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            padding: 26px 22px 24px 22px;
            display: flex;
            flex-direction: column;
            box-shadow: none !important;
            transition: transform 0.35s cubic-bezier(0.25, 1, 0.5, 1), background 0.3s ease, border-color 0.3s ease;
            text-decoration: none !important;
            user-select: none !important;
            -webkit-user-select: none !important;
            -webkit-user-drag: none !important;
            cursor: grab;
        }

        html body #related-services .hf-related-card:hover {
            transform: translateY(-6px);
            background: rgba(255, 255, 255, 0.14) !important;
            border-color: #E8C99A !important;
            box-shadow: none !important;
        }

        html body #related-services .hf-related-card__title,
        html body #related-services .hf-related-card h3 {
            font-family: var(--serif, 'Playfair Display', Georgia, serif) !important;
            font-style: italic !important;
            font-size: 1.1rem !important;
            font-weight: 500 !important;
            color: #FAF9F6 !important;
            -webkit-text-fill-color: #FAF9F6 !important;
            margin-bottom: 0 !important;
            line-height: 1.25 !important;
            display: flex;
            align-items: flex-start;
            transition: color 0.25s ease;
        }

        html body #related-services .hf-related-card:hover .hf-related-card__title {
            color: #F8E2C8 !important;
            -webkit-text-fill-color: #F8E2C8 !important;
        }

        html body #related-services .hf-related-card__divider {
            width: 100%;
            height: 1px;
            background: rgba(232, 201, 154, 0.4) !important;
            margin: 14px 0 16px 0;
        }

        html body #related-services .hf-related-card__desc,
        html body #related-services .hf-related-card p,
        html body #related-services a.hf-related-card p {
            font-family: var(--sans, 'Inter', system-ui, sans-serif) !important;
            font-size: 0.93rem !important;
            line-height: 1.7 !important;
            color: #FAF9F6 !important;
            -webkit-text-fill-color: #FAF9F6 !important;
            opacity: 0.92 !important;
            margin-bottom: 20px !important;
            min-height: 4.8em;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
            flex-grow: 1;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }

        html body #related-services .hf-related-card__action,
        html body #related-services .hf-related-card span.hf-related-card__action {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #FAF9F6 !important;
            -webkit-text-fill-color: #FAF9F6 !important;
            letter-spacing: 0.02em;
            transition: gap 0.25s ease, color 0.25s ease;
        }

        html body #related-services .hf-related-card:hover .hf-related-card__action {
            gap: 10px;
            color: #FAF9F6 !important;
            -webkit-text-fill-color: #FAF9F6 !important;
        }

        html body #related-services .hf-related-card__action svg {
            stroke: #FAF9F6 !important;
            transition: stroke 0.25s ease;
        }

        @media (max-width: 767px) {
            html body #related-services .hf-related-track {
                gap: 16px;
                padding-left: 16px;
                padding-right: 16px;
                padding-bottom: 8px;
                margin-left: -12px;
                margin-right: -12px;
                scrollbar-width: none;
                -ms-overflow-style: none;
            }

            html body #related-services .hf-related-track::-webkit-scrollbar {
                display: none !important;
                height: 0 !important;
                width: 0 !important;
            }

            html body #related-services .hf-related-card {
                flex: 0 0 270px;
                max-width: 270px;
                padding: 22px 18px;
            }

            html body #related-services .hf-related-card__title {
                font-size: 1.22rem !important;
            }

            html body #related-services .hf-related-card__desc {
                font-size: 0.88rem !important;
            }
        }"""

assert old_css in content, "old_css not found"
content = content.replace(old_css, new_css, 1)

# 2. Update the HTML track element: remove bx-related-track class
old_track = '<div class="hf-related-track bx-related-track" id="relatedTrack">'
new_track = '<div class="hf-related-track" id="relatedTrack">'
assert old_track in content, "old_track not found"
content = content.replace(old_track, new_track, 1)

# 3. Add the JavaScript for grabbing, dragging, and horizontal scrolling before </body>
script_to_add = """    <script>
        // Related Concerns Desktop Grab & Scroll + Mouse Wheel (like laser-hair-removal.html)
        (function () {
            var track = document.getElementById('relatedTrack') || document.querySelector('#related-services .hf-related-track');
            if (!track) return;

            var isDown = false;
            var startX = 0;
            var scrollLeft = 0;
            var hasDragged = false;

            // Stop native HTML5 image/link drag ghost
            track.addEventListener('dragstart', function (e) {
                e.preventDefault();
            });

            track.addEventListener('mousedown', function (e) {
                if (e.button !== 0) return; // Only primary button
                isDown = true;
                hasDragged = false;
                startX = e.pageX - track.offsetLeft;
                scrollLeft = track.scrollLeft;
                track.classList.add('is-dragging');
            });

            window.addEventListener('mousemove', function (e) {
                if (!isDown) return;
                var x = e.pageX - track.offsetLeft;
                var walk = (x - startX);
                if (Math.abs(walk) > 5) {
                    hasDragged = true;
                }
                track.scrollLeft = scrollLeft - walk;
            });

            window.addEventListener('mouseup', function () {
                if (isDown) {
                    isDown = false;
                    track.classList.remove('is-dragging');
                }
            });

            // Suppress link navigation if dragged
            track.addEventListener('click', function (e) {
                if (hasDragged) {
                    e.preventDefault();
                    e.stopPropagation();
                    hasDragged = false;
                }
            }, true);

            // Desktop mouse wheel horizontal navigation on track
            track.addEventListener('wheel', function (e) {
                if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
                    var maxScroll = track.scrollWidth - track.clientWidth;
                    var canScrollLeft = track.scrollLeft > 0 && e.deltaY < 0;
                    var canScrollRight = track.scrollLeft < maxScroll && e.deltaY > 0;
                    if (canScrollLeft || canScrollRight) {
                        e.preventDefault();
                        track.scrollLeft += e.deltaY * 1.1;
                    }
                }
            }, { passive: false });
        })();
    </script>
</body>"""

assert '</body>' in content, "</body> not found"
content = content.replace('</body>', script_to_add, 1)

with open('under-eye-darkness.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied horizontal slide implementation to Related Concerns successfully!")
