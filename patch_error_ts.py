import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

# Add DOM elements for error screen
dom_elements = """    const onlineModal = document.getElementById('attendee-online-modal')!;
    
    const errorOverlay = document.getElementById('attendee-error-overlay')!;
    const errorMessage = document.getElementById('attendee-error-message')!;

    const showFatalError = (msg: string) => {
        if (contentContainer) contentContainer.classList.add('hidden');
        if (waitingScreen) waitingScreen.classList.add('hidden');
        if (errorOverlay) {
            errorMessage.textContent = msg;
            errorOverlay.classList.remove('hidden');
            errorOverlay.classList.add('flex');
        }
    };"""

content = content.replace("    const onlineModal = document.getElementById('attendee-online-modal')!;", dom_elements)

# Replace "statusBanner.innerHTML = ..." with showFatalError
content = content.replace(
"""        statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-red-900 text-red-200 rounded-xl shadow border border-red-700";
        statusBanner.innerHTML = `⚠️ URL inválida. ID do evento ausente.`;""",
"""        showFatalError('URL inválida. ID do evento ausente.');"""
)

content = content.replace(
"""        statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-red-900 text-red-200 rounded-xl shadow border border-red-700";
        statusBanner.innerHTML = `⚠️ Erro de conexão com o painel: ${e.message}`;""",
"""        showFatalError(`Erro de conexão com o painel: ${e.message}`);"""
)

content = content.replace(
"""            statusBanner.classList.remove('hidden');
            contentContainer.classList.add('hidden');
            statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-red-900 text-red-200 rounded-xl shadow border border-red-700";
            statusBanner.innerHTML = `⚠️ Evento não encontrado. O organizador pode ter fechado a sala.`;""",
"""            showFatalError('Evento não encontrado. O organizador pode ter fechado a sala.');"""
)

with open('attendee.tsx', 'w') as f:
    f.write(content)
print("Attendee TSX patched for fatal errors")
