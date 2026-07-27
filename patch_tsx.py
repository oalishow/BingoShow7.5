import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement = """                    if (state.latestRoundTimestamp && state.latestRoundTimestamp !== lastRoundTs && lastRoundTs !== 0) {
                        if (config.customLogo) {
                            overlayIconEl.innerHTML = `<img src="${config.customLogo}" alt="Logo" class="h-24 w-auto object-contain drop-shadow-md" />`;
                        } else {
                            overlayIconEl.textContent = "🎯";
                        }
                        overlayTitleEl.textContent = "Nova Rodada";
                        overlayMsgEl.textContent = game.name || `Rodada ${eventData.activeGameNumber}`;
                        overlayEl.classList.remove("hidden");
                        overlayEl.classList.add("flex");
                        setTimeout(() => {
                            overlayEl.classList.add("hidden");
                            overlayEl.classList.remove("flex");
                        }, 4000);
                    }
                    lastRoundTs = state.latestRoundTimestamp || 0;

                    if (state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs && lastBingoTs !== 0) {
                        if ((window as any).confetti) {
                            const duration = 5 * 1000;
                            const animationEnd = Date.now() + duration;
                            const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 60 };
                            const interval: any = setInterval(function() {
                                const timeLeft = animationEnd - Date.now();
                                if (timeLeft <= 0) return clearInterval(interval);
                                const particleCount = 50 * (timeLeft / duration);
                                (window as any).confetti(Object.assign({}, defaults, { particleCount, origin: { x: Math.random(), y: Math.random() - 0.2 } }));
                            }, 250);
                        }
                        
                        const lastWinner = game.winners && game.winners.length > 0 ? game.winners[game.winners.length - 1] : null;
                        if (lastWinner) {
                            overlayIconEl.innerHTML = "🏆";
                            overlayTitleEl.textContent = "BINGO!";
                            overlayMsgEl.innerHTML = `<span class="text-2xl font-black text-white">${lastWinner.name}</span><br/><span class="text-lg text-yellow-300 font-bold mt-2 block">${lastWinner.prize}</span>`;
                            overlayEl.classList.remove("hidden");
                            overlayEl.classList.add("flex");
                            setTimeout(() => {
                                overlayEl.classList.add("hidden");
                                overlayEl.classList.remove("flex");
                            }, 8000);
                        }
                    }
                    lastBingoTs = state.latestBingoTimestamp || 0;

                    // Drawn Cartelas
                    const drawnPrizes = state.drawnPrizeNumbers || [];
                    if (!((window as any).lastDrawnPrizeCount)) {
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                    } else if (drawnPrizes.length > (window as any).lastDrawnPrizeCount) {
                        const lastPrize = drawnPrizes[drawnPrizes.length - 1];
                        overlayIconEl.innerHTML = "🎁";
                        overlayTitleEl.textContent = "Cartela Sorteada";
                        overlayMsgEl.innerHTML = `<span class="text-6xl font-black text-yellow-300 drop-shadow-md mt-2 block">${lastPrize}</span>`;
                        overlayEl.classList.remove("hidden");
                        overlayEl.classList.add("flex");
                        
                        if ((window as any).confetti) {
                            (window as any).confetti({ particleCount: 150, spread: 180, origin: { y: 0.6 }, zIndex: 60 });
                        }
                        
                        setTimeout(() => {
                            overlayEl.classList.add("hidden");
                            overlayEl.classList.remove("flex");
                        }, 6000);
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                    }
                    if (drawnPrizes.length < (window as any).lastDrawnPrizeCount) {
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                    }

                    isVerifyingState = state.isVerifying || false;
                    if (isVerifyingState) {
                        overlayIconEl.textContent = "🔍";
                        overlayTitleEl.textContent = "Aguardando conferência...";
                        overlayMsgEl.textContent = "Verificando as cartelas chamadas";
                        overlayEl.classList.remove("hidden");
                        overlayEl.classList.add("flex");
                    } else if (!isVerifyingState && overlayIconEl.textContent === "🔍") {
                        overlayEl.classList.add("hidden");
                        overlayEl.classList.remove("flex");
                    }"""

tsx = re.sub(
    r"if \(state\.latestRoundTimestamp.*?overlayEl\.classList\.remove\(\"flex\"\);\n                    }",
    replacement,
    tsx,
    flags=re.DOTALL
)

# Insert modal logic for donate button at the end
tsx += """
// Modal Logic
document.addEventListener('DOMContentLoaded', () => {
    const donateBtn = document.getElementById('donate-btn-attendee');
    const pixModal = document.getElementById('pix-donation-modal-attendee');
    const closeBtn = document.getElementById('close-donation-btn-attendee');

    if (donateBtn && pixModal && closeBtn) {
        donateBtn.addEventListener('click', () => {
            pixModal.classList.remove('hidden');
            pixModal.classList.add('flex');
        });

        closeBtn.addEventListener('click', () => {
            pixModal.classList.add('hidden');
            pixModal.classList.remove('flex');
        });
    }
});
"""

with open("attendee.tsx", "w") as f:
    f.write(tsx)
