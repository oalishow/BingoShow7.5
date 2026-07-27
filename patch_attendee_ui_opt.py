import re

with open("attendee.tsx") as f:
    content = f.read()

# We replace the criticalState object with separate state trackers

replacement = """    let lastNumbersStr = '';
    let lastAuctionStr = '';
    let lastRoundStatusStr = '';
    let lastLabelsStr = '';
    let lastWinnersStr = '';

    onSnapshot(doc(db, "events", targetEventId), (docSnap) => {
        if (docSnap.exists()) {
            const eventData = docSnap.data();
            
            if (!eventData.activeGameNumber) {
                statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-yellow-900/50 text-yellow-200 rounded-xl shadow-sm border border-yellow-700/50 animate-pulse";
                statusBanner.innerHTML = `⏳ Aguardando próxima rodada...`;
                contentContainer.classList.add('hidden');
                statusBanner.classList.remove('hidden');
                lastNumbersStr = '';
                lastAuctionStr = '';
                lastRoundStatusStr = '';
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

                    const labelsStr = JSON.stringify(state.appLabels || {});
                    if (lastLabelsStr !== labelsStr) {
                        lastLabelsStr = labelsStr;
                        const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };
                        if (labels.supportButton) {
                            const btnText = document.getElementById('donate-btn-text');
                            if (btnText) btnText.textContent = labels.supportButton;
                        }
                        if (labels.donationModalTitle) {
                            const mTitle = document.getElementById('donation-modal-title');
                            if (mTitle) mTitle.textContent = labels.donationModalTitle;
                        }
                        if (labels.donationModalDescription) {
                            const mDesc = document.getElementById('donation-modal-desc');
                            if (mDesc) mDesc.textContent = labels.donationModalDescription;
                        }
                        if (labels.donationModalPaypalLabel) {
                            const pLabel = document.getElementById('donation-modal-paypal-label');
                            if (pLabel) pLabel.textContent = labels.donationModalPaypalLabel;
                        }
                        if (labels.donationModalPixLabel) {
                            const pixLabel = document.getElementById('donation-modal-pix-label');
                            if (pixLabel) pixLabel.textContent = labels.donationModalPixLabel;
                        }
                        const pixDisplay = document.getElementById('pix-key-display-attendee');
                        if (pixDisplay && config.pixKey) {
                            pixDisplay.textContent = config.pixKey;
                        }
                        if (labels.donationModalCopyButton) {
                            const copyBtn = document.getElementById('copy-pix-btn-attendee');
                            if (copyBtn && !copyBtn.textContent?.includes('Copiado')) copyBtn.textContent = labels.donationModalCopyButton;
                        }
                    }

                    const winnersStr = JSON.stringify(game ? game.winners : []);
                    if (lastWinnersStr !== winnersStr) {
                        lastWinnersStr = winnersStr;
                        updateWinnersList(state.gamesData);
                    }

"""

old_code = """    let lastRenderedStateStr = '';

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

                    updateWinnersList(state.gamesData);
                    
                    const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };
                    
                    // Update donation modal contents
                    if (labels.supportButton) {
                        const btnText = document.getElementById('donate-btn-text');
                        if (btnText) btnText.textContent = labels.supportButton;
                    }
                    if (labels.donationModalTitle) {
                        const mTitle = document.getElementById('donation-modal-title');
                        if (mTitle) mTitle.textContent = labels.donationModalTitle;
                    }
                    if (labels.donationModalDescription) {
                        const mDesc = document.getElementById('donation-modal-desc');
                        if (mDesc) mDesc.textContent = labels.donationModalDescription;
                    }
                    if (labels.donationModalPaypalLabel) {
                        const pLabel = document.getElementById('donation-modal-paypal-label');
                        if (pLabel) pLabel.textContent = labels.donationModalPaypalLabel;
                    }
                    if (labels.donationModalPixLabel) {
                        const pixLabel = document.getElementById('donation-modal-pix-label');
                        if (pixLabel) pixLabel.textContent = labels.donationModalPixLabel;
                    }
                    
                    const pixDisplay = document.getElementById('pix-key-display-attendee');
                    if (pixDisplay && config.pixKey) {
                        pixDisplay.textContent = config.pixKey;
                    }
                    if (labels.donationModalCopyButton) {
                        const copyBtn = document.getElementById('copy-pix-btn-attendee');
                        if (copyBtn && !copyBtn.textContent?.includes('Copiado')) copyBtn.textContent = labels.donationModalCopyButton;
                    }"""

content = content.replace(old_code, replacement)
with open("attendee.tsx", "w") as f:
    f.write(content)
