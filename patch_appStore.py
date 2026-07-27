import re

with open("index.tsx") as f:
    content = f.read()

# Add pendingNumber to state
if 'currentBingoType: \'\',' in content and 'pendingNumber: null as number | null,' not in content:
    content = content.replace("currentBingoType: '',", "currentBingoType: '',\n                pendingNumber: null as number | null,")

# Add auction fields to appConfig
if 'boardColor: \'default\',' in content and 'auctionBid:' not in content:
    content = content.replace("boardColor: 'default',", "boardColor: 'default',\n                    auctionBid: '0',\n                    auctionItemName: '',\n                    auctionWinnerName: '',")

with open("index.tsx", "w") as f:
    f.write(content)
print("Done")
