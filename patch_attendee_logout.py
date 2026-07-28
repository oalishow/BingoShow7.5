import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

confirm_old = """        logoutBtn.addEventListener('click', async () => {
            if (confirm("Deseja realmente desconectar sua conta? Você precisará entrar novamente para gritar BINGO.")) {
                try {
                    await signOut(auth);
                    await signInAnonymously(auth);
                    showAttendeeAlert("Conta desconectada.");
                } catch (e) {
                    console.error("Erro ao desconectar", e);
                }
            }
        });"""

confirm_new = """        logoutBtn.addEventListener('click', async () => {
            showAttendeeConfirm("Deseja realmente desconectar sua conta? Você precisará entrar novamente para gritar BINGO.", async () => {
                try {
                    await signOut(auth);
                    await signInAnonymously(auth);
                    showAttendeeAlert("Conta desconectada.");
                } catch (e) {
                    console.error("Erro ao desconectar", e);
                }
            });
        });"""

if confirm_old in content:
    content = content.replace(confirm_old, confirm_new)
    print("Patch attendee logout successful!")
else:
    print("Old attendee logout not found!")

with open('attendee.tsx', 'w') as f:
    f.write(content)
