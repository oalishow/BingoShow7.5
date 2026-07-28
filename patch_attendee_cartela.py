import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                        // Atualizar Último Sorteado
                        if (calledNumbers.length > 0) {
                            const last = calledNumbers[calledNumbers.length - 1];
                            lastNumberEl.textContent = last.toString();
                            lastNumberEl.style.color = activeColor;
                            
                            // Fazer o bola acender
                            lastNumberBallEl.style.boxShadow = `0 0 30px ${activeColor}80`;
                            
                            if (isNewNumber) {
                                lastNumberBallEl.classList.remove('animate-bounce-in');
                                void lastNumberBallEl.offsetWidth; // trigger reflow
                                lastNumberBallEl.classList.add('animate-bounce-in');
                            }
                        } else {
                            lastNumberEl.textContent = '- -';
                            lastNumberEl.style.color = 'white';
                            lastNumberBallEl.style.boxShadow = 'none';
                        }"""

new_code = """                        // Atualizar Último Sorteado
                        const hasWinners = game && game.winners && game.winners.length > 0;
                        const lastWinner = hasWinners ? game.winners[game.winners.length - 1] : null;
                        
                        if (calledNumbers.length > 0) {
                            const last = calledNumbers[calledNumbers.length - 1];
                            lastNumberEl.textContent = last.toString();
                            lastNumberEl.style.color = activeColor;
                            lastTitleEl.textContent = "Último Sorteado";
                            
                            // Fazer o bola acender
                            lastNumberBallEl.style.boxShadow = `0 0 30px ${activeColor}80`;
                            
                            if (isNewNumber) {
                                lastNumberBallEl.classList.remove('animate-bounce-in');
                                void lastNumberBallEl.offsetWidth; // trigger reflow
                                lastNumberBallEl.classList.add('animate-bounce-in');
                            }
                        } else if (lastWinner && lastWinner.cartela) {
                            lastNumberEl.textContent = lastWinner.cartela.toString();
                            lastNumberEl.style.color = activeColor;
                            lastTitleEl.textContent = "Cartela Sorteada";
                            lastNumberBallEl.style.boxShadow = `0 0 30px ${activeColor}80`;
                        } else {
                            lastNumberEl.textContent = '- -';
                            lastNumberEl.style.color = 'white';
                            lastTitleEl.textContent = "Último Sorteado";
                            lastNumberBallEl.style.boxShadow = 'none';
                        }"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee cartela successful!")
else:
    print("Old code not found!")
