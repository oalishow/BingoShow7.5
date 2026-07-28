import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """               (window as any).masterBingoClaimsUnsub = onSnapshot(claimsRef, (snapshot) => {
                   if (initialLoad) {
                       initialLoad = false;
                       return;
                   }
                   snapshot.docChanges().forEach((change) => {
                       if (change.type === 'added') {
                           const docData = change.doc.data();
                           showBingoClaimNotification(docData.series, docData.uuid, gameNumber, docData);
                       }
                   });
               });"""

new_code = """               (window as any).masterBingoClaimsUnsub = onSnapshot(claimsRef, (snapshot) => {
                   if (initialLoad) {
                       initialLoad = false;
                       return;
                   }
                   snapshot.docChanges().forEach((change) => {
                       if (change.type === 'added') {
                           const docData = change.doc.data();
                           if (!appStore.state.blockedUsers.includes(docData.uuid)) {
                               showBingoClaimNotification(docData.series, docData.uuid, gameNumber, docData);
                           }
                       }
                   });
               });"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch check blocked users successful!")
else:
    print("Old check blocked users not found!")

old_code_2 = """        function showBingoClaimNotification(series: number, uuid: string, gameNumber: string, docData?: any) {
            const audio = new Audio('/bingo-alert.mp3');
            audio.play().catch(e => console.log('Audio blocked', e));"""

new_code_2 = """        (window as any).blockUser = (uuid: string) => {
            if (!appStore.state.blockedUsers.includes(uuid)) {
                appStore.state.blockedUsers.push(uuid);
                appStore.debouncedSave();
                showAlert("Usuário bloqueado com sucesso. Ele não poderá mais enviar alertas de BINGO.");
                updateBlockedUsersUI();
            }
        };

        function showBingoClaimNotification(series: number, uuid: string, gameNumber: string, docData?: any) {
            const audio = new Audio('/bingo-alert.mp3');
            audio.play().catch(e => console.log('Audio blocked', e));"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch window.blockUser successful!")
else:
    print("Old window.blockUser not found!")

old_code_3 = """                    <button class="bg-white text-green-700 hover:bg-gray-100 py-3 mt-1 w-full rounded-lg font-bold shadow uppercase transition-all active:scale-95" onclick="this.parentElement.remove()">Verificar Física Manualmente</button>
                `;
            } else {
                el.innerHTML = `
                    <div class="flex justify-between items-center w-full">
                        <span class="text-[10px] uppercase bg-black/20 px-2 py-0.5 rounded tracking-widest">Alerta de Jogador Online</span>
                        <button class="text-white hover:text-gray-200" onclick="this.parentElement.parentElement.remove()">✕</button>
                    </div>
                    <div class="text-3xl font-black uppercase text-center mt-1 drop-shadow-md">BINGO!</div>
                    <div class="text-lg text-center mx-1 mb-1 leading-tight">A cartela nº <span class="bg-yellow-400 text-black px-2 py-1 mx-1 rounded inline-block shadow-sm">${cardStr}</span> bateu lá do celular!</div>
                    <button class="bg-white text-green-700 hover:bg-gray-100 py-3 mt-1 w-full rounded-lg font-bold shadow uppercase transition-all active:scale-95" onclick="window.pauseDrawAndVerify('${uuid}', '${cardStr}'); this.parentElement.remove()">Fazer Checagem Oficial</button>
                `;
            }"""

new_code_3 = """                    <button class="bg-white text-green-700 hover:bg-gray-100 py-3 mt-1 w-full rounded-lg font-bold shadow uppercase transition-all active:scale-95" onclick="this.parentElement.remove()">Verificar Física Manualmente</button>
                    <button class="text-white hover:text-red-200 text-xs mt-1 underline" onclick="if(confirm('Bloquear este jogador? Ele não poderá mais gritar bingo.')) { window.blockUser('${uuid}'); this.parentElement.remove(); }">Bloquear Jogador (Falso Bingo)</button>
                `;
            } else {
                el.innerHTML = `
                    <div class="flex justify-between items-center w-full">
                        <span class="text-[10px] uppercase bg-black/20 px-2 py-0.5 rounded tracking-widest">Alerta de Jogador Online</span>
                        <button class="text-white hover:text-gray-200" onclick="this.parentElement.parentElement.remove()">✕</button>
                    </div>
                    <div class="text-3xl font-black uppercase text-center mt-1 drop-shadow-md">BINGO!</div>
                    <div class="text-lg text-center mx-1 mb-1 leading-tight">A cartela nº <span class="bg-yellow-400 text-black px-2 py-1 mx-1 rounded inline-block shadow-sm">${cardStr}</span> bateu lá do celular!</div>
                    <button class="bg-white text-green-700 hover:bg-gray-100 py-3 mt-1 w-full rounded-lg font-bold shadow uppercase transition-all active:scale-95" onclick="window.pauseDrawAndVerify('${uuid}', '${cardStr}'); this.parentElement.remove()">Fazer Checagem Oficial</button>
                    <button class="text-white hover:text-red-200 text-xs mt-1 underline" onclick="if(confirm('Bloquear este jogador? Ele não poderá mais gritar bingo.')) { window.blockUser('${uuid}'); this.parentElement.remove(); }">Bloquear Jogador (Falso Bingo)</button>
                `;
            }"""

if old_code_3 in content:
    content = content.replace(old_code_3, new_code_3)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch notification block btn successful!")
else:
    print("Old notification block btn not found!")

