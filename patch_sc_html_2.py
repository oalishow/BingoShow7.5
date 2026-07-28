import re

with open('index.html', 'r') as f:
    content = f.read()

old_html = """            <div class="text-center w-full max-w-sm mb-6">
                <div class="text-slate-400 text-sm font-bold uppercase mb-1">Último Número</div>
                <div id="sc-last-number" class="flex items-center justify-center min-h-[160px]">
                    --
                </div>
            </div>"""

new_html = """            <div class="w-full max-w-sm bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-lg flex flex-col items-center justify-center relative overflow-hidden transition-colors duration-500 min-h-[180px] mb-6" id="sc-last-card">
                <span class="absolute top-3 left-3 text-xs font-black text-teal-400 uppercase tracking-widest z-10">Último Sorteado</span>
                
                <!-- Bola no estilo do attendee (público) -->
                <div id="sc-last-number-ball" class="w-32 h-32 rounded-full flex items-center justify-center shadow-2xl border-[5px] border-teal-500 transition-colors duration-500 relative overflow-hidden bg-slate-900 my-2">
                    <div class="absolute inset-0 rounded-full opacity-40 bg-gradient-to-br from-white/60 to-transparent mix-blend-overlay"></div>
                    <div class="absolute bottom-0 right-0 w-full h-1/2 bg-black/30 rounded-b-full"></div>
                    <div id="sc-last-number" class="text-6xl font-black text-white tracking-tighter z-10 drop-shadow-md">
                        --
                    </div>
                </div>
            </div>"""

content = content.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(content)
print("sc html 2 patched")
