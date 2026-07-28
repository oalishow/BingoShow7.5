import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                        const newlyDrawn = drawnPrizes[drawnPrizes.length - 1];
                        
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
                        
                        if ((window as any)._raffleTimeout) clearTimeout((window as any)._raffleTimeout);
                        (window as any)._raffleTimeout = setTimeout(() => {
                            if (overlayIconEl.textContent === "🎁") {
                                overlayEl.classList.add("hidden");
                                overlayEl.classList.remove("flex");
                                overlayMsgEl.style.fontSize = ""; // reset
                                overlayMsgEl.style.color = ""; // reset
                            }
                        }, 8000); // Show for 8 seconds"""

new_code = """                        const newlyDrawn = drawnPrizes[drawnPrizes.length - 1];
                        
                        const overlayIconEl = document.getElementById('overlay-icon')!;
                        const overlayTitleEl = document.getElementById('overlay-title')!;
                        const overlayMsgEl = document.getElementById('overlay-msg')!;
                        const overlayEl = document.getElementById('attendee-overlay')!;
                        
                        if ((window as any)._raffleDelayTimeout) clearTimeout((window as any)._raffleDelayTimeout);
                        
                        (window as any)._raffleDelayTimeout = setTimeout(() => {
                            overlayIconEl.textContent = "🎁";
                            overlayTitleEl.textContent = "Cartela Sorteada!";
                            overlayMsgEl.textContent = "Nº " + newlyDrawn;
                            
                            // Increase font size for emphasis
                            overlayMsgEl.style.fontSize = "4rem";
                            overlayMsgEl.style.color = "#f59e0b"; // amber-500
                            
                            overlayEl.classList.remove("hidden");
                            overlayEl.classList.add("flex");
                            
                            if ((window as any)._raffleTimeout) clearTimeout((window as any)._raffleTimeout);
                            (window as any)._raffleTimeout = setTimeout(() => {
                                if (overlayIconEl.textContent === "🎁") {
                                    overlayEl.classList.add("hidden");
                                    overlayEl.classList.remove("flex");
                                    overlayMsgEl.style.fontSize = ""; // reset
                                    overlayMsgEl.style.color = ""; // reset
                                }
                            }, 8000); // Show for 8 seconds
                        }, 4000); // Delay 4 seconds"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch delay successful!")
else:
    print("Old code not found!")
