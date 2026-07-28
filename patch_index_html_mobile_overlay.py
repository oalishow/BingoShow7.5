import re

with open('index.html', 'r') as f:
    content = f.read()

mobile_overlay_html = """
    <!-- Painel Simples Controlador (Mobile) -->
    <div id="simple-controller-overlay" class="fixed inset-0 bg-slate-900/95 backdrop-blur-md z-[300] hidden flex-col w-full h-full text-white">
        <!-- Header -->
        <div class="flex items-center justify-between p-4 border-b border-slate-700 bg-slate-800">
            <h2 id="sc-game-name" class="text-lg font-black uppercase text-teal-400">Rodada Atual</h2>
            <button id="sc-close-btn" class="p-2 text-slate-400 hover:text-white rounded-full bg-slate-700">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
        </div>
        
        <!-- Main Area -->
        <div class="flex-1 overflow-y-auto p-4 flex flex-col items-center">
            
            <div id="sc-status-message" class="text-yellow-400 font-bold mb-4 text-center text-sm hidden"></div>
            
            <div class="text-center w-full max-w-sm mb-6">
                <div class="text-slate-400 text-sm font-bold uppercase mb-1">Último Número</div>
                <div id="sc-last-number" class="text-7xl font-black text-white bg-slate-800 rounded-2xl p-6 border-4 border-teal-500 shadow-[0_0_20px_rgba(20,184,166,0.4)] flex items-center justify-center min-h-[160px]">
                    --
                </div>
            </div>

            <!-- Draw Button -->
            <button id="sc-draw-btn" class="w-full max-w-sm bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-400 hover:to-emerald-500 text-white font-black text-2xl py-6 rounded-2xl shadow-[0_10px_0_rgba(4,120,87,1)] active:translate-y-2 active:shadow-none transition-all mb-8">
                SORTEAR
            </button>
            
            <!-- Recents -->
            <div class="w-full max-w-sm bg-slate-800 p-4 rounded-xl border border-slate-700">
                <div class="text-slate-400 text-sm font-bold uppercase mb-2 flex justify-between">
                    <span>Sorteados (1-75)</span>
                    <span id="sc-drawn-count">0/75</span>
                </div>
                <div id="sc-recents" class="flex flex-wrap gap-2 text-lg font-bold">
                    <span class="text-slate-500 text-sm">Nenhum</span>
                </div>
            </div>
            
        </div>
        
        <!-- Footer / Claims -->
        <div class="p-4 bg-slate-800 border-t border-slate-700">
            <button id="sc-claims-btn" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-900 font-black py-4 rounded-xl flex items-center justify-center gap-2 relative transition-transform active:scale-95">
                VERIFICAR BINGOS
                <span id="sc-claims-badge" class="absolute top-2 right-4 bg-red-600 text-white text-xs px-2 py-1 rounded-full hidden">0</span>
            </button>
        </div>
    </div>
"""

content = content.replace("</body>", mobile_overlay_html + "\n</body>")

with open('index.html', 'w') as f:
    f.write(content)
print("Mobile controller overlay added to index.html")
