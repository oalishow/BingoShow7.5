import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                    // Drawn Cartelas
                    const drawnPrizes = state.drawnPrizeNumbers || [];
                    if (drawnPrizes.length > ((window as any).lastDrawnPrizeCount || 0)) {
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                    }"""

new_code = """                    // Drawn Cartelas
                    const drawnPrizes = state.drawnPrizeNumbers || [];
                    if (drawnPrizes.length > ((window as any).lastDrawnPrizeCount || 0)) {
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                        
                        const newlyDrawn = drawnPrizes[drawnPrizes.length - 1];
                        
                        const overlayIconEl = document.getElementById('overlay-icon')!;
                        const overlayTitleEl = document.getElementById('overlay-title')!;
                        const overlayMsgEl = document.getElementById('overlay-msg')!;
                        const overlayEl = document.getElementById('attendee-overlay')!;
                        
                        overlayIconEl.textContent = "🎁";
                        overlayTitleEl.textContent = "Cartela Sorteada!";
                        overlayMsgEl.textContent = "Nº " + newlyDrawn;
                        
                        // Increase font size for emphasis
                        overlayMsgEl.style.fontSize = "4rem";
                        overlayMsgEl.style.color = "#f59e0b"; // amber-500
                        
                        overlayEl.classList.remove("hidden");
                        overlayEl.classList.add("flex");
                        
                        // Play winner sound if needed, but attendee usually doesn't have sounds enabled automatically unless interacted with.
                        
                        setTimeout(() => {
                            overlayEl.classList.add("hidden");
                            overlayEl.classList.remove("flex");
                            overlayMsgEl.style.fontSize = ""; // reset
                            overlayMsgEl.style.color = ""; // reset
                        }, 8000); // Show for 8 seconds
                    }"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch successful!")
else:
    print("Old code not found!")
