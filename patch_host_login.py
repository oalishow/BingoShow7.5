import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """    const syncToggle = document.getElementById('online-sync-toggle') as HTMLInputElement;
    syncToggle.checked = appConfig.onlineSyncEnabled === true;"""

new_code = """    const updateHostAuthUI = () => {
        const loginBtn = document.getElementById('host-login-facebook-btn');
        const logoutBtn = document.getElementById('host-logout-btn');
        const userInfo = document.getElementById('host-user-info');
        
        if (firebaseUser && !firebaseUser.isAnonymous) {
            if (loginBtn) loginBtn.classList.add('hidden');
            if (logoutBtn) logoutBtn.classList.remove('hidden');
            if (userInfo) {
                userInfo.textContent = `Logado como: ${firebaseUser.displayName || 'Usuário'} (${firebaseUser.email || 'N/A'})`;
                userInfo.classList.remove('hidden');
            }
        } else {
            if (loginBtn) loginBtn.classList.remove('hidden');
            if (logoutBtn) logoutBtn.classList.add('hidden');
            if (userInfo) userInfo.classList.add('hidden');
        }
    };
    
    updateHostAuthUI();
    
    document.getElementById('host-login-facebook-btn')?.addEventListener('click', async () => {
        try {
            const provider = new FacebookAuthProvider();
            await signInWithPopup(auth, provider);
            // onAuthStateChanged will handle the rest
            updateHostAuthUI();
            showAlert("Login com Facebook realizado com sucesso!");
        } catch (e: any) {
            console.error("Login Facebook Host erro:", e);
            showAlert("Erro ao logar com Facebook: " + (e.message || String(e)));
        }
    });

    document.getElementById('host-logout-btn')?.addEventListener('click', async () => {
        try {
            await signOut(auth);
            await signInAnonymously(auth); // re-authenticate as anonymous
            updateHostAuthUI();
            showAlert("Desconectado com sucesso.");
        } catch (e: any) {
            console.error("Logout erro:", e);
            showAlert("Erro ao desconectar.");
        }
    });

    const syncToggle = document.getElementById('online-sync-toggle') as HTMLInputElement;
    syncToggle.checked = appConfig.onlineSyncEnabled === true;"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch auth JS successful!")
else:
    print("Old JS code not found!")
