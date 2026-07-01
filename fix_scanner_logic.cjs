const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regexScanner = /(closeBtn\.onclick = cleanupScanner;)/;
const inputLogic = `$1

            const manualInput = document.getElementById('manual-card-id-input') as HTMLInputElement;
            const manualBtn = document.getElementById('verify-manual-card-btn') as HTMLButtonElement;
            manualBtn.addEventListener('click', () => {
                const searchId = manualInput.value.trim();
                if (!searchId) {
                    showAlert("Digite o número da cartela.");
                    return;
                }
                
                // Procurar nas cartelas pelo numero curto (series)
                let foundUuid = "";
                for (const [uuid, card] of Object.entries(appStore.state.cardsData)) {
                    if (card.series.toString() === searchId) {
                        foundUuid = uuid;
                        break;
                    }
                }
                
                if (foundUuid) {
                    cleanupScanner();
                    verifyCardByQRCode(foundUuid);
                } else {
                    showAlert("Cartela N° " + searchId + " não encontrada na base de dados.");
                }
            });
            manualInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') manualBtn.click();
            });`;

code = code.replace(regexScanner, inputLogic);
fs.writeFileSync('index.tsx', code);
