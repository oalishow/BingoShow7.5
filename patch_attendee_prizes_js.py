import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement = """                    // Exibir Prêmios
                    const prizeParts = [];
                    const wonPrize1 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize1');
                    const wonPrize2 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize2');
                    const wonPrize3 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize3');

                    if (game.prizes?.prize1) prizeParts.push(`<span class="opacity-70">${labels.prize1Label}:</span> <span class="${wonPrize1 ? 'line-through opacity-50' : ''}">${game.prizes.prize1}</span>`);
                    if (game.prizes?.prize2) prizeParts.push(`<span class="opacity-70">${labels.prize2Label}:</span> <span class="${wonPrize2 ? 'line-through opacity-50' : ''}">${game.prizes.prize2}</span>`);
                    if (game.prizes?.prize3) prizeParts.push(`<span class="opacity-70">${labels.prize3Label}:</span> <span class="${wonPrize3 ? 'line-through opacity-50' : ''}">${game.prizes.prize3}</span>`);
"""

tsx = tsx.replace("""                    // Exibir Prêmios
                    const prizeParts = [];
                    if (game.prizes?.prize1) prizeParts.push(`<span class="opacity-70">${labels.prize1Label}:</span> ${game.prizes.prize1}`);
                    if (game.prizes?.prize2) prizeParts.push(`<span class="opacity-70">${labels.prize2Label}:</span> ${game.prizes.prize2}`);
                    if (game.prizes?.prize3) prizeParts.push(`<span class="opacity-70">${labels.prize3Label}:</span> ${game.prizes.prize3}`);""", replacement)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
