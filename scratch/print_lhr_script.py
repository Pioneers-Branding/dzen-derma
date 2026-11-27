with open('laser-hair-removal.html', 'r', encoding='utf-8') as f:
    lhr = f.read()

pos = 178059
start = lhr.rfind('<script', 0, pos)
end = lhr.find('</script>', pos) + 9
print(lhr[start:end])
