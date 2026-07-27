import re

with open("attendee.tsx") as f:
    content = f.read()

replacement = """    let lastRenderedStateStr = '';

    onSnapshot(doc(db, "events", targetEventId), (docSnap) => {
        if (docSnap.exists()) {
            const eventData = docSnap.data();
            
            if (!eventData.activeGameNumber) {
                statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-yellow-900/50 text-yellow-200 rounded-xl shadow-sm border border-yellow-700/50 animate-pulse";
                statusBanner.innerHTML = `⏳ Aguardando próxima rodada...`;
                contentContainer.classList.add('hidden');
                statusBanner.classList.remove('hidden');
                lastRenderedStateStr = ''; // reset on no active game
                return;
            }
            
            statusBanner.classList.add('hidden');
            contentContainer.classList.remove('hidden');
            contentContainer.classList.add('flex');
            
            if (eventData.fullStateJSON) {
                try {
                    const state = JSON.parse(eventData.fullStateJSON);
                    const game = state.gamesData[eventData.activeGameNumber];
                    const config = state.appConfig;

                    // Otimização: Apenas atualiza a UI se os campos críticos mudarem
                    const criticalState = {
                        activeGame: eventData.activeGameNumber,
                        called: game ? game.calledNumbers : [],
                        winners: game ? game.winners : [],
                        drawnPrizes: state.drawnPrizeNumbers || [],
                        auctionBid: config.auctionBid,
                        auctionItem: config.auctionItemName,
                        auctionWinner: config.auctionWinnerName,
                        isVerifying: state.isVerifying,
                        pending: state.pendingNumber,
                        bingoTs: state.latestBingoTimestamp,
                        roundTs: state.latestRoundTimestamp,
                        gameName: game ? game.name : '',
                        appName: eventData.appName,
                        logo: config.customLogo,
                        menu: state.menuItems || []
                    };
                    const currentStateStr = JSON.stringify(criticalState);
                    if (lastRenderedStateStr === currentStateStr) {
                        return; // Nenhuma mudança crítica, ignora re-render
                    }
                    lastRenderedStateStr = currentStateStr;

                    updateWinnersList(state.gamesData);"""

old_code = """    onSnapshot(doc(db, "events", targetEventId), (docSnap) => {
        if (docSnap.exists()) {
            const eventData = docSnap.data();
            
            if (!eventData.activeGameNumber) {
                statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-yellow-900/50 text-yellow-200 rounded-xl shadow-sm border border-yellow-700/50 animate-pulse";
                statusBanner.innerHTML = `⏳ Aguardando próxima rodada...`;
                contentContainer.classList.add('hidden');
                statusBanner.classList.remove('hidden');
                return;
            }
            
            statusBanner.classList.add('hidden');
            contentContainer.classList.remove('hidden');
            contentContainer.classList.add('flex');
            
            if (eventData.fullStateJSON) {
                try {
                    const state = JSON.parse(eventData.fullStateJSON);
                    const game = state.gamesData[eventData.activeGameNumber];
                    const config = state.appConfig;
                    updateWinnersList(state.gamesData);"""

content = content.replace(old_code, replacement)

with open("attendee.tsx", "w") as f:
    f.write(content)
