import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<div id="sc-last-number" class="text-7xl font-black text-white bg-slate-800 rounded-2xl p-6 border-4 border-teal-500 shadow-[0_0_20px_rgba(20,184,166,0.4)] flex items-center justify-center min-h-[160px]">',
    '<div id="sc-last-number" class="flex items-center justify-center min-h-[160px]">'
)

with open('index.html', 'w') as f:
    f.write(content)
print("sc html patched")
