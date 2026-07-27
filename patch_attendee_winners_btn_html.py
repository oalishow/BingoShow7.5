import re

with open("attendee.html") as f:
    html = f.read()

winners_btn = """
        <button id="show-winners-attendee-btn" class="absolute top-2 right-12 p-2 text-amber-500 hover:text-amber-600 transition-colors h-8 w-8 flex items-center justify-center rounded-full bg-brand-card shadow border border-brand-border z-50" title="Ver Vencedores">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" /></svg>
        </button>
"""

# replace theme-toggle button to include both
html = html.replace('<button id="theme-toggle-attendee-btn"', winners_btn + '\n        <button id="theme-toggle-attendee-btn"')

# Also add the modal HTML
winners_modal = """
    <!-- Vencedores Modal -->
    <div id="attendee-winners-modal" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-[60] hidden flex-col items-center justify-center p-4">
        <div class="bg-brand-card w-full max-w-lg rounded-2xl shadow-xl flex flex-col border border-brand-border max-h-[85vh] overflow-hidden relative">
            <button id="close-winners-attendee-btn" class="absolute top-3 right-3 text-slate-400 hover:text-slate-600 dark:hover:text-white transition-colors z-10 bg-brand-bg rounded-full p-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
            <div class="p-6 pb-2 border-b border-brand-border bg-brand-bg">
                <h3 class="text-xl font-black text-slate-800 dark:text-white flex items-center gap-2">
                    <span class="text-amber-500">🏆</span> Galeria de Vencedores
                </h3>
            </div>
            <div id="attendee-winners-container" class="p-4 overflow-y-auto flex-1 flex flex-col gap-3">
                <p class="text-slate-500 text-center italic mt-4">Nenhum vencedor registrado ainda.</p>
            </div>
        </div>
    </div>
"""

html = html.replace('</body>', winners_modal + '\n</body>')

with open("attendee.html", "w") as f:
    f.write(html)
