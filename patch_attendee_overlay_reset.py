import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                                overlayTitleEl.textContent = "Nova Rodada";
                                overlayMsgEl.textContent = game ? (game.name || `Rodada ${eventData.activeGameNumber}`) : `Rodada ${eventData.activeGameNumber}`;
                                overlayEl.classList.remove("hidden");
                                overlayEl.classList.add("flex");"""

new_code = """                                overlayTitleEl.textContent = "Nova Rodada";
                                overlayMsgEl.textContent = game ? (game.name || `Rodada ${eventData.activeGameNumber}`) : `Rodada ${eventData.activeGameNumber}`;
                                overlayMsgEl.style.fontSize = ""; // reset
                                overlayMsgEl.style.color = ""; // reset
                                overlayEl.classList.remove("hidden");
                                overlayEl.classList.add("flex");"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch reset successful!")
else:
    print("Old reset code not found!")
