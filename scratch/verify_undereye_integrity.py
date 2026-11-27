import re

with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Check title and meta
print("Title:", re.search(r'<title>(.*?)</title>', c).group(1))
print("Hero Title:", re.search(r'<h1 class="page-title[^"]*">(.*?)</h1>', c, re.DOTALL).group(1).strip())

# 2. Check sections
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', c)
print("\nSections found in order:")
for s in sections:
    print(f"  - #{s}")

# 3. Check recommended treatments anchors vs treatment cards
rec_anchors = re.findall(r'<a href="#(t-[^"]+)"', c)
print(f"\nRecommended treatments links found ({len(rec_anchors)}):", rec_anchors)

treatment_card_ids = re.findall(r'<article class="dz-treatment-card" id="([^"]+)"', c)
print(f"Treatment card IDs found ({len(treatment_card_ids)}):", treatment_card_ids)

missing_cards = set(rec_anchors) - set(treatment_card_ids)
if missing_cards:
    print("WARNING: Missing card IDs for links:", missing_cards)
else:
    print("All recommended treatment links match treatment card IDs!")

# 4. Check TOC links
toc_targets = re.findall(r'data-target="([^"]+)"', c)
print(f"\nTOC targets ({len(toc_targets)}):", toc_targets)
missing_sections = [t for t in toc_targets if f'id="{t}"' not in c]
if missing_sections:
    print("WARNING: Missing sections for TOC:", missing_sections)
else:
    print("All TOC targets match section IDs!")

# 5. Check FAQs count
faqs = re.findall(r'<details class="hf-faq-item"', c)
print(f"\nTotal FAQ items in page: {len(faqs)}")

# 6. Check for unreplaced 'pigmentation' keywords in user-facing content (outside file paths / generic styles)
body_start = c.find('<main>')
body_end = c.find('</main>')
body = c[body_start:body_end]

# Check headers and titles
bad_headers = re.findall(r'<h[1-4][^>]*>[^<]*pigmentation[^<]*</h[1-4]>', body, re.IGNORECASE)
print("\nAny bad headers containing pigmentation in body?:", bad_headers)

print("\nIntegrity check complete!")
