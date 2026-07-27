import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement = """                    if (drawnPrizes.length > (window as any).lastDrawnPrizeCount) {
                        const lastPrize = drawnPrizes[drawnPrizes.length - 1];
                        overlayIconEl.innerHTML = "🎁";
                        overlayTitleEl.textContent = "Sorteando Cartela...";
                        overlayEl.classList.remove("hidden");
                        overlayEl.classList.add("flex");
                        
                        let shuffleInterval: any;
                        const startShuffle = (speed: number) => {
                            clearInterval(shuffleInterval);
                            shuffleInterval = setInterval(() => {
                                const randomNum = Math.floor(Math.random() * 9999) + 1;
                                overlayMsgEl.innerHTML = `<span class="text-6xl font-black text-white drop-shadow-md mt-2 block">${randomNum}</span>`;
                            }, speed);
                        };

                        startShuffle(50);
                        setTimeout(() => startShuffle(100), 2000);
                        setTimeout(() => startShuffle(200), 3000);
                        setTimeout(() => startShuffle(400), 4000);
                        
                        setTimeout(() => {
                            clearInterval(shuffleInterval);
                            overlayTitleEl.textContent = "Cartela Sorteada";
                            overlayMsgEl.innerHTML = `<span class="text-6xl font-black text-yellow-300 drop-shadow-md mt-2 block animate-bounce-in">${lastPrize}</span>`;
                            if ((window as any).confetti) {
                                (window as any).confetti({ particleCount: 150, spread: 180, origin: { y: 0.6 }, zIndex: 60 });
                            }
                        }, 5000);
                        
                        setTimeout(() => {
                            overlayEl.classList.add("hidden");
                            overlayEl.classList.remove("flex");
                        }, 10000);
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                    }"""

tsx = re.sub(
    r"if \(drawnPrizes\.length > \(window as any\)\.lastDrawnPrizeCount\) \{.*?\(window as any\)\.lastDrawnPrizeCount = drawnPrizes\.length;\n                    \}",
    replacement,
    tsx,
    flags=re.DOTALL
)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
