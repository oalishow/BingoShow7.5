import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

helpers = """// Custom Modal Helpers
function showAttendeeAlert(message: string) {
    const modal = document.getElementById('attendee-alert-modal');
    const msgEl = document.getElementById('attendee-alert-message');
    const okBtn = document.getElementById('attendee-alert-ok-btn');
    
    if (modal && msgEl && okBtn) {
        msgEl.textContent = message;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        
        const close = () => {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            okBtn.removeEventListener('click', close);
        };
        okBtn.addEventListener('click', close);
    } else {
        alert(message);
    }
}

function showAttendeeConfirm(message: string, onConfirm: () => void) {
    const modal = document.getElementById('attendee-confirm-modal');
    const msgEl = document.getElementById('attendee-confirm-message');
    const okBtn = document.getElementById('attendee-confirm-ok-btn');
    const cancelBtn = document.getElementById('attendee-confirm-cancel-btn');
    
    if (modal && msgEl && okBtn && cancelBtn) {
        msgEl.textContent = message;
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        
        const close = () => {
            modal.classList.add('hidden');
            modal.classList.remove('flex');
            okBtn.removeEventListener('click', handleOk);
            cancelBtn.removeEventListener('click', close);
        };
        
        const handleOk = () => {
            close();
            onConfirm();
        };
        
        okBtn.addEventListener('click', handleOk);
        cancelBtn.addEventListener('click', close);
    } else {
        if (confirm(message)) {
            onConfirm();
        }
    }
}

"""

if "function showAttendeeAlert" not in content:
    content = content.replace("let attendeeUserData: any = null;", helpers + "let attendeeUserData: any = null;")

# Now replace alerts and confirms
content = content.replace('alert("Conta desconectada.");', 'showAttendeeAlert("Conta desconectada.");')
content = content.replace('alert("Botão habilitado com sucesso!");', 'showAttendeeAlert("Botão habilitado com sucesso!");')
content = content.replace('alert("Erro ao fazer login: " + errorMsg);', 'showAttendeeAlert("Erro ao fazer login: " + errorMsg);')
content = content.replace('alert("Cadastro realizado com sucesso!");', 'showAttendeeAlert("Cadastro realizado com sucesso!");')
content = content.replace('alert("Preencha todos os campos e aceite os termos.");', 'showAttendeeAlert("Preencha todos os campos e aceite os termos.");')
content = content.replace('alert("ID do evento não encontrado.");', 'showAttendeeAlert("ID do evento não encontrado.");')
content = content.replace('alert("BINGO enviado para a banca! Aguarde conferência oficial.");', 'showAttendeeAlert("BINGO enviado para a banca! Aguarde conferência oficial.");')
content = content.replace('alert("Erro ao enviar BINGO: " + errMsg);', 'showAttendeeAlert("Erro ao enviar BINGO: " + errMsg);')

# Confirms
confirm_1_old = """            if (confirm("Deseja realmente desconectar sua conta? Você precisará entrar novamente para gritar BINGO.")) {
                await signOut(auth);
                attendeeAuthenticated = false;
                attendeeUserData = null;
                alert("Conta desconectada.");
                
                logoutBtn.classList.add('hidden');
                
                shoutBingoBtn.innerHTML = '🚨 BINGO!';
                shoutBingoBtn.classList.remove('from-emerald-600', 'to-green-600', 'from-amber-600', 'to-yellow-600');
                shoutBingoBtn.classList.add('from-red-600', 'to-rose-600');
                shoutBingoBtn.disabled = false;
            }"""
confirm_1_new = """            showAttendeeConfirm("Deseja realmente desconectar sua conta? Você precisará entrar novamente para gritar BINGO.", async () => {
                await signOut(auth);
                attendeeAuthenticated = false;
                attendeeUserData = null;
                showAttendeeAlert("Conta desconectada.");
                
                logoutBtn.classList.add('hidden');
                
                shoutBingoBtn.innerHTML = '🚨 BINGO!';
                shoutBingoBtn.classList.remove('from-emerald-600', 'to-green-600', 'from-amber-600', 'to-yellow-600');
                shoutBingoBtn.classList.add('from-red-600', 'to-rose-600');
                shoutBingoBtn.disabled = false;
            });"""
content = content.replace(confirm_1_old, confirm_1_new)

confirm_2_old = """        shoutBingoBtn.addEventListener('click', () => {
            if (!attendeeAuthenticated) {
                authModal?.classList.remove('hidden');
                authModal?.classList.add('flex');
            } else {
                if (confirm("Você tem certeza que quer gritar BINGO? Evite toques acidentais para não atrapalhar o andamento do jogo.")) {
                    sendBingoClaim();
                }
            }
        });"""
confirm_2_new = """        shoutBingoBtn.addEventListener('click', () => {
            if (!attendeeAuthenticated) {
                authModal?.classList.remove('hidden');
                authModal?.classList.add('flex');
            } else {
                showAttendeeConfirm("Você tem certeza que quer gritar BINGO? Evite toques acidentais para não atrapalhar o andamento do jogo.", () => {
                    sendBingoClaim();
                });
            }
        });"""
content = content.replace(confirm_2_old, confirm_2_new)

with open('attendee.tsx', 'w') as f:
    f.write(content)

print("Patch attendee.tsx successful!")
