import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use the generic /#services link on index.html, but use /index.html#services on other pages,
# BUT we'll provide a dropdown with actual links to the pages for better SEO routing.
new_nav = '''<nav class="nav-links">
          <div class="dropdown">
            <a href="/#services" class="dropbtn" id="services-link">Services ▼</a>
            <div class="dropdown-content">
              <a href="/water-heater-repair.html">Water Heater Repair</a>
              <a href="/tankless.html">Tankless Installation</a>
              <a href="/drain-cleaning.html">Drain Cleaning</a>
              <a href="/emergency.html">24/7 Emergency</a>
            </div>
          </div>
          <div class="dropdown">
            <a href="#" class="dropbtn">Service Areas ▼</a>
            <div class="dropdown-content">
              <a href="/shasta-lake.html">Shasta Lake</a>
              <a href="/anderson.html">Anderson</a>
              <a href="/palo-cedro.html">Palo Cedro</a>
              <a href="/bella-vista.html">Bella Vista</a>
            </div>
          </div>
          <a href="/about.html">About</a>
          <a href="/contact.html">Contact</a>
        </nav>'''

pattern = re.compile(r'<nav class="nav-links">.*?</nav>', re.DOTALL)

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    is_index = (f == 'index.html')
    
    if is_index:
        nav_replacement = new_nav.replace('href="/#services"', 'href="#services"')
    else:
        nav_replacement = new_nav

    new_content = pattern.sub(nav_replacement, content)
    
    with open(f, 'w') as file:
        file.write(new_content)
        
print("Updated all HTML files with Services dropdown.")
