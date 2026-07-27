sed -i '/const auctionMinus50Btn/i \
            const auctionItemNameInput = document.getElementById('\''auction-item-name'\'') as HTMLInputElement;\
            const auctionWinnerNameInput = document.getElementById('\''auction-winner-name'\'') as HTMLInputElement;\
            const auctionBidInput = document.getElementById('\''auction-item-current-bid'\'') as HTMLInputElement;\
            if (auctionItemNameInput) auctionItemNameInput.addEventListener('\''input'\'', (e) => { appStore.state.appConfig.auctionItemName = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });\
            if (auctionWinnerNameInput) auctionWinnerNameInput.addEventListener('\''input'\'', (e) => { appStore.state.appConfig.auctionWinnerName = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });\
            if (auctionBidInput) auctionBidInput.addEventListener('\''input'\'', (e) => { appStore.state.appConfig.auctionBid = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });' index.tsx
