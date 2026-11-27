import glob, re

for fname in glob.glob('*.html'):
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'SCIENCE & SERENITY' in c or 'ENHANCEMENT & RESTRAINT' in c:
        print(f"Found in {fname}")
