import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    if 'Copyright 2026' not in content:
        content = content.replace(
            '<div class="container footer-bottom"><p>Topline Plumbing | 530-768-9446 | Redding, CA</p></div>',
            '<div class="container footer-bottom"><p>&copy; Copyright 2026. Topline Plumbing. All rights reserved. | 530-768-9446 | Redding, CA</p></div>'
        )
        
        with open(f, 'w') as file:
            file.write(content)

print("Updated footers")
