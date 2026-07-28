import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_logic = """            const scBoardRows = document.getElementById('sc-board-rows');
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

new_logic = """            const scRecentNumbers = document.getElementById('sc-recent-numbers');
            if (scRecentNumbers) {
                if (called.length > 0) {
                    const last3 = called.slice(-4, -1).reverse();
                    if (last3.length > 0) {
                        scRecentNumbers.innerHTML = '';
                        last3.forEach((num, idx) => {
                            const pill = document.createElement('div');
                            pill.className = `w-12 h-12 rounded-full bg-slate-900 text-white border-2 flex items-center justify-center font-black text-lg shadow-sm relative overflow-hidden`;
                            pill.style.borderColor = game.color || '#38bdf8';
                            
                            const glare = document.createElement('div');
                            glare.className = 'absolute inset-0 rounded-full opacity-30 bg-gradient-to-br from-white/50 to-transparent mix-blend-overlay';
                            pill.appendChild(glare);
                            
                            const numSpan = document.createElement('span');
                            numSpan.className = 'z-10 relative';
                            numSpan.textContent = num.toString();
                            pill.appendChild(numSpan);
                            
                            scRecentNumbers.appendChild(pill);
                        });
                    } else {
                        scRecentNumbers.innerHTML = '<span class="text-slate-500 font-bold text-sm">⏳ Aguardando Início do Sorteio...</span>';
                    }
                } else {
                    scRecentNumbers.innerHTML = '<span class="text-slate-500 font-bold text-sm">⏳ Aguardando Início do Sorteio...</span>';
                }
            }

            const scBoardRows = document.getElementById('sc-board-rows');
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
                    scBoardRows.innerHTML = '<span class="text-slate-500 text-sm p-4 text-center w-full">Nenhum sorteio ainda</span>';
                    scBoardRows.dataset.renderedLetters = '';
                } else {
                    const cacheKey = letters.join('') + (game.color || '#14b8a6');
                    if (!scBoardRows.dataset.renderedLetters || scBoardRows.dataset.renderedLetters !== cacheKey) {
                        scBoardRows.innerHTML = '';
                        letters.forEach((letter, index) => {
                            const rowWrapper = document.createElement('div');
                            rowWrapper.className = 'flex flex-row items-stretch border border-slate-700 rounded-lg min-h-[56px] relative z-10 overflow-hidden bg-slate-900';
                            
                            const letterCol = document.createElement('div');
                            letterCol.className = 'w-16 flex items-center justify-center font-black transition-colors duration-300 text-4xl border-r border-slate-700 bg-slate-800';
                            letterCol.style.color = game.color || '#38bdf8';
                            letterCol.textContent = letter;
                            
                            const numbersCol = document.createElement('div');
                            numbersCol.className = 'flex-1 flex flex-wrap gap-2 items-center p-2 bg-slate-900 transition-colors duration-300';
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
                            numDiv.className = `w-10 h-10 rounded-full flex items-center justify-center font-bold text-white shadow-sm transition-all duration-500 relative overflow-hidden border-2`;
                            numDiv.style.borderColor = game.color || '#38bdf8';
                            numDiv.style.backgroundColor = (game.color || '#38bdf8') + '20';
                            
                            const numSpan = document.createElement('span');
                            numSpan.className = 'z-10 relative text-base';
                            numSpan.textContent = num.toString();
                            numDiv.appendChild(numSpan);
                            row.appendChild(numDiv);
                        }
                    });
                }
            }"""

content = content.replace(old_logic, new_logic)

with open('index.tsx', 'w') as f:
    f.write(content)
print("index.tsx patched")
