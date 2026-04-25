import os
import re

css_additions = """
/* --- Additional Responsiveness --- */
.responsive-grid { display: grid; gap: 16px; }
.grid-2 { grid-template-columns: 1fr 1fr; }
.grid-1-2 { grid-template-columns: 1fr 2fr; }
.grid-auto { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
.grid-4 { grid-template-columns: 1fr 1fr 1fr auto; }

.table-wrapper {
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

@media (max-width: 768px) {
  .grid-2, .grid-1-2, .grid-4 { grid-template-columns: 1fr !important; }
  .stat-card { min-width: 100%; margin-bottom: 16px; }
  .topbar { padding: 12px 16px; flex-wrap: wrap; }
  .login-card { padding: 24px; margin: 16px; width: calc(100% - 32px); }
  .modal { width: 95%; max-height: 95vh; margin: 10px; }
  .sidebar { z-index: 100; transition: transform 0.3s ease; }
  .search-bar { width: 100% !important; margin-bottom: 16px; }
  .main-content { padding-top: 10px; }
  
  /* Make header flexboxes stack if needed */
  .mobile-flex-col { flex-direction: column !important; align-items: stretch !important; gap: 16px; }
  .mobile-flex-col > * { width: 100%; }
}

/* Sidebar Overlay */
.sidebar-overlay {
    display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 90;
}
@media (max-width: 768px) {
    .sidebar.mobile-open ~ .sidebar-overlay { display: block; }
}
"""

with open('public/css/custom.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_additions + '\n')

js_sidebar_func = """
    function toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        const main = document.getElementById('mainContent');
        if(window.innerWidth <= 768) {
            sidebar.classList.toggle('mobile-open');
        } else {
            sidebar.classList.toggle('collapsed');
            if(main) main.classList.toggle('expanded');
        }
    }
"""

html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace inline grids
    content = content.replace('style="display:grid;grid-template-columns:1fr 1fr;gap:16px;"', 'class="responsive-grid grid-2"')
    content = content.replace('style="display:grid;grid-template-columns:1fr 2fr;gap:24px;" id="dashboardPanels"', 'class="responsive-grid grid-1-2" style="gap:24px;" id="dashboardPanels"')
    content = content.replace('style="display:grid;grid-template-columns:1fr 2fr;gap:24px;"', 'class="responsive-grid grid-1-2" style="gap:24px;"')
    content = content.replace('style="display:grid;grid-template-columns:1fr 1fr 1fr auto;gap:16px;align-items:end;"', 'class="responsive-grid grid-4" style="align-items:end;"')
    content = content.replace('style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;"', 'class="mobile-flex-col" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;"')

    # Add table wrapper for horizontal scroll
    content = re.sub(r'(<table class="data-table">)', r'<div class="table-wrapper">\n\1', content)
    content = re.sub(r'(</table>)', r'\1\n</div>', content)

    # Update hamburger button onclick
    content = re.sub(r'onclick="document\.getElementById\(\'sidebar\'\)\.classList\.toggle\(\'collapsed\'\);.*?"', 'onclick="toggleSidebar()"', content)

    # Add the JS function if not present
    if 'function toggleSidebar()' not in content and '</body>' in content:
        if 'function initTheme()' in content:
            content = content.replace('function initTheme()', js_sidebar_func + '\n    function initTheme()')
        else:
            content = content.replace('</body>', '<script>' + js_sidebar_func + '</script>\n</body>')

    # Add overlay div right after sidebar
    if '</aside>' in content and '<div class="sidebar-overlay"' not in content:
        content = content.replace('</aside>', '</aside>\n<!-- Overlay for mobile sidebar -->\n<div class="sidebar-overlay" onclick="toggleSidebar()"></div>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Responsiveness added successfully.')
