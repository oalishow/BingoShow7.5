import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_html_checkboxes = r"""                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-title" class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Título
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-locdate" class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Local/Data
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-price" class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Preço
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-prizes" class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Prêmios
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-qr" class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar QR Code
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-code" class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar ID p/ Check
                                                </label>"""
                                                
good_html_checkboxes = """                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-title" checked class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Título
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-locdate" checked class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Local/Data
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-price" checked class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Preço
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-prizes" checked class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar Prêmios
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-qr" checked class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar QR Code
                                                </label>
                                                <label class="flex items-center gap-2 cursor-pointer text-sm text-gray-700 dark:text-gray-300">
                                                    <input type="checkbox" id="card-opt-code" checked class="w-4 h-4 rounded text-sky-600 focus:ring-sky-500"> Mostrar ID p/ Check
                                                </label>"""

content = content.replace(bad_html_checkboxes, good_html_checkboxes)

bad_html_quantity = r"""                                       <div class="flex items-center justify-between gap-2 mt-2">
                                            <div class="flex-1 text-left text-sm font-bold text-slate-500 dark:text-slate-400">Total de Grades:</div>
                                            <input type="number" id="card-quantity" placeholder="Ex: 120 (rendem 20 folhas)" value="120" class="w-32 text-center text-lg font-bold p-3 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500">
                                       </div>"""

good_html_quantity = """                                       <div class="flex items-center justify-between gap-2 mt-2">
                                            <div class="flex-1 text-left text-sm font-bold text-slate-500 dark:text-slate-400">Quantidade de Folhas:</div>
                                            <input type="number" id="card-quantity" placeholder="Ex: 20 folhas" value="20" class="w-32 text-center text-lg font-bold p-3 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500">
                                       </div>"""

content = content.replace(bad_html_quantity, good_html_quantity)

bad_logic = r"""            const quantity = parseInt(quantityInput.value, 10);
            const cardColor = colorInput ? colorInput.value : '#0ea5e9';
            const isLight = isLightColor(cardColor);
            const headerTextColor = isLight ? '#000000' : '#ffffff';

            const optTitle = (document.getElementById('card-opt-title') as HTMLInputElement)?.checked ?? true;
            const optLocDate = (document.getElementById('card-opt-locdate') as HTMLInputElement)?.checked ?? true;
            const optPrice = (document.getElementById('card-opt-price') as HTMLInputElement)?.checked ?? true;
            const optPrizes = (document.getElementById('card-opt-prizes') as HTMLInputElement)?.checked ?? true;
            const optQR = (document.getElementById('card-opt-qr') as HTMLInputElement)?.checked ?? true;
            const optCode = (document.getElementById('card-opt-code') as HTMLInputElement)?.checked ?? true;
            const saveTemplate = (document.getElementById('card-save-template') as HTMLInputElement)?.checked ?? false;
            const downloadBackup = (document.getElementById('card-download-backup') as HTMLInputElement)?.checked ?? true;
            const layoutSelect = (document.getElementById('card-cards-per-page') as HTMLSelectElement)?.value || '6';

            if (saveTemplate) {
                 appStore.state.appConfig.cardGeneratorConfig = {
                      title,
                      location: locationVal,
                      date: dateVal,
                      price: priceVal,
                      quantity,
                      color: cardColor,
                      cardsPerPage: layoutSelect,
                      showTitle: optTitle,
                      showLocationDate: optLocDate,
                      showPrice: optPrice,
                      showPrizes: optPrizes,
                      showQRCode: optQR,
                      showVerificationCode: optCode
                 };
                 appStore.debouncedSave();
            }

            if (isNaN(quantity) || quantity <= 0 || quantity > 5000) {
                showAlert("Por favor, insira uma quantidade válida entre 1 e 5000.");
                return;
            }"""

good_logic = """            const quantityPages = parseInt(quantityInput.value, 10);
            const cardColor = colorInput ? colorInput.value : '#0ea5e9';
            const isLight = isLightColor(cardColor);
            const headerTextColor = isLight ? '#000000' : '#ffffff';

            const optTitle = (document.getElementById('card-opt-title') as HTMLInputElement)?.checked ?? true;
            const optLocDate = (document.getElementById('card-opt-locdate') as HTMLInputElement)?.checked ?? true;
            const optPrice = (document.getElementById('card-opt-price') as HTMLInputElement)?.checked ?? true;
            const optPrizes = (document.getElementById('card-opt-prizes') as HTMLInputElement)?.checked ?? true;
            const optQR = (document.getElementById('card-opt-qr') as HTMLInputElement)?.checked ?? true;
            const optCode = (document.getElementById('card-opt-code') as HTMLInputElement)?.checked ?? true;
            const saveTemplate = (document.getElementById('card-save-template') as HTMLInputElement)?.checked ?? false;
            const downloadBackup = (document.getElementById('card-download-backup') as HTMLInputElement)?.checked ?? true;
            const layoutSelect = (document.getElementById('card-cards-per-page') as HTMLSelectElement)?.value || '6';

            let cpp = 6;
            const numGames = Object.keys(appStore.state.gamesData).length;
            if (layoutSelect === 'auto') {
                if (numGames <= 1) cpp = 6;
                else if (numGames === 2) cpp = 2;
                else if (numGames === 3 || numGames === 4) cpp = 4;
                else if (numGames === 5 || numGames === 6) cpp = 6;
                else cpp = 8;
            } else {
                cpp = parseInt(layoutSelect, 10);
            }
            
            const quantity = quantityPages * cpp;

            if (saveTemplate) {
                 appStore.state.appConfig.cardGeneratorConfig = {
                      title,
                      location: locationVal,
                      date: dateVal,
                      price: priceVal,
                      quantity: quantityPages,
                      color: cardColor,
                      cardsPerPage: layoutSelect,
                      showTitle: optTitle,
                      showLocationDate: optLocDate,
                      showPrice: optPrice,
                      showPrizes: optPrizes,
                      showQRCode: optQR,
                      showVerificationCode: optCode
                 };
                 appStore.debouncedSave();
            }

            if (isNaN(quantityPages) || quantityPages <= 0 || quantityPages > 5000) {
                showAlert("Por favor, insira uma quantidade de folhas válida entre 1 e 5000.");
                return;
            }"""
            
content = content.replace(bad_logic, good_logic)

bad_cpp_logic = r"""            const logoData = appStore.state.appConfig.customLogoBase64 || '';
            const useLogo = !!logoData;
            
            let cpp = 6;
            const numGames = Object.keys(appStore.state.gamesData).length;
            if (layoutSelect === 'auto') {
                if (numGames <= 1) cpp = 6;
                else if (numGames === 2) cpp = 2;
                else if (numGames === 3 || numGames === 4) cpp = 4;
                else if (numGames === 5 || numGames === 6) cpp = 6;
                else cpp = 8;
            } else {
                cpp = parseInt(layoutSelect, 10);
            }
            
            let gridClasses = "grid-cols-2 grid-rows-3";"""

good_cpp_logic = """            const logoData = appStore.state.appConfig.customLogoBase64 || '';
            const useLogo = !!logoData;
            
            let gridClasses = "grid-cols-2 grid-rows-3";"""

content = content.replace(bad_cpp_logic, good_cpp_logic)

with open('index.tsx', 'w') as f:
    f.write(content)
