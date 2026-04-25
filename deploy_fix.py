import os

# Rename login.html to index.html
if os.path.exists('login.html'):
    os.rename('login.html', 'index.html')
    print('Renamed login.html to index.html')

# Find all HTML files and update links
html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('href="../../login.html"', 'href="../../index.html"')
    new_content = new_content.replace('href="login.html"', 'href="index.html"')
    new_content = new_content.replace("window.location.href = 'login.html'", "window.location.href = 'index.html'")
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated links in {file_path}')

print('Ready for deployment!')
