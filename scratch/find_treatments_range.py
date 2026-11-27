with open('sagging-skin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_line = None
end_line = None
for i, l in enumerate(lines):
    if '<section id="treatments"' in l:
        start_line = i + 1
    if start_line and '</section>' in l:
        end_line = i + 1
        break

print(f"Start: {start_line}, End: {end_line}")
print("".join(lines[start_line-1:start_line+25]))
print("...")
print("".join(lines[end_line-15:end_line]))
