import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """    (window as any).blockUser = (uuid: string) => {
            if (!appStore.state.blockedUsers.includes(uuid)) {
                appStore.state.blockedUsers.push(uuid);
                appStore.debouncedSave();
                showAlert("Usuário bloqueado com sucesso. Ele não poderá mais enviar alertas de BINGO.");
                updateBlockedUsersUI();
            }
        };"""

new_code = """    (window as any).unblockUser = (uuid: string) => {
            appStore.state.blockedUsers = appStore.state.blockedUsers.filter((u: string) => u !== uuid);
            appStore.debouncedSave();
            showAlert("Usuário desbloqueado com sucesso.");
            updateBlockedUsersUI();
        };
        
        function updateBlockedUsersUI() {
            const listEl = document.getElementById('blocked-users-list');
            if (!listEl) return;
            
            if (appStore.state.blockedUsers.length === 0) {
                listEl.innerHTML = '<p class="text-sm text-slate-500 italic">Nenhum usuário bloqueado.</p>';
                return;
            }
            
            listEl.innerHTML = appStore.state.blockedUsers.map((uuid: string) => `
                <div class="flex justify-between items-center bg-gray-100 dark:bg-gray-700 p-3 rounded">
                    <span class="text-sm font-mono text-gray-800 dark:text-gray-200">${uuid}</span>
                    <button class="bg-indigo-600 hover:bg-indigo-700 text-white px-3 py-1 rounded text-xs font-bold" onclick="window.unblockUser('${uuid}')">Desbloquear</button>
                </div>
            `).join('');
        }

        (window as any).blockUser = (uuid: string) => {
            if (!appStore.state.blockedUsers.includes(uuid)) {
                appStore.state.blockedUsers.push(uuid);
                appStore.debouncedSave();
                showAlert("Usuário bloqueado com sucesso. Ele não poderá mais enviar alertas de BINGO.");
                updateBlockedUsersUI();
            }
        };"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch block functions successful!")
else:
    print("Old block functions not found!")

old_code_2 = """    const tabs = ['appearance', 'sponsors', 'labels', 'shortcuts', 'security'];
    
    const switchTab = (targetTabId: string) => {"""

new_code_2 = """    const tabs = ['appearance', 'sponsors', 'labels', 'shortcuts', 'security'];
    
    const switchTab = (targetTabId: string) => {"""

old_code_3 = """    // --- Shortcuts Tab ---
    const resetCardDataBtn = document.getElementById('reset-card-data-btn');"""

new_code_3 = """    // --- Security Tab ---
    if (typeof updateBlockedUsersUI === 'function') {
        updateBlockedUsersUI();
    }

    // --- Shortcuts Tab ---
    const resetCardDataBtn = document.getElementById('reset-card-data-btn');"""

if old_code_3 in content:
    content = content.replace(old_code_3, new_code_3)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch render security tab successful!")
else:
    print("Old render security tab not found!")

