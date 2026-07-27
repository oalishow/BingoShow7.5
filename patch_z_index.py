import re

with open("attendee.html") as f:
    html = f.read()

# Fix Z-Indexes
html = html.replace('id="attendee-bingo-overlay" class="fixed inset-0 bg-slate-900/90 backdrop-blur-md z-[50]', 'id="attendee-bingo-overlay" class="fixed inset-0 bg-slate-900/90 backdrop-blur-md z-[110]')
html = html.replace('id="attendee-overlay" class="fixed inset-0 bg-brand-bg/90 backdrop-blur-sm z-40', 'id="attendee-overlay" class="fixed inset-0 bg-brand-bg/90 backdrop-blur-sm z-[90]')
html = html.replace('id="attendee-pending-overlay" class="fixed inset-0 bg-brand-bg/90 backdrop-blur-sm z-[45]', 'id="attendee-pending-overlay" class="fixed inset-0 bg-brand-bg/90 backdrop-blur-sm z-[80]')
html = html.replace('id="attendee-offline-modal" class="fixed inset-0 bg-slate-900/90 backdrop-blur-md z-[100]', 'id="attendee-offline-modal" class="fixed inset-0 bg-slate-900/90 backdrop-blur-md z-[150]')

# Add Online Restored Modal
online_modal = """
    <div id="attendee-online-modal" class="fixed inset-0 bg-green-900/90 backdrop-blur-md z-[150] hidden flex-col items-center justify-center p-4 text-center">
        <div class="animate-bounce-in bg-white dark:bg-slate-800 p-8 rounded-3xl border-2 border-green-500 shadow-[0_0_30px_rgba(34,197,94,0.3)] flex flex-col items-center justify-center max-w-sm w-full">
            <div class="text-6xl mb-4">🟢</div>
            <h2 class="text-2xl font-black text-slate-800 dark:text-white mb-2">Conexão Restaurada!</h2>
            <p class="text-slate-600 dark:text-slate-300">O painel foi atualizado.</p>
        </div>
    </div>
"""

html = html.replace('<!-- Vencedores Modal -->', online_modal + '\n    <!-- Vencedores Modal -->')

with open("attendee.html", "w") as f:
    f.write(html)
