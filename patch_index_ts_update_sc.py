import re

with open('index.tsx', 'r') as f:
    content = f.read()

# I will add updateSimpleControllerUI globally inside DOMContentLoaded

update_fn = """
        function updateSimpleControllerUI() {
            if (!DOMElements.scOverlay || DOMElements.scOverlay.classList.contains('hidden')) return;
            const { activeGameNumber, gamesData } = appStore.state;
            if (!activeGameNumber || !gamesData[activeGameNumber]) {
                if (DOMElements.scGameName) DOMElements.scGameName.textContent = "Nenhuma Rodada Ativa";
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.textContent = "--";
                if (DOMElements.scRecents) DOMElements.scRecents.innerHTML = '<span class="text-slate-500 text-sm">Nenhum</span>';
                if (DOMElements.scDrawnCount) DOMElements.scDrawnCount.textContent = '0/75';
                return;
            }
            const game = gamesData[activeGameNumber];
            if (DOMElements.scGameName) DOMElements.scGameName.textContent = game.name || `Rodada ${activeGameNumber}`;
            
            const called = game.calledNumbers;
            if (called.length > 0) {
                const last = called[called.length - 1];
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.innerHTML = `<span class="text-6xl text-teal-400 font-bold mr-2">${getLetterForNumber(last)}</span>${last}`;
            } else {
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.textContent = "--";
            }
            
            if (DOMElements.scDrawnCount) DOMElements.scDrawnCount.textContent = `${called.length}/75`;
            
            if (called.length > 1) {
                const recent = called.slice(0, -1).reverse().slice(0, 5); // Last 5 except the very last one
                if (DOMElements.scRecents) DOMElements.scRecents.innerHTML = recent.map(num => `<span class="bg-slate-700 text-white px-2 py-1 rounded shadow-sm text-base border border-slate-600">${getLetterForNumber(num)} ${num}</span>`).join('');
            } else {
                if (DOMElements.scRecents) DOMElements.scRecents.innerHTML = '<span class="text-slate-500 text-sm">Nenhum</span>';
            }
        }
"""

content = content.replace("function updateMasterBoardCell(numberToUpdate: number) {", update_fn + "\n        function updateMasterBoardCell(numberToUpdate: number) {")

# Call updateSimpleControllerUI() inside updateCurrentNumberDisplay()
call_hook = """
            updateSimpleControllerUI();
"""
content = content.replace("            // Update labels in other modals if open", call_hook + "\n            // Update labels in other modals if open")

# And inside renderMasterBoard() at the very end
content = content.replace("            updateMasterBoardStats();\n        }", "            updateMasterBoardStats();\n            updateSimpleControllerUI();\n        }")

with open('index.tsx', 'w') as f:
    f.write(content)
print("updateSimpleControllerUI function added")
