import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement = """
    const attendeeAuctionCard = document.getElementById('attendee-auction-card')!;
    const attendeeAuctionItem = document.getElementById('attendee-auction-item')!;
    const attendeeAuctionBid = document.getElementById('attendee-auction-bid')!;
"""

tsx = re.sub(r"const overlayMsgEl = document.getElementById\('overlay-msg'\)!;", "const overlayMsgEl = document.getElementById('overlay-msg')!;\n" + replacement, tsx)

replacement2 = """
                    // Auction
                    if (eventData.activeGameNumber === 'Leilão') {
                        attendeeAuctionCard.classList.remove('hidden');
                        attendeeAuctionCard.classList.add('flex');
                        attendeeAuctionItem.textContent = config.auctionItemName || 'Item em Leilão';
                        const currentBid = parseInt(config.auctionBid || '0', 10);
                        if (currentBid > 0) {
                            attendeeAuctionBid.textContent = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(currentBid);
                        } else {
                            attendeeAuctionBid.textContent = 'R$ 0,00';
                        }
                    } else {
                        attendeeAuctionCard.classList.add('hidden');
                        attendeeAuctionCard.classList.remove('flex');
                    }
"""

# Inject before `if (config.customLogo)` inside `if (eventData.appName)`
tsx = re.sub(
    r"if \(eventData\.appName\) \{.*?appNameEl\.classList\.remove\('hidden'\);\n                    \}",
    r"if (eventData.appName) {\n                        appNameEl.textContent = eventData.appName;\n                        appNameEl.classList.remove('hidden');\n                    }\n" + replacement2,
    tsx,
    flags=re.DOTALL
)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
