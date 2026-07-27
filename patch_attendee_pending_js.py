import re

with open("attendee.tsx") as f:
    tsx = f.read()

# in onSnapshot logic
# find: "if (state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs) {"
replacement = """
                    // Handle Pending Number
                    const pendingOverlay = document.getElementById('attendee-pending-overlay')!;
                    const pendingMsg = document.getElementById('pending-overlay-msg')!;
                    if (state.pendingNumber) {
                        const letter = getLetterForNumber(state.pendingNumber);
                        pendingMsg.innerHTML = `<span class="text-4xl block mb-2">${letter}</span><span>${state.pendingNumber}</span>`;
                        if (game && game.color) {
                            pendingMsg.style.color = game.color;
                        } else {
                            pendingMsg.style.color = '';
                        }
                        pendingOverlay.classList.remove('hidden');
                        pendingOverlay.classList.add('flex');
                    } else {
                        pendingOverlay.classList.add('hidden');
                        pendingOverlay.classList.remove('flex');
                    }

                    if (state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs) {"""

tsx = tsx.replace("                    if (state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs) {", replacement)

# ensure getLetterForNumber is available in attendee.tsx
get_letter_func = """function getLetterForNumber(number: number): string {
    if (number >= 1 && number <= 15) return 'B';
    if (number >= 16 && number <= 30) return 'I';
    if (number >= 31 && number <= 45) return 'N';
    if (number >= 46 && number <= 60) return 'G';
    if (number >= 61 && number <= 75) return 'O';
    return '';
}

"""
# just prepend it if it's not there
if "function getLetterForNumber" not in tsx:
    tsx = get_letter_func + tsx

with open("attendee.tsx", "w") as f:
    f.write(tsx)
