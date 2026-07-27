import re

with open("attendee.html") as f:
    html = f.read()

offline_modal = """
    <div id="attendee-offline-modal" class="fixed inset-0 bg-slate-900/90 backdrop-blur-md z-[100] hidden flex-col items-center justify-center p-4 text-center">
        <div class="animate-bounce-in bg-white dark:bg-slate-800 p-8 rounded-3xl border-2 border-red-500 shadow-2xl flex flex-col items-center justify-center max-w-sm w-full">
            <div class="text-6xl mb-4">📡</div>
            <h2 class="text-2xl font-black text-slate-800 dark:text-white mb-2">Conexão Perdida</h2>
            <p class="text-slate-600 dark:text-slate-300 mb-6">Parece que você perdeu a conexão com a internet ou com o servidor. O painel será atualizado assim que a conexão retornar.</p>
            <div class="animate-pulse flex items-center justify-center gap-2 text-red-500 font-bold">
                <svg class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                Reconectando...
            </div>
        </div>
    </div>
"""

html = html.replace('</body>', offline_modal + '\n</body>')

with open("attendee.html", "w") as f:
    f.write(html)
