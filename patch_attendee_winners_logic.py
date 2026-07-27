import re

with open("attendee.tsx") as f:
    tsx = f.read()

winners_logic = """
// Winners Modal Logic
const winnersBtn = document.getElementById('show-winners-attendee-btn');
const winnersModal = document.getElementById('attendee-winners-modal');
const closeWinnersBtn = document.getElementById('close-winners-attendee-btn');
const winnersContainer = document.getElementById('attendee-winners-container');

if (winnersBtn && winnersModal && closeWinnersBtn) {
    winnersBtn.addEventListener('click', () => {
        winnersModal.classList.remove('hidden');
        winnersModal.classList.add('flex');
    });
    
    closeWinnersBtn.addEventListener('click', () => {
        winnersModal.classList.add('hidden');
        winnersModal.classList.remove('flex');
    });
}

function updateWinnersList(gamesData: any) {
    if (!winnersContainer) return;
    
    const allWinners: any[] = [];
    if (gamesData) {
        Object.values(gamesData).forEach((game: any) => {
            if (game.winners && game.winners.length > 0) {
                allWinners.push(...game.winners);
            }
        });
    }
    
    allWinners.sort((a, b) => b.id - a.id);
    
    if (allWinners.length === 0) {
        winnersContainer.innerHTML = '<p class="text-slate-500 text-center italic mt-4">Nenhum vencedor registrado ainda.</p>';
        return;
    }
    
    winnersContainer.innerHTML = '';
    allWinners.forEach(winnerData => {
        const winnerCard = document.createElement('div');
        winnerCard.className = 'bg-white dark:bg-slate-800 p-3 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm flex items-center justify-between';
        
        let prizeText = winnerData.prize;
        if (winnerData.bingoType === 'prize1' || winnerData.bingoType === 'prize2' || winnerData.bingoType === 'prize3') {
             prizeText = `${winnerData.prize} (${winnerData.bingoType === 'prize1' ? '1º' : winnerData.bingoType === 'prize2' ? '2º' : '3º'})`;
        }

        const gameName = (winnerData.gameNumber === 'Brinde' || winnerData.gameNumber === 'Leilão') 
                ? '' 
                : (gamesData[winnerData.gameNumber]?.name || `Rodada ${winnerData.gameNumber}`);
        
        winnerCard.innerHTML = `
            <div>
                 <p class="font-bold text-slate-800 dark:text-white text-lg">${winnerData.name}</p>
                 <p class="text-sm font-semibold text-amber-500 dark:text-amber-400">${prizeText}</p>
                 <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">${gameName}</p>
            </div>
            <div class="text-3xl">🏆</div>
        `;
        winnersContainer.appendChild(winnerCard);
    });
}
"""

tsx = tsx.replace("// Modal Logic", winners_logic + "\n// Modal Logic")

# In onSnapshot, call updateWinnersList(state.gamesData)
tsx = tsx.replace("const config = state.appConfig;", "const config = state.appConfig;\n                    updateWinnersList(state.gamesData);")

with open("attendee.tsx", "w") as f:
    f.write(tsx)
