import re

with open('attendee.html', 'r') as f:
    content = f.read()

new_html = """    <!-- Error Overlay -->
    <div id="attendee-error-overlay" class="fixed inset-0 bg-brand-bg/90 backdrop-blur-md z-[200] hidden flex-col items-center justify-center p-4 text-center">
        <div class="bg-brand-card p-8 rounded-3xl border-4 border-red-500 shadow-2xl flex flex-col items-center justify-center max-w-sm w-full">
            <div class="text-6xl mb-4">⚠️</div>
            <h2 class="text-2xl font-black text-slate-800 dark:text-white mb-2">Ops!</h2>
            <p id="attendee-error-message" class="text-slate-600 dark:text-slate-300 font-bold mb-6">Erro desconhecido.</p>
        </div>
    </div>
    
    <!-- Offline Overlay -->"""

content = content.replace("    <!-- Offline Overlay -->", new_html)

with open('attendee.html', 'w') as f:
    f.write(content)
print("Attendee HTML patched for error overlay")
