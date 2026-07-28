import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                        overlayEl.classList.remove("hidden");
                        overlayEl.classList.add("flex");
                        
                        // Play winner sound if needed, but attendee usually doesn't have sounds enabled automatically unless interacted with.
                        
                        setTimeout(() => {
                            overlayEl.classList.add("hidden");
                            overlayEl.classList.remove("flex");
                            overlayMsgEl.style.fontSize = ""; // reset
                            overlayMsgEl.style.color = ""; // reset
                        }, 8000); // Show for 8 seconds"""

new_code = """                        overlayEl.classList.remove("hidden");
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

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch timeout successful!")
else:
    print("Old timeout code not found!")
