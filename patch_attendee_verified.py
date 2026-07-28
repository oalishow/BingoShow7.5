import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                        const hasWinners = game && game.winners && game.winners.length > 0;
                        const lastWinner = hasWinners ? game.winners[game.winners.length - 1] : null;

                        if (calledNumbers.length > 0) {"""

new_code = """                        const hasWinners = game && game.winners && game.winners.length > 0;
                        const lastWinner = hasWinners ? game.winners[game.winners.length - 1] : null;
                        const hasVerifiedCards = game && game.verifiedWinningCards && game.verifiedWinningCards.length > 0;
                        const lastVerifiedCard = hasVerifiedCards ? game.verifiedWinningCards[game.verifiedWinningCards.length - 1] : null;

                        if (lastVerifiedCard) {
                            lastNumberEl.textContent = lastVerifiedCard.series.toString();
                            lastNumberEl.style.color = activeColor;
                            if (lastTitleEl) lastTitleEl.textContent = "Cartela Bateu!";
                            lastNumberBallEl.style.boxShadow = `0 0 30px ${activeColor}80`;
                            
                            if (isNewNumber || (window as any)._lastVerifiedSeries !== lastVerifiedCard.series) {
                                (window as any)._lastVerifiedSeries = lastVerifiedCard.series;
                                lastNumberBallEl.classList.remove('animate-bounce-in');
                                void lastNumberBallEl.offsetWidth; // trigger reflow
                                lastNumberBallEl.classList.add('animate-bounce-in');
                            }
                        } else if (calledNumbers.length > 0) {"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch successful!")
else:
    print("Old code not found!")
