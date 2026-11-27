import glob

for fname in glob.glob('*.html'):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'Serenity' in c or 'serenity' in c or 'why-dzen' in c:
        print(f"Found serenity or why-dzen in {fname}")
