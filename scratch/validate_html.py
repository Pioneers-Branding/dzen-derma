from html.parser import HTMLParser

class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last, pos = self.stack.pop()
        if last != tag:
            # check if tag is in stack
            found = any(t == tag for t, p in self.stack)
            if found:
                self.errors.append(f"Mismatched closing tag </{tag}> at line {self.getpos()[0]}, expected </{last}> from line {pos[0]}")
            else:
                self.errors.append(f"Extraneous closing tag </{tag}> at line {self.getpos()[0]}")

with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    html = f.read()

v = Validator()
v.feed(html)
print(f"Validation finished. Unclosed tags: {len(v.stack)}, Tag mismatches: {len(v.errors)}")
if v.errors:
    print("Top errors:")
    for e in v.errors[:10]:
        print(" ", e)
if v.stack:
    print("Unclosed tags:", [f"{t} (L{p[0]})" for t, p in v.stack[:10]])
