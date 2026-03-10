import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The old logo HTML:
# <a href="/" class="logo"><img src="/images/logo.png" width="40" height="40" style="background:white; border-radius:50%; padding: 2px;"> Topline Plumbing</a>
# The new logo HTML:
# <a href="/" class="logo"><img src="/images/logo-wide.png" alt="Topline Plumbing" style="height: 40px; width: auto; background: white; padding: 4px; border-radius: 4px;"></a>

pattern = re.compile(r'<a href="/" class="logo">\s*<img[^>]+>\s*Topline Plumbing\s*</a>', re.IGNORECASE)

replacement = '<a href="/" class="logo"><img src="/images/logo-wide.png" alt="Topline Plumbing Logo" style="height: 40px; width: auto; background: white; padding: 4px; border-radius: 4px;"></a>'

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        with open(f, 'w') as file:
            file.write(new_content)

print("Updated logo HTML.")
