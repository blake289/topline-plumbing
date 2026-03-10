import glob
import re
import os

new_fonts = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Georama:wght@500;600;700;800&family=Inter:wght@400;600;700&family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
"""

new_header = """  <!-- Desktop Nav -->
  <header class="navbar">
    <div class="container nav-container">
      <a href="/" class="logo">
        <img class="nav-logo" src="/images/logo-white.png" alt="Topline Plumbing Logo" style="max-height: 50px;" />
      </a>
      <nav class="nav-links">
        <a href="/index.html#services">Services</a>
        <a href="/about.html">About</a>
        <a href="/contact.html">Contact Us</a>
      </nav>
      <!-- Ref site has a red button on the far right of nav -->
      <a href="tel:5307689446" class="btn btn-primary" style="padding: 12px 24px; border-radius: 30px; display: none; margin-left: auto;">
        <span style="margin-right: 8px;">📞</span> (530) 768-9446
      </a>
      <button class="mobile-menu-btn" aria-label="Open Menu">☰</button>
    </div>
  </header>
  <style>
    .navbar { background-color: #041E38 !important; }
    .nav-links a { color: rgba(255, 255, 255, 0.9) !important; letter-spacing: 0.5px; }
    .nav-links a:hover { color: #fff !important; }
    .mobile-menu-btn { color: #fff !important; }
    @media (min-width: 1024px) {
      .navbar .btn-primary { display: inline-flex !important; }
    }
  </style>

  <!-- Mobile Drawer & Backdrop -->
  <div class="backdrop"></div>
  <div class="mobile-drawer">
    <button class="drawer-close" aria-label="Close Menu">✕</button>
    <div style="margin-top: 40px;">
      <a href="/index.html#services">Services</a>
      <a href="/about.html">About</a>
      <a href="/contact.html">Contact Us</a>
      <a href="tel:5307689446" class="btn btn-primary" style="margin-top: 24px; width: 100%;">Call (530) 768-9446</a>
    </div>
  </div>"""

new_footer = """  <!-- Global Footer -->
  <footer class="site-footer">
    <div class="container grid grid-4 animate-on-scroll">

      <!-- Col 1 -->
      <div>
        <img src="/images/logo.png" alt="Topline Plumbing"
          style="width: 160px; margin-bottom: 16px; background:white; border-radius:4px; padding:4px;" />
        <p style="font-size: 16px; color: var(--color-gray-300); margin-bottom: 24px;">Auburn & Grass Valley's most
          trusted plumber since 1998.</p>
        <div class="social-icons">
          <a href="https://www.facebook.com/profile.php?id=61551944100731" class="social-icon flex items-center justify-center" target="_blank"
            aria-label="Facebook">
            <svg style="width: 20px; height: 20px;" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          </a>
          <a href="https://www.instagram.com/toplinewatersolutions/" class="social-icon flex items-center justify-center" target="_blank"
            aria-label="Instagram">
            <svg style="width: 20px; height: 20px;" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
          </a>
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
        <a href="tel:5307689446" style="font-size: 18px; font-weight: 600; color: var(--color-white);">(530)
          768-9446</a>
        <a href="mailto:Toplineplumbingredding@gmail.com">Toplineplumbingredding@gmail.com</a>
        <p>Serving Redding & surrounding areas</p>
      </div>

    </div>

    <div class="container footer-bottom text-center flex-col">
      <p>&copy; Copyright 2026. Topline Plumbing. All rights reserved.</p>
      <p><a href="/contact.html" style="display:inline; margin-left: 10px;">Privacy Policy</a> | <a href="/contact.html"
          style="display:inline; margin-left: 10px;">Terms of Service</a></p>
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
