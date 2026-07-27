import re

with open("attendee.html") as f:
    html = f.read()

new_footer = """
        <footer class="w-full mt-auto flex flex-col items-center gap-3 pt-6 pb-2 text-center relative z-30">
            <p class="text-[9px] sm:text-[10px] text-slate-500 font-medium uppercase tracking-widest flex items-center justify-center gap-1">
                <svg class="w-3 h-3 text-brand-text" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                Powered by Bingo Show
            </p>
            <div class="flex items-center gap-3">
                <button id="donate-btn-attendee" class="flex items-center gap-1.5 px-3 py-1.5 bg-brand-text/10 hover:bg-brand-text/20 text-brand-text rounded-full font-bold transition-colors shadow-sm text-xs border border-brand-text/30">
                    <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"></path></svg>
                    Apoiar Projeto
                </button>
            </div>
        </footer>
        
        <div id="pix-donation-modal-attendee" class="fixed inset-0 bg-brand-bg/90 backdrop-blur-sm hidden z-50 flex-col items-center justify-center p-4">
            <div class="bg-brand-card border border-brand-border p-6 rounded-2xl shadow-2xl max-w-sm w-full text-center relative animate-bounce-in">
                <button id="close-donation-btn-attendee" class="absolute top-3 right-3 text-slate-400 hover:text-slate-200">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <div class="w-16 h-16 bg-brand-text/10 text-brand-text rounded-full flex items-center justify-center mx-auto mb-4 border border-brand-text/30">
                    <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"></path></svg>
                </div>
                <h3 class="text-xl font-bold text-white mb-2">Apoie o Projeto!</h3>
                <p class="text-sm text-slate-400 mb-6">Sua doação ajuda a manter o Bingo Show. Leia o QR Code abaixo com o app do seu banco.</p>
                
                <div class="bg-white p-4 rounded-xl inline-block mb-4">
                    <img src="/pix-qr.png" alt="QR Code Pix" class="w-48 h-48 object-contain rounded-lg" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTAiIGhlaWdodD0iMTUwIiB2aWV3Qm94PSIwIDAgMTUwIDE1MCI+PHJlY3Qgd2lkdGg9IjE1MCIgaGVpZ2h0PSIxNTAiIGZpbGw9IiNlN2U1ZTQiLz48dGV4dCB4PSI3NSIgeT0iNzUiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjE0IiBmaWxsPSIjOWNhM2FmIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkeT0iLjMiPlNlbSBJbWFnZW08L3RleHQ+PC9zdmc+'">
                </div>
                
                <p class="text-[10px] sm:text-xs text-slate-300 font-mono select-all bg-brand-bg border border-brand-border p-2 rounded break-all">
                    00020126480014br.gov.bcb.pix0126lucas.g.almeida1@gmail.com5204000053039865802BR5925Lucas Guedes de Almeida O6012Campo Grande62070503***6304FE29
                </p>
                <p class="text-[9px] text-slate-500 mt-2">Chave Pix: lucas.g.almeida1@gmail.com</p>
            </div>
        </div>
"""

html = re.sub(r"<footer.*?</footer>", new_footer, html, flags=re.DOTALL)
with open("attendee.html", "w") as f:
    f.write(html)
