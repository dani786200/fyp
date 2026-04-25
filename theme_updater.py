import os
import re

css_vars = """
:root {
  --bg-main: #0B0F19;
  --bg-card: #111116;
  --bg-modal: #1E293B;
  --text-primary: #F1F5F9;
  --text-secondary: #94A3B8;
  --text-muted: #64748B;
  --border-color: #1E1E24;
  --border-light: #334155;
  --table-header: rgba(0,0,0,0.2);
  --input-bg: rgba(15, 23, 42, 0.6);
}

body.light-mode {
  --bg-main: #F8FAFC;
  --bg-card: #FFFFFF;
  --bg-modal: #FFFFFF;
  --text-primary: #0F172A;
  --text-secondary: #475569;
  --text-muted: #64748B;
  --border-color: #E2E8F0;
  --border-light: #CBD5E1;
  --table-header: #F1F5F9;
  --input-bg: #FFFFFF;
}

body {
  background-color: var(--bg-main) !important;
  color: var(--text-primary) !important;
  transition: background-color 0.3s, color 0.3s;
}

.sidebar, .chart-container, .report-card, .login-card, .modal {
  background-color: var(--bg-card) !important;
  border-color: var(--border-color) !important;
}

.data-table thead {
  background-color: var(--table-header) !important;
}

.form-input {
  background-color: var(--input-bg) !important;
  color: var(--text-primary) !important;
  border-color: var(--border-light) !important;
}

h1, h2, h3, .stat-value { color: var(--text-primary) !important; }
p { color: var(--text-secondary) !important; }

/* General utility class replacements for inline styles */
.theme-toggle-btn {
    background: none; border: none; color: var(--text-secondary); cursor: pointer;
    display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%;
    transition: background 0.2s;
}
.theme-toggle-btn:hover { background: rgba(139, 92, 246, 0.1); color: #8B5CF6; }
"""

with open('public/css/custom.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_vars + '\n')

js_toggle_script = """
<script>
    function initTheme() {
        const isLight = localStorage.getItem('theme') === 'light';
        if(isLight) document.body.classList.add('light-mode');
        updateThemeIcon();
    }
    function toggleTheme() {
        document.body.classList.toggle('light-mode');
        const isLight = document.body.classList.contains('light-mode');
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
        updateThemeIcon();
    }
    function updateThemeIcon() {
        const btn = document.getElementById('themeToggleBtn');
        if(!btn) return;
        const isLight = document.body.classList.contains('light-mode');
        btn.innerHTML = isLight 
            ? '<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>'
            : '<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><path d="M12 1v2m0 18v2M4.22 4.22l1.42 1.42m12.72 12.72l1.42 1.42M1 12h2m18 0h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>';
    }
    document.addEventListener('DOMContentLoaded', initTheme);
</script>
"""

btn_html = '<button id="themeToggleBtn" class="theme-toggle-btn" onclick="toggleTheme()"></button>'

replacements = {
    '#111116': 'var(--bg-card)',
    '#1E293B': 'var(--bg-modal)',
    '#0F172A': 'var(--bg-main)',
    '#F1F5F9': 'var(--text-primary)',
    '#94A3B8': 'var(--text-secondary)',
    '#64748B': 'var(--text-muted)',
    '#1E1E24': 'var(--border-color)',
    '#334155': 'var(--border-light)'
}

html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace hex colors
    for hex_code, css_var in replacements.items():
        content = re.sub(hex_code, css_var, content, flags=re.IGNORECASE)

    # Insert button
    avatar_pattern = r'(<div style="width:36px;height:36px;border-radius:50%;background:#8B5CF6;.*?AU</div>)'
    if re.search(avatar_pattern, content):
        content = re.sub(avatar_pattern, btn_html + r' \1', content)

    # Insert script
    if 'function initTheme()' not in content:
        content = content.replace('</body>', js_toggle_script + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done')
