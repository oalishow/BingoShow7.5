import re

with open('attendee.html', 'r') as f:
    content = f.read()

# Replace the status banner with a nice waiting screen overlay
new_html = """
        <canvas id="confetti-canvas" class="fixed inset-0 w-full h-full pointer-events-none z-50"></canvas>
        
        <!-- Beautiful Waiting Screen -->
        <div id="attendee-waiting-screen" class="hidden flex-1 flex-col items-center justify-center w-full min-h-[70vh] animate-fade-in p-4 text-center">
            <img id="waiting-logo" src="" alt="Logo" class="h-32 w-auto hidden object-contain mb-6 drop-shadow-xl animate-bounce-in" />
            <h1 id="waiting-app-name" class="text-3xl sm:text-4xl font-black uppercase tracking-tight text-slate-800 dark:text-white drop-shadow-md mb-2"></h1>
            
            <div class="mt-8 bg-brand-card/80 backdrop-blur-md p-6 rounded-3xl border border-brand-border shadow-2xl flex flex-col items-center max-w-sm w-full">
                <div class="w-16 h-16 rounded-full border-4 border-slate-200 dark:border-slate-700 border-t-sky-500 animate-spin mb-4"></div>
                <h2 id="waiting-title" class="text-xl font-black text-slate-800 dark:text-white mb-2">Aguardando</h2>
                <p id="waiting-message" class="text-slate-600 dark:text-slate-400 text-sm font-bold">A próxima rodada começará em breve...</p>
            </div>
        </div>

        <div id="attendee-status-banner" class="w-full p-4 text-center text-sm font-bold bg-yellow-900/50 text-yellow-200 rounded-xl shadow-sm border border-yellow-700/50 animate-pulse hidden"></div>
"""

content = re.sub(
    r'<canvas id="confetti-canvas" class="fixed inset-0 w-full h-full pointer-events-none z-50"></canvas>\s*<div id="attendee-status-banner"[^>]*>.*?</div>',
    new_html,
    content,
    flags=re.DOTALL
)

with open('attendee.html', 'w') as f:
    f.write(content)
print("Attendee HTML patched")
