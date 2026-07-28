import re

with open('index.tsx', 'r') as f:
    content = f.read()

# Replace version history
old_version = """                versionHistory: `**v7.6.0 (Atual)**
- **MODO CLARO:** Melhoria no contraste de cores para os nomes de patrocinadores e itens do cardápio no modo claro.
- **PRIVACIDADE DE EVENTO:** O ID do evento online foi ocultado do status por padrão, sendo revelado apenas ao clicar no indicador "Modo Online".
- **ATUALIZAÇÃO DE CRÉDITOS:** Atualização da Inteligência Artificial para Gemini 3.1 PRO.

**v7.5.0**"""

new_version = """                versionHistory: `**v7.8.0 (Atual)**
- **PAINEL SIMPLES:** O painel de números no controlador simples foi atualizado para utilizar o mesmo estilo em grade do painel público, facilitando o acompanhamento e visualização pelo celular.
- **ESTABILIDADE:** Correção de loops e bugs no sistema de atualização do PWA em aparelhos móveis.

**v7.6.0**
- **MODO CLARO:** Melhoria no contraste de cores para os nomes de patrocinadores e itens do cardápio no modo claro.
- **PRIVACIDADE DE EVENTO:** O ID do evento online foi ocultado do status por padrão, sendo revelado apenas ao clicar no indicador "Modo Online".
- **ATUALIZAÇÃO DE CRÉDITOS:** Atualização da Inteligência Artificial para Gemini 3.1 PRO.

**v7.5.0**"""

content = content.replace(old_version, new_version)

old_logic = """            if (called.length > 1) {
                const recent = called.slice(0, -1).reverse().slice(0, 5); // Last 5 except the very last one
                if (DOMElements.scRecents) DOMElements.scRecents.innerHTML = recent.map(num => `<span class="bg-slate-700 text-white px-2 py-1 rounded shadow-sm text-base border border-slate-600">${getLetterForNumber(num)} ${num}</span>`).join('');
            } else {
                if (DOMElements.scRecents) DOMElements.scRecents.innerHTML = '<span class="text-slate-500 text-sm">Nenhum</span>';
            }"""

new_logic = """            const scBoardRows = document.getElementById('sc-board-rows');
            if (scBoardRows) {
                const letters = appConfig.bingoTitle || ['B', 'I', 'N', 'G', 'O'];
                const lettersRange = letters.join('') === 'AJUDE' ? [
                    { letter: 'A', min: 1, max: 15 },
                    { letter: 'J', min: 16, max: 30 },
                    { letter: 'U', min: 31, max: 45 },
                    { letter: 'D', min: 46, max: 60 },
                    { letter: 'E', min: 61, max: 75 }
                ] : [
                    { letter: 'B', min: 1, max: 15 },
                    { letter: 'I', min: 16, max: 30 },
                    { letter: 'N', min: 31, max: 45 },
                    { letter: 'G', min: 46, max: 60 },
                    { letter: 'O', min: 61, max: 75 }
                ];

                if (called.length === 0) {
                    scBoardRows.innerHTML = '<span class="text-slate-500 text-sm">Nenhum sorteio ainda</span>';
                    scBoardRows.dataset.renderedLetters = '';
                } else {
                    const cacheKey = letters.join('') + (game.color || '#14b8a6');
                    if (!scBoardRows.dataset.renderedLetters || scBoardRows.dataset.renderedLetters !== cacheKey) {
                        scBoardRows.innerHTML = '';
                        letters.forEach((letter, index) => {
                            const rowWrapper = document.createElement('div');
                            rowWrapper.className = 'flex flex-row items-stretch border border-slate-700 rounded-lg min-h-[36px] relative z-10 overflow-hidden bg-slate-900';
                            
                            const letterCol = document.createElement('div');
                            letterCol.className = 'w-8 flex items-center justify-center font-black text-white text-lg border-r border-slate-700';
                            letterCol.style.backgroundColor = game.color || '#14b8a6';
                            letterCol.textContent = letter;
                            
                            const numbersCol = document.createElement('div');
                            numbersCol.className = 'flex-1 flex flex-wrap gap-1 items-center p-1';
                            numbersCol.id = `sc-row-${index}`;
                            
                            rowWrapper.appendChild(letterCol);
                            rowWrapper.appendChild(numbersCol);
                            scBoardRows.appendChild(rowWrapper);
                        });
                        scBoardRows.dataset.renderedLetters = cacheKey;
                    } else {
                        document.querySelectorAll('[id^="sc-row-"]').forEach(row => {
                            row.innerHTML = '';
                        });
                    }
                    
                    called.forEach((num) => {
                        let targetIdx = 0;
                        lettersRange.forEach((rng, idx) => {
                            if (num >= rng.min && num <= rng.max) {
                                targetIdx = idx;
                            }
                        });
                        const row = document.getElementById(`sc-row-${targetIdx}`);
                        if (row) {
                            const numDiv = document.createElement('div');
                            numDiv.className = `w-7 h-7 rounded-full flex items-center justify-center font-bold text-white text-xs shadow-sm`;
                            numDiv.style.backgroundColor = game.color || '#14b8a6';
                            numDiv.textContent = num.toString();
                            row.appendChild(numDiv);
                        }
                    });
                }
            }"""

content = content.replace(old_logic, new_logic)

content = content.replace(
    """if (DOMElements.scRecents) DOMElements.scRecents.innerHTML = '<span class="text-slate-500 text-sm">Nenhum</span>';""",
    """const scBoard = document.getElementById('sc-board-rows'); if (scBoard) scBoard.innerHTML = '<span class="text-slate-500 text-sm">Nenhum</span>';"""
)

with open('index.tsx', 'w') as f:
    f.write(content)
print("index.tsx patched")
