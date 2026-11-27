with open('botox.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
m = re.search(r'(<section[^>]*id=["\'](?:why-dzen|approach)[^>]*>.*?</section>)', c, re.DOTALL)
if m:
    print(m.group(1)[:1000])
else:
    print("Not found by regex, searching why-dzen:")
    idx = c.find('why-dzen')
    if idx != -1:
        print(c[idx-50:idx+800])
