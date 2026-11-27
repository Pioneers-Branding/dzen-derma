import json, re

with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Meta Tags
old_meta = """    <title>Pigmentation: Types &amp; Treatment — D'Zen Derma</title>
    <link rel="icon" type="image/png" href="logo-header.png" />
    <link rel="apple-touch-icon" href="logo-header.png" />
    <meta name="description"
        content="Understand pigmentation at D'Zen Derma: melasma, sun spots, freckles, post-acne marks and PIH, and doctor-led options such as peels, pigment lasers, skin boosters and medi-facials." />
    <link rel="canonical" href="https://dzenderma.com/pigmentation" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <meta name="author" content="Dr. Aarushi Passi Bhandari" />

    <!-- Open Graph -->
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="D'Zen Derma" />
    <meta property="og:locale" content="en_IN" />
    <meta property="og:url" content="https://dzenderma.com/pigmentation" />
    <meta property="og:title" content="Pigmentation: Types &amp; Treatment | D'Zen Derma" />
    <meta property="og:description"
        content="More even-looking skin. Balanced tone. Renewed confidence. Doctor-led pigmentation care, personalised to your skin." />"""

new_meta = """    <title>Under-Eye Darkness &amp; Hollowness: Types &amp; Treatment — D'Zen Derma</title>
    <link rel="icon" type="image/png" href="logo-header.png" />
    <link rel="apple-touch-icon" href="logo-header.png" />
    <meta name="description"
        content="Understand under-eye darkness and hollowness at D'Zen Derma: tear trough hollowness, volume loss, wrinkles and dark circles, with doctor-led treatments tailored to your facial anatomy." />
    <link rel="canonical" href="https://dzenderma.com/under-eye-darkness" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <meta name="author" content="Dr. Aarushi Passi Bhandari" />

    <!-- Open Graph -->
    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="D'Zen Derma" />
    <meta property="og:locale" content="en_IN" />
    <meta property="og:url" content="https://dzenderma.com/under-eye-darkness" />
    <meta property="og:title" content="Under-Eye Darkness &amp; Hollowness: Types &amp; Treatment | D'Zen Derma" />
    <meta property="og:description"
        content="Rested-looking eyes. Softer contours. Renewed confidence. Doctor-led under-eye care, personalised to your facial anatomy." />"""

assert old_meta in content, "old_meta not found"
content = content.replace(old_meta, new_meta, 1)

# 2. Update Breadcrumb Schema
old_bc = """"name": "Pigmentation", "item": "https://dzenderma.com/pigmentation\""""
new_bc = """"name": "Under-Eye Darkness", "item": "https://dzenderma.com/under-eye-darkness\""""
assert old_bc in content, "old_bc not found"
content = content.replace(old_bc, new_bc, 1)

# 3. Update FAQ Schema
old_faq_schema_pattern = r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "FAQPage",.*?</script>'

new_faq_schema = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What causes under-eye hollowness?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Under-eye hollowness can be caused by genetics, facial anatomy, age-related volume loss, changes in fat distribution, and thinning of the skin beneath the eyes."
      }
    },
    {
      "@type": "Question",
      "name": "Why do my eyes look sunken or tired even when I sleep well?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The appearance of tired eyes may be related to natural under-eye anatomy, volume distribution, shadows, pigmentation, or skin thinning rather than lack of sleep."
      }
    },
    {
      "@type": "Question",
      "name": "Is under-eye hollowness the same as dark circles?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Hollowness refers to a depression or loss of volume beneath the eyes, while dark circles refer to darker colouring in the under-eye area. However, hollowness can create shadows that make dark circles appear more prominent."
      }
    },
    {
      "@type": "Question",
      "name": "Can under-eye hollowness be improved?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Depending on its cause, the appearance of under-eye hollowness may be improved with selected procedures that address volume, skin quality, or associated concerns. Suitability depends on individual anatomy and assessment."
      }
    },
    {
      "@type": "Question",
      "name": "Is under-eye hollowness caused by ageing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ageing can contribute to under-eye hollowness through changes in facial fat, skin elasticity, and underlying support. However, it can also be present in younger individuals due to genetics and natural facial structure."
      }
    },
    {
      "@type": "Question",
      "name": "Can under-eye hollowness occur at a young age?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Some people naturally have deeper tear troughs or less volume beneath the eyes due to their facial anatomy and genetics."
      }
    },
    {
      "@type": "Question",
      "name": "How many sessions are required to improve under-eye hollowness?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The number of sessions depends on the selected procedure, degree of hollowness, skin quality, and individual goals. Some options may involve one session, while others may require multiple sessions."
      }
    },
    {
      "@type": "Question",
      "name": "Are procedures for under-eye hollowness safe?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The under-eye area is delicate and contains important blood vessels and structures. All procedures require careful assessment and an experienced medical professional. Each procedure has its own risks, and suitability should be determined during consultation."
      }
    },
    {
      "@type": "Question",
      "name": "Does under-eye hollowness cause dark circles?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hollowness can create shadows beneath the eyes, making the area appear darker. Pigmentation, visible blood vessels, and skin thinning can also contribute to dark circles."
      }
    },
    {
      "@type": "Question",
      "name": "Can under-eye hollowness return after improvement?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Natural ageing and changes in facial volume continue over time. The longevity of improvement depends on the procedure, individual anatomy, and natural ageing process."
      }
    }
  ]
}
    </script>"""

content, count = re.subn(old_faq_schema_pattern, new_faq_schema, content, count=1, flags=re.DOTALL)
assert count == 1, "FAQ schema replacement failed"

# 4. Hero header <h1>
old_h1 = """                <h1 class="page-title mb-3 hf-hero-title">
                    Pigmentation
                </h1>"""
new_h1 = """                <h1 class="page-title mb-3 hf-hero-title">
                    Under-Eye Darkness
                </h1>"""
assert old_h1 in content, "old_h1 not found"
content = content.replace(old_h1, new_h1, 1)

# Save progress
with open('under-eye-darkness.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Part 1: Meta, Schemas, Hero h1 updated successfully.")
