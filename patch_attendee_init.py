import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement = """    let lastBingoTs = 0;
    let lastRoundTs = 0;
    let isInitialLoad = true;"""

tsx = re.sub(r"    let lastBingoTs = 0;\n    let lastRoundTs = 0;", replacement, tsx)

replacement_state = """                    const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };

                    if (isInitialLoad) {
                        lastRoundTs = state.latestRoundTimestamp || 0;
                        lastBingoTs = state.latestBingoTimestamp || 0;
                        (window as any).lastDrawnPrizeCount = (state.drawnPrizeNumbers || []).length;
                        isInitialLoad = false;
                    }

                    if (state.latestRoundTimestamp && state.latestRoundTimestamp !== lastRoundTs) {"""

tsx = re.sub(
    r"                    const labels = state\.appLabels \|\| \{ prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' \};\n\n                    if \(state\.latestRoundTimestamp && state\.latestRoundTimestamp !== lastRoundTs && lastRoundTs !== 0\) \{",
    replacement_state,
    tsx
)

tsx = re.sub(
    r"if \(state\.latestBingoTimestamp && state\.latestBingoTimestamp !== lastBingoTs && lastBingoTs !== 0\) \{",
    r"if (state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs) {",
    tsx
)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
