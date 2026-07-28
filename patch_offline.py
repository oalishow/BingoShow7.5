import re

with open('attendee.html', 'r') as f:
    content = f.read()

new_html = """    <!-- Offline Overlay -->
    <div id="attendee-offline-overlay" class="fixed inset-0 bg-red-900/90 backdrop-blur-md z-[200] hidden flex-col items-center justify-center p-4 text-center">
        <div class="animate-pulse bg-white dark:bg-slate-800 p-8 rounded-3xl border-4 border-red-500 shadow-[0_0_50px_rgba(239,68,68,0.5)] flex flex-col items-center justify-center max-w-sm w-full">
            <div class="text-6xl mb-4">📶</div>
            <h2 class="text-2xl font-black text-slate-800 dark:text-white mb-2">Conexão Perdida</h2>
            <p class="text-slate-600 dark:text-slate-300 mb-6 font-bold">Tentando reconectar ao painel do evento...</p>
            <div class="w-12 h-12 rounded-full border-4 border-slate-200 dark:border-slate-700 border-t-red-500 animate-spin"></div>
        </div>
    </div>
    
    <!-- Online Reconnected Modal -->"""

content = content.replace("    <!-- Vencedores Modal -->", new_html + "\n    <!-- Vencedores Modal -->")

with open('attendee.html', 'w') as f:
    f.write(content)
print("Attendee HTML patched for offline overlay")
