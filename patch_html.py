import re

with open('attendee.html', 'r') as f:
    content = f.read()

modals_html = """    <!-- Alert Modal -->
    <div id="attendee-alert-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[250] hidden flex-col items-center justify-center p-4">
        <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow-2xl max-w-sm w-full text-center border-2 border-emerald-500 animate-bounce-in">
            <h2 class="text-xl font-black text-slate-800 dark:text-white mb-2">Aviso</h2>
            <p id="attendee-alert-message" class="text-slate-600 dark:text-slate-300 mb-6"></p>
            <button id="attendee-alert-ok-btn" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-4 rounded-xl shadow-lg transition-transform active:scale-95">OK</button>
        </div>
    </div>

    <!-- Confirm Modal -->
    <div id="attendee-confirm-modal" class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[250] hidden flex-col items-center justify-center p-4">
        <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow-2xl max-w-sm w-full text-center border-2 border-amber-500 animate-bounce-in">
            <div class="text-4xl mb-4">⚠️</div>
            <h2 class="text-xl font-black text-slate-800 dark:text-white mb-2">Atenção</h2>
            <p id="attendee-confirm-message" class="text-slate-600 dark:text-slate-300 mb-6"></p>
            <div class="flex gap-3">
                <button id="attendee-confirm-cancel-btn" class="flex-1 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-slate-800 dark:text-white font-bold py-3 px-4 rounded-xl transition-colors">Cancelar</button>
                <button id="attendee-confirm-ok-btn" class="flex-1 bg-amber-500 hover:bg-amber-600 text-white font-bold py-3 px-4 rounded-xl shadow-lg transition-transform active:scale-95">Confirmar</button>
            </div>
        </div>
    </div>
</body>"""

content = content.replace("</body>", modals_html)

with open('attendee.html', 'w') as f:
    f.write(content)

print("Patch attendee.html successful!")
