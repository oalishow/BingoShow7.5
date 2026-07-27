import re

with open("attendee.tsx") as f:
    tsx = f.read()

# Define the elements
tsx = tsx.replace(
    "const overlayEl = document.getElementById('attendee-overlay')!;",
    "const overlayEl = document.getElementById('attendee-overlay')!;\n    const bingoOverlayEl = document.getElementById('attendee-bingo-overlay')!;\n    const bingoOverlayTitleEl = document.getElementById('bingo-overlay-title')!;\n    const bingoOverlayMsgEl = document.getElementById('bingo-overlay-msg')!;"
)

# Update the Bingo logic
bingo_logic_old = """                            overlayTitleEl.textContent = "BINGO!";
                            overlayMsgEl.innerHTML = `<span class="text-2xl font-black text-slate-800 dark:text-white">${lastWinner.name}</span><br/><span class="text-lg text-yellow-300 font-bold mt-2 block">${lastWinner.prize}</span>`;
                            overlayEl.classList.remove("hidden");
                            overlayEl.classList.add("flex");
                            setTimeout(() => {
                                overlayEl.classList.add("hidden");
                                overlayEl.classList.remove("flex");
                            }, 8000);"""

bingo_logic_new = """                            bingoOverlayMsgEl.innerHTML = `<span class="text-3xl font-black text-slate-800 dark:text-white">${lastWinner.name}</span><br/><span class="text-2xl text-yellow-500 dark:text-yellow-400 font-bold mt-3 block">${lastWinner.prize}</span>`;
                            bingoOverlayEl.classList.remove("hidden");
                            bingoOverlayEl.classList.add("flex");
                            setTimeout(() => {
                                bingoOverlayEl.classList.add("hidden");
                                bingoOverlayEl.classList.remove("flex");
                            }, 8000);"""

tsx = tsx.replace(bingo_logic_old, bingo_logic_new)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
