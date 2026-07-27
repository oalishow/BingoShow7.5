import re

with open("index.tsx") as f:
    content = f.read()

replacement = """    let lastRenderedStateStr = '';

            onSnapshot(doc(db, "events", targetEventId), (docSnap) => {
                if (docSnap.exists()) {
                    const eventData = docSnap.data();
                    if (eventData.appName) appNameEl.textContent = eventData.appName;
                    
                    if (!eventData.activeGameNumber) {
                        statusBanner.className = "w-full p-2 text-center text-sm font-bold bg-slate-800 text-yellow-400 rounded shadow animate-pulse";
                        statusBanner.innerHTML = `⏳ Aguardando próxima rodada...`;
                        boardContainer.classList.add('hidden');
                        lastRenderedStateStr = ''; // reset on no active game
                        return;
                    }
                    
                    statusBanner.classList.add('hidden');
                    boardContainer.classList.remove('hidden');
                    boardContainer.classList.add('flex');
                    
                    // Parse fullStateJSON to get current board state and config
                    if (eventData.fullStateJSON) {
                        try {
                            const state = JSON.parse(eventData.fullStateJSON);
                            const game = state.gamesData[eventData.activeGameNumber];
                            const config = state.appConfig;

                            // Otimização: Apenas atualiza a UI se os campos críticos mudarem
                            const criticalState = {
                                activeGame: eventData.activeGameNumber,
                                called: game ? game.calledNumbers : [],
                                auctionBid: config.auctionBid,
                                auctionItem: config.auctionItemName,
                                auctionWinner: config.auctionWinnerName,
                                pending: state.pendingNumber,
                                bingoTs: state.latestBingoTimestamp,
                                roundTs: state.latestRoundTimestamp,
                                gameName: game ? game.name : '',
                                appName: eventData.appName,
                                boardColor: config.boardColor
                            };
                            const currentStateStr = JSON.stringify(criticalState);
                            if (lastRenderedStateStr === currentStateStr) {
                                return; // Nenhuma mudança crítica, ignora re-render
                            }
                            lastRenderedStateStr = currentStateStr;"""

old_code = """            onSnapshot(doc(db, "events", targetEventId), (docSnap) => {
                if (docSnap.exists()) {
                    const eventData = docSnap.data();
                    if (eventData.appName) appNameEl.textContent = eventData.appName;
                    
                    if (!eventData.activeGameNumber) {
                        statusBanner.className = "w-full p-2 text-center text-sm font-bold bg-slate-800 text-yellow-400 rounded shadow animate-pulse";
                        statusBanner.innerHTML = `⏳ Aguardando próxima rodada...`;
                        boardContainer.classList.add('hidden');
                        return;
                    }
                    
                    statusBanner.classList.add('hidden');
                    boardContainer.classList.remove('hidden');
                    boardContainer.classList.add('flex');
                    
                    // Parse fullStateJSON to get current board state and config
                    if (eventData.fullStateJSON) {
                        try {
                            const state = JSON.parse(eventData.fullStateJSON);
                            const game = state.gamesData[eventData.activeGameNumber];
                            const config = state.appConfig;"""

content = content.replace(old_code, replacement)

with open("index.tsx", "w") as f:
    f.write(content)
