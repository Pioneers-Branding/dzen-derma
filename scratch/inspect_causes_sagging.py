with open('sagging-skin.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="causes"')
print('id="causes" index:', idx)
if idx != -1:
    end = c.find('</section>', idx) + 10
    print(c[idx-50:end])

# Also list available images in images/home and images/botox etc that could suit sagging/laxity
import glob
print("\n--- Available relevant images ---")
for p in glob.glob('images/**/*.webp', recursive=True):
    lp = p.lower()
    if any(k in lp for k in ['lax', 'sag', 'jaw', 'neck', 'arm', 'volume', 'aging', 'ageing', 'fine', 'dull']):
        print(p)
