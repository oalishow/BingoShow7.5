import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement2 = """
                    // Auction
                    const currentBid = parseInt(config.auctionBid || '0', 10);
                    if (currentBid > 0) {
                        attendeeAuctionCard.classList.remove('hidden');
                        attendeeAuctionCard.classList.add('flex');
                        attendeeAuctionItem.textContent = config.auctionItemName || 'Item em Leilão';
                        attendeeAuctionBid.textContent = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(currentBid);
                    } else {
                        attendeeAuctionCard.classList.add('hidden');
                        attendeeAuctionCard.classList.remove('flex');
                    }
"""

tsx = re.sub(
    r"// Auction\s+if \(eventData\.activeGameNumber === 'Leilão'\) \{.*?attendeeAuctionCard\.classList\.remove\('flex'\);\n                    \}",
    replacement2,
    tsx,
    flags=re.DOTALL
)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
