import re

with open('water-heater-repair.html', 'r') as file:
    content = file.read()
    
injection = """
    <!-- Stats Section -->
    <section class="section">
      <div class="container text-center">
        <h2 style="margin-bottom: 2rem; color: var(--primary-navy);">Regular Water Heater Service Will Save You Time & Money</h2>
        <div class="grid grid-3">
          <div class="card" style="border-top: 4px solid var(--accent-orange);">
            <div style="font-size: 3rem; font-weight: 800; color: var(--accent-orange); margin-bottom: 1rem;">15%</div>
            <p style="font-size: 1.1rem; opacity: 0.9;">Routine service can improve your water heater's efficiency by up to 15%, helping it run better and last longer.</p>
          </div>
          <div class="card" style="border-top: 4px solid var(--accent-orange);">
            <div style="font-size: 3rem; font-weight: 800; color: var(--accent-orange); margin-bottom: 1rem;">1,500gal</div>
            <p style="font-size: 1.1rem; opacity: 0.9;">A well-maintained system can save up to 1,500 gallons of water per year, reducing waste and lowering utility costs.</p>
          </div>
          <div class="card" style="border-top: 4px solid var(--accent-orange);">
            <div style="font-size: 3rem; font-weight: 800; color: var(--accent-orange); margin-bottom: 1rem;">$200</div>
            <p style="font-size: 1.1rem; opacity: 0.9;">Homeowners can save up to $200 per year on energy bills with regular water heater maintenance.</p>
          </div>
        </div>
      </div>
    </section>
"""

# Insert right after the hero section
pattern = re.compile(r'(</section>\s*<!-- Content -->)', re.DOTALL)
new_content = pattern.sub(f"</section>\n{injection}\n    <!-- Content -->", content)

with open('water-heater-repair.html', 'w') as file:
    file.write(new_content)
    
print("Updated water-heater-repair.html")
