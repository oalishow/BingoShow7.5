import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    """<button id="sc-claims-btn" class="w-full bg-amber-500 hover:bg-amber-400 text-slate-900 font-black py-4 rounded-xl flex items-center justify-center gap-2 relative transition-transform active:scale-95">
                VERIFICAR BINGOS
                <span id="sc-claims-badge" class="absolute top-2 right-4 bg-red-600 text-white text-xs px-2 py-1 rounded-full hidden">0</span>
            </button>""",
    """<button id="sc-claims-btn" class="w-full bg-slate-700 hover:bg-slate-600 text-white font-bold py-4 rounded-xl flex items-center justify-center gap-2 relative transition-transform active:scale-95 border border-slate-600">
                VOLTAR AO PAINEL COMPLETO
            </button>"""
)

with open('index.html', 'w') as f:
    f.write(content)
print("Button text changed")
