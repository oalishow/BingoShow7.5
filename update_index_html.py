import re

with open('index.html', 'r') as f:
    content = f.read()

old_html = """            <div class="w-full max-w-sm bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-lg flex flex-col items-center justify-center relative overflow-hidden transition-colors duration-500 min-h-[180px] mb-6" id="sc-last-card">
                <span class="absolute top-3 left-3 text-xs font-black text-teal-400 uppercase tracking-widest z-10">Último Sorteado</span>
                
                <!-- Bola no estilo do attendee (público) -->
                <div id="sc-last-number-ball" class="w-32 h-32 rounded-full flex items-center justify-center shadow-2xl border-[5px] border-teal-500 transition-colors duration-500 relative overflow-hidden bg-slate-900 my-2">
                    <div class="absolute inset-0 rounded-full opacity-40 bg-gradient-to-br from-white/60 to-transparent mix-blend-overlay"></div>
                    <div class="absolute bottom-0 right-0 w-full h-1/2 bg-black/30 rounded-b-full"></div>
                    <div id="sc-last-number" class="text-6xl font-black text-white tracking-tighter z-10 drop-shadow-md">
                        --
                    </div>
                </div>
            </div>

            <!-- Draw Button -->
            <button id="sc-draw-btn" class="w-full max-w-sm bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-400 hover:to-emerald-500 text-white font-black text-2xl py-6 rounded-2xl shadow-[0_10px_0_rgba(4,120,87,1)] active:translate-y-2 active:shadow-none transition-all mb-8">
                SORTEAR
            </button>
            
            <!-- Board -->
            <div class="w-full max-w-sm bg-slate-800 p-4 rounded-xl border border-slate-700">
                <div class="text-slate-400 text-sm font-bold uppercase mb-2 flex justify-between">
                    <span>Números Sorteados</span>
                    <span id="sc-drawn-count">0/75</span>
                </div>
                <div id="sc-board-rows" class="flex flex-col gap-1.5 relative overflow-hidden transition-colors duration-500">
                    <span class="text-slate-500 text-sm">Nenhum sorteio ainda</span>
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
            </div>

            <!-- Últimos 3 Sorteados -->
            <div class="w-full max-w-sm bg-slate-800 border border-slate-700 rounded-xl p-4 shadow-lg flex flex-col relative overflow-hidden transition-colors duration-500 mb-6" id="sc-recent-card">
                <span class="w-full text-left text-xs font-black text-teal-400 uppercase tracking-widest mb-2 z-10">Últimos 3 Sorteados</span>
                <div id="sc-recent-numbers" class="bg-slate-900 border border-slate-700 rounded-lg p-2 text-center min-h-[60px] flex items-center justify-center gap-3 z-10 transition-colors duration-500">
                    <span class="text-slate-500 font-bold text-sm">Aguardando sorteio</span>
                </div>
            </div>

            <!-- Draw Button -->
            <button id="sc-draw-btn" class="w-full max-w-sm bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-400 hover:to-emerald-500 text-white font-black text-2xl py-6 rounded-2xl shadow-[0_10px_0_rgba(4,120,87,1)] active:translate-y-2 active:shadow-none transition-all mb-8">
                SORTEAR
            </button>
            
            <!-- Board -->
            <div class="w-full max-w-sm bg-slate-800 p-0 rounded-xl border border-slate-700 overflow-hidden shadow-lg mb-6">
                <div class="bg-slate-900 p-3 text-slate-400 text-xs font-black uppercase flex justify-between border-b border-slate-700">
                    <span>Números Sorteados</span>
                    <span id="sc-drawn-count">0/75</span>
                </div>
                <div id="sc-board-rows" class="flex flex-col gap-1 relative overflow-hidden transition-colors duration-500 bg-slate-800 p-2">
                    <span class="text-slate-500 text-sm p-4 text-center w-full">Nenhum sorteio ainda</span>
                </div>
            </div>"""

content = content.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(content)
print("index.html patched")
