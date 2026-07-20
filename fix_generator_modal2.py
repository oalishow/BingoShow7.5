import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""             // Attach event listeners for Card Generator"""

good_replacement = r"""             // Restore values
             const cfg = appStore.state.appConfig.cardGeneratorConfig;
             if (cfg) {
                 const titleEl = document.getElementById('card-batch-title') as HTMLInputElement;
                 const locEl = document.getElementById('card-batch-location') as HTMLInputElement;
                 const dateEl = document.getElementById('card-batch-date') as HTMLInputElement;
                 const priceEl = document.getElementById('card-batch-price') as HTMLInputElement;
                 const colorEl = document.getElementById('card-color') as HTMLInputElement;
                 const perPageEl = document.getElementById('card-cards-per-page') as HTMLSelectElement;
                 const qtyEl = document.getElementById('card-quantity') as HTMLInputElement;
                 if (titleEl && cfg.title) titleEl.value = cfg.title;
                 if (locEl && cfg.location) locEl.value = cfg.location;
                 if (dateEl && cfg.date) dateEl.value = cfg.date;
                 if (priceEl && cfg.price) priceEl.value = cfg.price;
                 if (colorEl && cfg.color) colorEl.value = cfg.color;
                 if (perPageEl && cfg.cardsPerPage) perPageEl.value = cfg.cardsPerPage;
                 if (qtyEl && cfg.quantity) qtyEl.value = cfg.quantity.toString();
                 
                 const optTitleEl = document.getElementById('card-opt-title') as HTMLInputElement;
                 const optLocDateEl = document.getElementById('card-opt-locdate') as HTMLInputElement;
                 const optPriceEl = document.getElementById('card-opt-price') as HTMLInputElement;
                 const optPrizesEl = document.getElementById('card-opt-prizes') as HTMLInputElement;
                 const optQREl = document.getElementById('card-opt-qr') as HTMLInputElement;
                 const optCodeEl = document.getElementById('card-opt-code') as HTMLInputElement;
                 
                 if (optTitleEl && cfg.showTitle !== undefined) optTitleEl.checked = cfg.showTitle;
                 if (optLocDateEl && cfg.showLocationDate !== undefined) optLocDateEl.checked = cfg.showLocationDate;
                 if (optPriceEl && cfg.showPrice !== undefined) optPriceEl.checked = cfg.showPrice;
                 if (optPrizesEl && cfg.showPrizes !== undefined) optPrizesEl.checked = cfg.showPrizes;
                 if (optQREl && cfg.showQRCode !== undefined) optQREl.checked = cfg.showQRCode;
                 if (optCodeEl && cfg.showVerificationCode !== undefined) optCodeEl.checked = cfg.showVerificationCode;
             }

             // Attach event listeners for Card Generator"""

content = re.sub(bad_pattern, good_replacement, content)

with open('index.tsx', 'w') as f:
    f.write(content)
