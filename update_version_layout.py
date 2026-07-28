import re

with open('index.html', 'r') as f:
    content = f.read()

old_html = """            <!-- Recents -->
            <div class="w-full max-w-sm bg-slate-800 p-4 rounded-xl border border-slate-700">
                <div class="text-slate-400 text-sm font-bold uppercase mb-2 flex justify-between">
                    <span>Sorteados (1-75)</span>
                    <span id="sc-drawn-count">0/75</span>
                </div>
                <div id="sc-recents" class="flex flex-wrap gap-2 text-lg font-bold">
                    <span class="text-slate-500 text-sm">Nenhum</span>
                </div>
            </div>"""

new_html = """            <!-- Board -->
            <div class="w-full max-w-sm bg-slate-800 p-4 rounded-xl border border-slate-700">
                <div class="text-slate-400 text-sm font-bold uppercase mb-2 flex justify-between">
                    <span>Números Sorteados</span>
                    <span id="sc-drawn-count">0/75</span>
                </div>
                <div id="sc-board-rows" class="flex flex-col gap-1.5 relative overflow-hidden transition-colors duration-500">
                    <span class="text-slate-500 text-sm">Nenhum sorteio ainda</span>
                </div>
            </div>"""

content = content.replace(old_html, new_html)

# Update footer version
content = re.sub(r'Bingo Show v\d+\.\d+\.\d+', 'Bingo Show v7.8.0', content)
content = re.sub(r'Build: \d{2}/\d{2}/\d{4}', 'Build: 28/07/2026', content)

with open('index.html', 'w') as f:
    f.write(content)
print("index.html patched")
