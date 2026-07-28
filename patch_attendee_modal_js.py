import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """    const closeAuthBtn = document.getElementById('close-auth-btn');
    const loginGoogleBtn = document.getElementById('login-google-btn');
    const loginFacebookBtn = document.getElementById('login-facebook-btn');
    const authProvidersSection = document.getElementById('auth-providers-section');
    const cpfSection = document.getElementById('cpf-section');
    const cpfInput = document.getElementById('auth-cpf-input') as HTMLInputElement;
    const lgpdCheckbox = document.getElementById('lgpd-consent-checkbox') as HTMLInputElement;
    const confirmAuthBtn = document.getElementById('confirm-auth-btn') as HTMLButtonElement;"""

new_code = """    const closeAuthBtn = document.getElementById('close-auth-btn');
    const loginGoogleBtn = document.getElementById('login-google-btn');
    const registerAnonBtn = document.getElementById('register-anon-btn');
    const authProvidersSection = document.getElementById('auth-providers-section');
    const cpfSection = document.getElementById('cpf-section');
    const nameInput = document.getElementById('auth-name-input') as HTMLInputElement;
    const cpfInput = document.getElementById('auth-cpf-input') as HTMLInputElement;
    const lgpdCheckbox = document.getElementById('lgpd-consent-checkbox') as HTMLInputElement;
    const confirmAuthBtn = document.getElementById('confirm-auth-btn') as HTMLButtonElement;"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee elements successful!")
else:
    print("Old attendee elements not found!")

old_code_2 = """    loginGoogleBtn?.addEventListener('click', () => handleLogin(new GoogleAuthProvider()));
    loginFacebookBtn?.addEventListener('click', () => handleLogin(new FacebookAuthProvider()));

    const checkFormValidity = () => {
        if (cpfInput.value.length === 14 && lgpdCheckbox.checked) {
            authProvidersSection?.classList.remove('opacity-50', 'pointer-events-none');
        } else {
            authProvidersSection?.classList.add('opacity-50', 'pointer-events-none');
        }
    };"""

new_code_2 = """    loginGoogleBtn?.addEventListener('click', () => handleLogin(new GoogleAuthProvider()));
    
    registerAnonBtn?.addEventListener('click', () => {
        if (nameInput.value.trim().length > 0 && cpfInput.value.length === 14 && lgpdCheckbox.checked) {
            attendeeAuthenticated = true;
            attendeeUserData = {
                uid: 'anon-' + Math.random().toString(36).substring(2, 9),
                isAnonymous: true, // We treat it as pseudo-authenticated for UI, real anonymous auth is active
                displayName: nameInput.value.trim(),
                cpf: cpfInput.value
            };
            authModal?.classList.add('hidden');
            authModal?.classList.remove('flex');
            if (logoutBtn) logoutBtn.classList.remove('hidden');
            
            const currentTitle = (window as any).currentBingoTitle === 'AJUDE' ? '🔔 BATI AJUDE!' : '🔔 BATI BINGO!';
            if (shoutBingoBtn) shoutBingoBtn.innerHTML = currentTitle;
            alert("Cadastro realizado com sucesso!");
        } else {
            alert("Preencha todos os campos e aceite os termos.");
        }
    });

    const checkFormValidity = () => {
        if (cpfInput.value.length === 14 && lgpdCheckbox.checked && nameInput.value.trim().length > 0) {
            authProvidersSection?.classList.remove('opacity-50', 'pointer-events-none');
        } else {
            authProvidersSection?.classList.add('opacity-50', 'pointer-events-none');
        }
    };
    
    nameInput?.addEventListener('input', checkFormValidity);"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee form successful!")
else:
    print("Old attendee form not found!")

old_code_3 = """            await addDoc(claimsRef, {
                uuid: 'public-' + attendeeUserData.uid,
                series: 0,
                name: attendeeUserData.displayName || 'Público',
                cpf: cpfInput?.value || '',
                timestamp: Date.now()
            });"""

new_code_3 = """            await addDoc(claimsRef, {
                uuid: 'public-' + attendeeUserData.uid,
                series: 0,
                name: attendeeUserData.displayName || 'Público',
                cpf: attendeeUserData.cpf || cpfInput?.value || '',
                timestamp: Date.now()
            });"""

if old_code_3 in content:
    content = content.replace(old_code_3, new_code_3)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee claim successful!")
else:
    print("Old attendee claim not found!")

