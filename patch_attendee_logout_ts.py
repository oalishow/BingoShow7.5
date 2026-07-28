import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """    let attendeeAuthenticated = false;
    let attendeeUserData: any = null;"""

new_code = """    let attendeeAuthenticated = false;
    let attendeeUserData: any = null;
    const logoutBtn = document.getElementById('attendee-logout-btn');
    
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            if (confirm("Deseja realmente desconectar sua conta? Você precisará entrar novamente para gritar BINGO.")) {
                attendeeAuthenticated = false;
                attendeeUserData = null;
                logoutBtn.classList.add('hidden');
                
                const currentTitle = (window as any).currentBingoTitle === 'AJUDE' ? '🚨 BATI AJUDE!' : '🚨 BINGO!';
                if (shoutBingoBtn) shoutBingoBtn.innerHTML = currentTitle;
                
                // Re-authenticate anonymously to keep listening to the round
                try {
                    await signInAnonymously(auth);
                } catch (e) {
                    console.error("Erro ao reconectar anonimamente", e);
                }
                alert("Conta desconectada.");
            }
        });
    }"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch auth successful!")
else:
    print("Old auth code not found!")

old_code_2 = """            attendeeAuthenticated = true;
            authModal?.classList.add('hidden');
            authModal?.classList.remove('flex');
            alert("Botão habilitado com sucesso!");"""

new_code_2 = """            attendeeAuthenticated = true;
            authModal?.classList.add('hidden');
            authModal?.classList.remove('flex');
            if (logoutBtn) logoutBtn.classList.remove('hidden');
            alert("Botão habilitado com sucesso!");"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch login successful!")
else:
    print("Old login code not found!")
