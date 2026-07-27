import re

with open("attendee.html") as f:
    html = f.read()

style_block = """
    <style>
        :root {
            --color-bg: #f8fafc;
            --color-card: #ffffff;
            --color-border: #e2e8f0;
            --color-text: #0ea5e9;
        }
        .dark {
            --color-bg: #060a16;
            --color-card: #0d1527;
            --color-border: #1a2744;
            --color-text: #38bdf8;
        }
    </style>
"""

# add style_block before <script src="https://cdn.tailwindcss.com">
html = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>', style_block + '    <script src="https://cdn.tailwindcss.com"></script>', html)

# update colors in tailwind config
colors_replacement = """colors: {
              brand: {
                bg: 'var(--color-bg)',
                card: 'var(--color-card)',
                border: 'var(--color-border)',
                text: 'var(--color-text)'
              }
            },"""
html = re.sub(r'colors: \{.*?text: \'#38bdf8\'\n\s*\}\n\s*\},', colors_replacement, html, flags=re.DOTALL)

# ensure body text color responds to light/dark
# It has text-white, let's change to text-slate-800 dark:text-white
html = html.replace('text-white font-sans', 'text-slate-800 dark:text-white font-sans')
# overlay text:
html = html.replace('text-slate-200 hidden bg-brand-card/50', 'text-slate-700 dark:text-slate-200 hidden bg-brand-card/50')
# other text-white
html = html.replace('text-6xl font-black text-white', 'text-6xl font-black text-slate-800 dark:text-white')
html = html.replace('text-5xl sm:text-7xl font-black text-white', 'text-5xl sm:text-7xl font-black text-slate-800 dark:text-white')
html = html.replace('text-slate-300 font-mono', 'text-slate-700 dark:text-slate-300 font-mono')
html = html.replace('text-slate-400 font-bold', 'text-slate-500 dark:text-slate-400 font-bold')
html = html.replace('text-white font-bold', 'text-slate-800 dark:text-white font-bold')


# Add a toggle button in the top right
toggle_btn = """
        <button id="theme-toggle-attendee-btn" class="absolute top-2 right-2 p-2 text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white transition-colors h-8 w-8 flex items-center justify-center rounded-full bg-brand-card shadow border border-brand-border z-50" title="Alternar Modo Claro/Escuro">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 dark:hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 hidden dark:block" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
        </button>
"""

html = html.replace('<div id="attendee-content"', toggle_btn + '\n        <div id="attendee-content"')

with open("attendee.html", "w") as f:
    f.write(html)
