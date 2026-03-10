import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

new_nav = '''<nav class="nav-links">
          <a href="/#services">Services</a>
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
        
print("Updated all HTML files.")
