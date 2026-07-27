import re

with open("attendee.tsx") as f:
    content = f.read()

# Replace the Nova Rodada block
old_nova_rodada = """                    if (state.latestRoundTimestamp && state.latestRoundTimestamp !== lastRoundTs) {
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
                    lastRoundTs = state.latestRoundTimestamp || 0;"""

new_nova_rodada = """                    const isNewBingo = state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs;
                    if (state.latestRoundTimestamp && state.latestRoundTimestamp !== lastRoundTs) {
                        const showNovaRodada = () => {
                            if (config.customLogo) {
                                overlayIconEl.innerHTML = `<img src="${config.customLogo}" alt="Logo" class="h-24 w-auto object-contain drop-shadow-md" />`;
                            } else {
                                overlayIconEl.textContent = "🎯";
                            }
                            overlayTitleEl.textContent = "Nova Rodada";
                            overlayMsgEl.textContent = game ? (game.name || `Rodada ${eventData.activeGameNumber}`) : `Rodada ${eventData.activeGameNumber}`;
                            overlayEl.classList.remove("hidden");
                            overlayEl.classList.add("flex");
                            setTimeout(() => {
                                overlayEl.classList.add("hidden");
                                overlayEl.classList.remove("flex");
                            }, 4000);
                        };
                        
                        if (isNewBingo) {
                            // Delay Nova Rodada until BINGO modal finishes
                            setTimeout(showNovaRodada, 8000);
                        } else {
                            showNovaRodada();
                        }
                    }
                    lastRoundTs = state.latestRoundTimestamp || 0;"""

content = content.replace(old_nova_rodada, new_nova_rodada)

with open("attendee.tsx", "w") as f:
    f.write(content)
