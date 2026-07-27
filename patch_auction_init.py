import re

with open("index.tsx") as f:
    content = f.read()

old_block = """            const auctionItemNameInput = document.getElementById('auction-item-name') as HTMLInputElement;
            const auctionWinnerNameInput = document.getElementById('auction-winner-name') as HTMLInputElement;
            const auctionBidInput = document.getElementById('auction-item-current-bid') as HTMLInputElement;
            if (auctionItemNameInput) auctionItemNameInput.addEventListener('input', (e) => { appStore.state.appConfig.auctionItemName = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });
            if (auctionWinnerNameInput) auctionWinnerNameInput.addEventListener('input', (e) => { appStore.state.appConfig.auctionWinnerName = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });
            if (auctionBidInput) auctionBidInput.addEventListener('input', (e) => { appStore.state.appConfig.auctionBid = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });"""

new_block = """            const auctionItemNameInput = document.getElementById('auction-item-name') as HTMLInputElement;
            const auctionWinnerNameInput = document.getElementById('auction-winner-name') as HTMLInputElement;
            const auctionBidInput = document.getElementById('auction-item-current-bid') as HTMLInputElement;
            if (auctionItemNameInput) {
                auctionItemNameInput.value = appStore.state.appConfig.auctionItemName || '';
                auctionItemNameInput.addEventListener('input', (e) => { appStore.state.appConfig.auctionItemName = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });
            }
            if (auctionWinnerNameInput) {
                auctionWinnerNameInput.value = appStore.state.appConfig.auctionWinnerName || '';
                auctionWinnerNameInput.addEventListener('input', (e) => { appStore.state.appConfig.auctionWinnerName = (e.target as HTMLInputElement).value; appStore.debouncedSave(); });
            }
            if (auctionBidInput) {
                auctionBidInput.value = appStore.state.appConfig.auctionBid || '0';
                updateAuctionBidDisplay(parseInt(auctionBidInput.value) || 0);
                auctionBidInput.addEventListener('input', (e) => { 
                    appStore.state.appConfig.auctionBid = (e.target as HTMLInputElement).value; 
                    updateAuctionBidDisplay(parseInt(appStore.state.appConfig.auctionBid) || 0);
                    appStore.debouncedSave(); 
                });
            }"""

if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("Could not find the block to replace!")

with open("index.tsx", "w") as f:
    f.write(content)
