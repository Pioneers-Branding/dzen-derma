with open('laser-hair-removal.html', 'r', encoding='utf-8') as f:
    lhr = f.read()

start_marker = "/* ── Related Services Section (Why D'Zen Philosophy Style & Horizontal Scroll) ── */"
idx = lhr.find(start_marker)
if idx != -1:
    end_idx = lhr.find("/* ──", idx + len(start_marker))
    print(lhr[idx:end_idx])
else:
    print("start marker not found")
