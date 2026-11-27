with open('concerns.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
cards = re.findall(r'<div class="col-lg-4 col-md-6 mb-4">.*?</div>\s*</div>\s*</div>', c, re.DOTALL)
for card in cards:
    if 'sag' in card.lower() or 'lax' in card.lower():
        print(card)
        print("="*40)
