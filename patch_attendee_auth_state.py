import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """import { getAuth, signInAnonymously, GoogleAuthProvider, FacebookAuthProvider, signInWithPopup } from 'firebase/auth';"""

new_code = """import { getAuth, signInAnonymously, GoogleAuthProvider, FacebookAuthProvider, signInWithPopup, onAuthStateChanged, signOut } from 'firebase/auth';"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee imports successful!")
else:
    print("Old attendee imports not found!")

old_code_2 = """    let attendeeAuthenticated = false;
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

new_code_2 = """    let attendeeAuthenticated = false;
    let attendeeUserData: any = null;
    const logoutBtn = document.getElementById('attendee-logout-btn');
    
    onAuthStateChanged(auth, (user) => {
        if (user && !user.isAnonymous) {
            attendeeAuthenticated = true;
            attendeeUserData = user;
            if (logoutBtn) logoutBtn.classList.remove('hidden');
            
            const currentTitle = (window as any).currentBingoTitle === 'AJUDE' ? '🔔 BATI AJUDE!' : '🔔 BATI BINGO!';
            if (shoutBingoBtn) shoutBingoBtn.innerHTML = currentTitle;
        } else {
            attendeeAuthenticated = false;
            attendeeUserData = null;
            if (logoutBtn) logoutBtn.classList.add('hidden');
            const currentTitle = (window as any).currentBingoTitle === 'AJUDE' ? '🚨 BATI AJUDE!' : '🚨 BINGO!';
            if (shoutBingoBtn) shoutBingoBtn.innerHTML = currentTitle;
        }
    });
    
    if (logoutBtn) {
        logoutBtn.addEventListener('click', async () => {
            if (confirm("Deseja realmente desconectar sua conta? Você precisará entrar novamente para gritar BINGO.")) {
                try {
                    await signOut(auth);
                    await signInAnonymously(auth);
                    alert("Conta desconectada.");
                } catch (e) {
                    console.error("Erro ao desconectar", e);
                }
            }
        });
    }"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee auth state successful!")
else:
    print("Old attendee auth state not found!")
