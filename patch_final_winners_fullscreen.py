import re

with open('index.tsx', 'r') as f:
    content = f.read()

# Replace the appendChild logic in showFinalWinnersModal
old_code = """    let finalModal = DOMElements.finalWinnersModal || document.getElementById('final-winners-modal');
    if (!finalModal) {
        finalModal = document.createElement('div');
        finalModal.id = 'final-winners-modal';
        finalModal.className = 'fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center p-4 z-[110] hidden';
        document.body.appendChild(finalModal);
    }
    DOMElements.finalWinnersModal = finalModal;
    finalModal.innerHTML = getModalTemplates().finalWinners;
    finalModal.classList.remove('hidden');"""

new_code = """    let finalModal = DOMElements.finalWinnersModal || document.getElementById('final-winners-modal');
    if (!finalModal) {
        finalModal = document.createElement('div');
        finalModal.id = 'final-winners-modal';
        finalModal.className = 'fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center p-4 z-[110] hidden';
    }
    
    // Anexa ao elemento em tela cheia se existir, senão ao body
    const targetContainer = document.fullscreenElement || document.body;
    if (finalModal.parentElement !== targetContainer) {
        targetContainer.appendChild(finalModal);
    }

    DOMElements.finalWinnersModal = finalModal;
    finalModal.innerHTML = getModalTemplates().finalWinners;
    finalModal.classList.remove('hidden');"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch successful!")
else:
    print("Old code not found!")
