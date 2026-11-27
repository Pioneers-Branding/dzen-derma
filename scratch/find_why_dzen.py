with open('pigmentation.html', 'r', encoding='utf-8') as f:
    p = f.read()

import re
matches = re.findall(r'(Why D’Zen[^\n<]+|<h[1-4][^>]*>[^<]*Why[^<]*</h[1-4]>)', p, re.IGNORECASE)
print('Matches for Why D’Zen in pigmentation.html:', matches)

matches2 = re.findall(r'(SCIENCE & SERENITY|INNER & OUTER|ENHANCEMENT & RESTRAINT)', p, re.IGNORECASE)
print('Matches for pillars in pigmentation.html:', matches2)
