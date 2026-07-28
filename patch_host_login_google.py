import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """                                <div class="flex flex-col sm:flex-row gap-3 mb-4">
                                    <button id="host-login-facebook-btn" class="flex items-center justify-center gap-2 bg-[#1877F2] text-white hover:bg-[#166FE5] py-2 px-4 rounded-lg font-bold transition-colors shadow-sm">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                                        Logar Facebook
                                    </button>
                                    <button id="host-logout-btn" class="hidden flex items-center justify-center gap-2 bg-red-600 text-white hover:bg-red-700 py-2 px-4 rounded-lg font-bold transition-colors shadow-sm">
                                        Desconectar
                                    </button>
                                </div>"""

new_code = """                                <div class="flex flex-col sm:flex-row gap-3 mb-4">
                                    <button id="host-login-facebook-btn" class="flex items-center justify-center gap-2 bg-[#1877F2] text-white hover:bg-[#166FE5] py-2 px-4 rounded-lg font-bold transition-colors shadow-sm">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                                        Logar Facebook
                                    </button>
                                    <button id="host-login-google-btn" class="flex items-center justify-center gap-2 bg-white text-gray-700 border border-gray-300 hover:bg-gray-50 py-2 px-4 rounded-lg font-bold transition-colors shadow-sm">
                                        <svg class="w-5 h-5" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
                                        Logar Google
                                    </button>
                                    <button id="host-logout-btn" class="hidden flex items-center justify-center gap-2 bg-red-600 text-white hover:bg-red-700 py-2 px-4 rounded-lg font-bold transition-colors shadow-sm">
                                        Desconectar
                                    </button>
                                </div>"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch UI Google successful!")
else:
    print("Old UI Google code not found!")

old_code_2 = """    const updateHostAuthUI = () => {
        const loginBtn = document.getElementById('host-login-facebook-btn');
        const logoutBtn = document.getElementById('host-logout-btn');
        const userInfo = document.getElementById('host-user-info');
        
        if (firebaseUser && !firebaseUser.isAnonymous) {
            if (loginBtn) loginBtn.classList.add('hidden');
            if (logoutBtn) logoutBtn.classList.remove('hidden');"""

new_code_2 = """    const updateHostAuthUI = () => {
        const loginBtn = document.getElementById('host-login-facebook-btn');
        const loginGoogleBtn = document.getElementById('host-login-google-btn');
        const logoutBtn = document.getElementById('host-logout-btn');
        const userInfo = document.getElementById('host-user-info');
        
        if (firebaseUser && !firebaseUser.isAnonymous) {
            if (loginBtn) loginBtn.classList.add('hidden');
            if (loginGoogleBtn) loginGoogleBtn.classList.add('hidden');
            if (logoutBtn) logoutBtn.classList.remove('hidden');"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch UI Google auth 1 successful!")
else:
    print("Old UI Google auth 1 code not found!")

old_code_3 = """        } else {
            if (loginBtn) loginBtn.classList.remove('hidden');
            if (logoutBtn) logoutBtn.classList.add('hidden');
            if (userInfo) userInfo.classList.add('hidden');
        }
    };"""

new_code_3 = """        } else {
            if (loginBtn) loginBtn.classList.remove('hidden');
            if (loginGoogleBtn) loginGoogleBtn.classList.remove('hidden');
            if (logoutBtn) logoutBtn.classList.add('hidden');
            if (userInfo) userInfo.classList.add('hidden');
        }
    };"""

if old_code_3 in content:
    content = content.replace(old_code_3, new_code_3)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch UI Google auth 2 successful!")
else:
    print("Old UI Google auth 2 code not found!")


old_code_4 = """    document.getElementById('host-login-facebook-btn')?.addEventListener('click', async () => {
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
    });"""

new_code_4 = """    document.getElementById('host-login-facebook-btn')?.addEventListener('click', async () => {
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

    document.getElementById('host-login-google-btn')?.addEventListener('click', async () => {
        try {
            const provider = new GoogleAuthProvider();
            await signInWithPopup(auth, provider);
            // onAuthStateChanged will handle the rest
            updateHostAuthUI();
            showAlert("Login com Google realizado com sucesso!");
        } catch (e: any) {
            console.error("Login Google Host erro:", e);
            showAlert("Erro ao logar com Google: " + (e.message || String(e)));
        }
    });"""

if old_code_4 in content:
    content = content.replace(old_code_4, new_code_4)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch UI Google auth 3 successful!")
else:
    print("Old UI Google auth 3 code not found!")
