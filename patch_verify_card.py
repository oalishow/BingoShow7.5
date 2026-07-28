import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """            DOMElements.customAlertModal.innerHTML = `<div class="modal-content bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-2xl max-w-md w-full text-center">
                <h2 class="text-3xl font-bold text-gray-900 dark:text-white mb-2">Resultado da Verificação</h2>
                <h3 class="text-xl text-slate-800 dark:text-slate-300 mb-4">Cartela N° ${String(cardData.series).padStart(4, '0')}</h3>
                ${resultHtml}
                ${cardHTML}
                <button id="close-card-result-btn" class="mt-6 bg-slate-600 hover:bg-slate-700 text-white font-bold py-2 px-8 rounded-full text-lg">Fechar</button>
            </div>`;
            
            DOMElements.customAlertModal.classList.remove('hidden');"""

new_code = """            DOMElements.customAlertModal.innerHTML = `<div class="modal-content bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-2xl max-w-md w-full text-center">
                <h2 class="text-3xl font-bold text-gray-900 dark:text-white mb-2">Resultado da Verificação</h2>
                <h3 class="text-xl text-slate-800 dark:text-slate-300 mb-4">Cartela N° ${String(cardData.series).padStart(4, '0')}</h3>
                ${resultHtml}
                ${cardHTML}
                <button id="close-card-result-btn" class="mt-6 bg-slate-600 hover:bg-slate-700 text-white font-bold py-2 px-8 rounded-full text-lg">Fechar</button>
            </div>`;
            
            DOMElements.customAlertModal.classList.remove('hidden');

            if (isWinner) {
                // Broadcast verified winning card to attendee view
                if (!activeGame.verifiedWinningCards) {
                    activeGame.verifiedWinningCards = [];
                }
                activeGame.verifiedWinningCards.push({
                    series: cardData.series,
                    uuid: uuid,
                    numbers: cardData.numbers
                });
                appStore.debouncedSave(true);
            }"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch successful!")
else:
    print("Old code not found!")
