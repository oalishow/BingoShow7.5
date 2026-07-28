import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """        shoutBingoBtn.addEventListener('click', () => {
            if (!attendeeAuthenticated) {
                authModal?.classList.remove('hidden');
                authModal?.classList.add('flex');
            } else {
                sendBingoClaim();
            }
        });"""

new_code = """        shoutBingoBtn.addEventListener('click', () => {
            if (!attendeeAuthenticated) {
                authModal?.classList.remove('hidden');
                authModal?.classList.add('flex');
            } else {
                if (confirm("Você tem certeza que quer gritar BINGO? Evite toques acidentais para não atrapalhar o andamento do jogo.")) {
                    sendBingoClaim();
                }
            }
        });"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee confirm successful!")
else:
    print("Old attendee confirm not found!")
