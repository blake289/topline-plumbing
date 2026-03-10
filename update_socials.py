import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use the existing generic footer string and add the social links and the new copyright tag.
for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. First, make sure the copyright string is there (or update it if it is the old short one)
    if 'Copyright 2026. Topline Plumbing.' not in content:
        # Check if the older copyright string is present, or the short footer string
        if '&copy; Copyright 2026. Topline Plumbing. All rights reserved. | 530-768-9446 | Redding, CA' in content:
            # We already updated it in the last step, so we will append the socials above it.
            pass
        elif '<div class="container footer-bottom"><p>Topline Plumbing | 530-768-9446 | Redding, CA</p></div>' in content:
            content = content.replace(
                '<div class="container footer-bottom"><p>Topline Plumbing | 530-768-9446 | Redding, CA</p></div>',
                '<div class="container footer-bottom"><p>&copy; Copyright 2026. Topline Plumbing. All rights reserved. | 530-768-9446 | Redding, CA</p></div>'
            )

    # 2. Find the footer injection point and insert the social links ABOVE the copyright line.
    # The existing footer contains `<div class="container footer-bottom">`
    social_html = '''
      <div class="container text-center" style="margin-bottom: 2rem;">
        <a href="https://www.facebook.com/profile.php?id=61551944100731" target="_blank" style="margin: 0 10px; font-size: 1.25rem;">Facebook</a>
        <a href="https://www.instagram.com/toplinewatersolutions/" target="_blank" style="margin: 0 10px; font-size: 1.25rem;">Instagram</a>
      </div>
      <div class="container footer-bottom">'''
      
    if social_html not in content:
        content = content.replace('<div class="container footer-bottom">', social_html)
        
        with open(f, 'w') as file:
            file.write(content)

print("Updated footers with social links.")
