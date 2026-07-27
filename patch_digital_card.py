import re

with open("index.tsx") as f:
    content = f.read()

replacement = """                        let lastActiveGame = '';
                        // Watch event
                        onSnapshot(doc(db, "events", cardEventId), (docSnap) => {
                           if (docSnap.exists()) {
                               const eventData = docSnap.data();
                               document.getElementById('digital-app-name')!.textContent = eventData.appName || "Bingo Show";
                               if (eventData.bingoTitle) {
                                   document.getElementById('digital-bingo-title')!.textContent = eventData.bingoTitle;
                               }
                               
                               const activeGame = eventData.activeGameNumber;
                               const statusBanner = document.getElementById('realtime-status-banner')!;
                               
                               if (activeGame !== lastActiveGame) {
                                   lastActiveGame = activeGame;
                                   
                                   if (activeGame) {
                                       statusBanner.className = "w-full max-w-md mt-16 p-2 text-center text-sm font-bold bg-green-800 text-green-100 rounded shadow";
                                       statusBanner.innerHTML = `🟢 Rodada Ativa! Carregando sincronização...`;
                                       (window as any).currentActiveGame = activeGame;
                                       
                                       // Unsub previous game listeners
                                       if ((window as any).currentGameUnsub) {
                                           (window as any).currentGameUnsub();
                                       }
                                       
                                       // Watch active game
                                       (window as any).currentGameUnsub = onSnapshot(doc(db, `events/${cardEventId}/games`, activeGame), (gameSnap) => {"""

old_code = """                        // Watch event
                        onSnapshot(doc(db, "events", cardEventId), (docSnap) => {
                           if (docSnap.exists()) {
                               const eventData = docSnap.data();
                               document.getElementById('digital-app-name')!.textContent = eventData.appName || "Bingo Show";
                               if (eventData.bingoTitle) {
                                   document.getElementById('digital-bingo-title')!.textContent = eventData.bingoTitle;
                               }
                               
                               const activeGame = eventData.activeGameNumber;
                               const statusBanner = document.getElementById('realtime-status-banner')!;
                               if (activeGame) {
                                   statusBanner.className = "w-full max-w-md mt-16 p-2 text-center text-sm font-bold bg-green-800 text-green-100 rounded shadow";
                                   statusBanner.innerHTML = `🟢 Rodada Ativa! Carregando sincronização...`;
                                   (window as any).currentActiveGame = activeGame;
                                   
                                   // Unsub previous game listeners
                                   if ((window as any).currentGameUnsub) {
                                       (window as any).currentGameUnsub();
                                   }
                                   
                                   // Watch active game
                                   (window as any).currentGameUnsub = onSnapshot(doc(db, `events/${cardEventId}/games`, activeGame), (gameSnap) => {"""

content = content.replace(old_code, replacement)

with open("index.tsx", "w") as f:
    f.write(content)
