import re

with open("attendee.tsx") as f:
    content = f.read()

# We need to replace `const lastWinner = game.winners && game.winners.length > 0 ? game.winners[game.winners.length - 1] : null;`
replacement = """
                        let lastWinner = null;
                        if (state.gamesData) {
                            const allWinners = Object.values(state.gamesData).flatMap((g: any) => g.winners || []);
                            if (allWinners.length > 0) {
                                allWinners.sort((a, b) => a.id - b.id);
                                lastWinner = allWinners[allWinners.length - 1];
                            }
                        }
"""

content = re.sub(r'const lastWinner = game\.winners && game\.winners\.length > 0 \? game\.winners\[game\.winners\.length - 1\] : null;', replacement, content)

# Also fix `overlayIconEl.innerHTML = "🏆";` which should not be there or should be bingoOverlayTitleEl
content = content.replace('overlayIconEl.innerHTML = "🏆";', '')

with open("attendee.tsx", "w") as f:
    f.write(content)
