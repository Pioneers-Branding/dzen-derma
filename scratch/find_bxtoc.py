with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'bxToc' in line:
            print(f"Line {i+1}: {line.strip()}")
