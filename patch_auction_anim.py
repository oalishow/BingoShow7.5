import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement = """
                    // Auction
                    const currentBid = parseInt(config.auctionBid || '0', 10);
                    if (currentBid > 0) {
                        attendeeAuctionCard.classList.remove('hidden');
                        attendeeAuctionCard.classList.add('flex');
                        attendeeAuctionItem.textContent = config.auctionItemName || 'Item em Leilão';
                        const newBidText = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(currentBid);
                        if (attendeeAuctionBid.textContent !== newBidText) {
                            attendeeAuctionBid.textContent = newBidText;
                            attendeeAuctionBid.classList.add('text-green-400', 'scale-125');
                            setTimeout(() => {
                                attendeeAuctionBid.classList.remove('text-green-400', 'scale-125');
                            }, 300);
                        }
                    } else {
                        attendeeAuctionCard.classList.add('hidden');
                        attendeeAuctionCard.classList.remove('flex');
                    }
"""

tsx = re.sub(
    r"// Auction.*?attendeeAuctionCard\.classList\.remove\('flex'\);\s*\}",
    replacement.strip(),
    tsx,
    flags=re.DOTALL
)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
