with open('botox.html', 'r', encoding='utf-8') as f:
    b = f.read()

idx = b.find('id="why-dzen"')
end_idx = b.find('</section>', idx)
print(b[idx:end_idx+10])
