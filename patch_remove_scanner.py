import re

with open("index.html") as f:
    html = f.read()

html = html.replace('<div class="grid grid-cols-2 gap-2 mb-4 flex-shrink-0">', '<div class="flex flex-col gap-2 mb-4 flex-shrink-0">')
html = re.sub(r'<button id="show-card-scanner-btn" .*?</button>', '', html)

with open("index.html", "w") as f:
    f.write(html)
