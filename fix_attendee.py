import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement_state = """                    const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };

                    if (isInitialLoad) {
                        lastRoundTs = state.latestRoundTimestamp || 0;
                        lastBingoTs = state.latestBingoTimestamp || 0;
                        (window as any).lastDrawnPrizeCount = (state.drawnPrizeNumbers || []).length;
                        isInitialLoad = false;
                    }

                    if (state.latestRoundTimestamp && state.latestRoundTimestamp !== lastRoundTs) {"""

# Replace exactly what's there
tsx = re.sub(
    r"                    const labels = state\.appLabels \|\| \{ prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' \};\s*if \(state\.latestRoundTimestamp && state\.latestRoundTimestamp !== lastRoundTs && lastRoundTs !== 0\) \{",
    replacement_state,
    tsx
)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
