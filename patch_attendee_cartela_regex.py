import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_block = """                        // Atualizar Último Sorteado
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

new_block = """                        // Atualizar Último Sorteado
                        const hasWinners = game && game.winners && game.winners.length > 0;
                        const lastWinner = hasWinners ? game.winners[game.winners.length - 1] : null;

                        if (calledNumbers.length > 0) {
                            const last = calledNumbers[calledNumbers.length - 1];
                            lastNumberEl.textContent = last.toString();
                            lastNumberEl.style.color = activeColor;
                            if (lastTitleEl) lastTitleEl.textContent = "Último Sorteado";
                               
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
                            if (lastTitleEl) lastTitleEl.textContent = "Cartela Sorteada";
                            lastNumberBallEl.style.boxShadow = `0 0 30px ${activeColor}80`;
                        } else {
                            lastNumberEl.textContent = '- -';
                            lastNumberEl.style.color = 'white';
                            if (lastTitleEl) lastTitleEl.textContent = "Último Sorteado";
                            lastNumberBallEl.style.boxShadow = 'none';
                        }"""

# The file might have different spaces or indentation.
# Let's just do a manual string replace after minimizing spaces.

def normalize(text):
    return re.sub(r'\s+', ' ', text)

content_norm = normalize(content)
if normalize(old_block) in content_norm:
    print("Found! Using regex replacement.")
    # More robust regex
    pattern = re.compile(r'// Atualizar Último Sorteado.*?lastNumberBallEl\.style\.boxShadow = \'none\';\s*\}', re.DOTALL)
    content = pattern.sub(new_block.replace('\\', '\\\\'), content)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee cartela successful!")
else:
    print("Old block not found!")

