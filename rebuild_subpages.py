import glob
import re
import os

new_fonts = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">
"""

new_header = """    <!-- Desktop Nav -->
    <header class="navbar">
      <div class="container nav-container">
        <a href="/" class="logo">
          <img class="nav-logo" src="/images/logo-wide.png" alt="Topline Plumbing Logo" />
        </a>
        <nav class="nav-links">
          <a href="/index.html#services">Services</a>
          <a href="/about.html">About</a>
          <a href="/contact.html">Contact</a>
          <a href="tel:5307689446" class="btn nav-cta" style="color: white !important;">Book Free Inspection</a>
        </nav>
        <button class="mobile-menu-btn" aria-label="Open Menu">☰</button>
      </div>
    </header>

    <!-- Mobile Drawer & Backdrop -->
    <div class="backdrop"></div>
    <div class="mobile-drawer">
      <button class="drawer-close" aria-label="Close Menu">✕</button>
      <div style="margin-top: 40px;">
        <a href="/index.html#services">Services</a>
        <a href="/about.html">About</a>
        <a href="/contact.html">Contact</a>
        <a href="tel:5307689446" class="btn nav-cta" style="margin-top: 24px;">Book Free Inspection</a>
      </div>
    </div>"""

new_footer = """    <!-- Global Footer -->
    <footer class="site-footer">
      <div class="container grid grid-4 animate-on-scroll">
        <!-- Col 1 -->
        <div>
          <img src="/images/logo-wide.png" alt="Topline Plumbing" style="width: 160px; margin-bottom: 16px; background:white; border-radius:4px; padding:4px;" />
          <p style="font-size: 16px; color: var(--color-gray-300); margin-bottom: 24px;">Auburn & Grass Valley's most trusted plumber since 1998.</p>
          <div class="social-icons">
            <a href="https://www.facebook.com/profile.php?id=61551944100731" class="social-icon" target="_blank" aria-label="Facebook">f</a>
            <a href="https://www.instagram.com/toplinewatersolutions/" class="social-icon" target="_blank" aria-label="Instagram">ig</a>
          </div>
        </div>

        <!-- Col 2 -->
        <div>
          <h4>Services</h4>
          <a href="/water-heater-repair.html">Water Heater Repair</a>
          <a href="/tankless.html">Tankless Installation</a>
          <a href="/emergency.html">Emergency Plumbing</a>
          <a href="/drain-cleaning.html">Drain Cleaning</a>
        </div>

        <!-- Col 3 -->
        <div>
          <h4>Service Areas</h4>
          <a href="/shasta-lake.html">Shasta Lake, CA</a>
          <a href="/anderson.html">Anderson, CA</a>
          <a href="/palo-cedro.html">Palo Cedro, CA</a>
          <a href="/bella-vista.html">Bella Vista, CA</a>
        </div>

        <!-- Col 4 -->
        <div>
          <h4>Contact Us</h4>
          <a href="tel:5307689446" style="font-size: 18px; font-weight: 600; color: var(--color-white);">(530) 768-9446</a>
          <a href="mailto:Toplineplumbingredding@gmail.com">Toplineplumbingredding@gmail.com</a>
          <p>Serving Redding & surrounding areas</p>
        </div>
      </div>
      
      <div class="container footer-bottom flex-col" style="text-align: center;">
        <p>&copy; Copyright 2026. Topline Plumbing. All rights reserved.</p>
        <p><a href="/contact.html" style="display:inline; margin-left: 10px;">Privacy Policy</a> | <a href="/contact.html" style="display:inline; margin-left: 10px;">Terms of Service</a></p>
      </div>
    </footer>
"""

header_pattern = re.compile(r'<header class="site-header">.*?</header>', re.DOTALL)
footer_pattern = re.compile(r'<footer class="site-footer">.*?</footer>', re.DOTALL)

for file in glob.glob('*.html'):
    if file == 'index.html': continue
    with open(file, 'r') as f:
        content = f.read()

    # Apply Header Replacement
    content = header_pattern.sub(new_header, content)
    
    # Apply Footer Replacement
    content = footer_pattern.sub(new_footer, content)

    # Inject Fonts and styling padding fix for subpages right below header
    if '<link rel="preconnect" href="https://fonts.googleapis.com">' not in content:
        content = content.replace('<head>', '<head>\n' + new_fonts)
        
    # Adding padding under fixed header so content doesn't get covered
    content = content.replace('<section class="hero"', '<section class="hero-section" style="padding-top: 100px;"')
    
    # Ensuring JS is still correctly loaded right before closing body
    if 'src="/main.js"' not in content:
        content = content.replace('</body>', '    <script type="module" src="/main.js"></script>\n  </body>')

    with open(file, 'w') as f:
        f.write(content)
        
print("Updated subpages successfully!")
