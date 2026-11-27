import glob

print("--- Treatment images in images/ ---")
for f in glob.glob('images/**/*.webp', recursive=True):
    print(f)

with open('sagging-skin.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="treatments"')
print("\nid='treatments' index:", idx)
if idx != -1:
    end = c.find('</section>', idx) + 10
    print(c[idx-50:end][:2000])
