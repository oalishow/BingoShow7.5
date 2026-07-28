import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                        if (isVerifyingState) {
                            overlayIconEl.textContent = "🔍";
                            overlayTitleEl.textContent = "Aguardando conferência...";
                            overlayMsgEl.textContent = "Verificando as cartelas chamadas";
                            overlayEl.classList.remove("hidden");
                            overlayEl.classList.add("flex");"""

new_code = """                        if (isVerifyingState) {
                            overlayIconEl.textContent = "🔍";
                            overlayTitleEl.textContent = "Aguardando conferência...";
                            overlayMsgEl.textContent = "Verificando as cartelas chamadas";
                            overlayMsgEl.style.fontSize = ""; // reset
                            overlayMsgEl.style.color = ""; // reset
                            overlayEl.classList.remove("hidden");
                            overlayEl.classList.add("flex");"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch verifying reset successful!")
else:
    print("Old verifying reset code not found!")
