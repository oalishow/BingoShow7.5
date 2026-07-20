import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern_code = r"""                const numbers = generateSingleBingoCardNumbers\(\);
                const cardData = \{
                    series: startSeries \+ i,
                    numbers: numbers
                \};"""
                
good_replacement_code = """                const numbers = generateSingleBingoCardNumbers();
                let code = '';
                do {
                    code = Math.random().toString(36).substring(2, 6).toUpperCase();
                } while (Object.values(appStore.state.cardsData).some(c => c.code === code) || Object.values(newCardsBatch).some(c => c.code === code));
                
                const cardData = {
                    series: startSeries + i,
                    numbers: numbers,
                    code: code
                };"""

content = re.sub(bad_pattern_code, good_replacement_code, content)

bad_pattern_save = r"""            const saveTemplate = \(document.getElementById\('card-save-template'\) as HTMLInputElement\)\?\.checked \?\? false;

            if \(saveTemplate\) \{
                 appStore.state.appConfig.cardGeneratorConfig = \{
                      title,
                      location: locationVal,
                      date: dateVal,
                      price: priceVal,
                      quantity,
                      color: cardColor,"""

good_replacement_save = """            const saveTemplate = (document.getElementById('card-save-template') as HTMLInputElement)?.checked ?? false;
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
                      cardsPerPage: layoutSelect,"""

content = re.sub(bad_pattern_save, good_replacement_save, content)

bad_pattern_layout = r"""            const logoData = appStore.state.appConfig.customLogoBase64 \|\| '';
            const useLogo = !!logoData;

            // Split into pages of 6
            for \(let i = 0; i < uuids.length; i \+= 6\) \{
                const batch = uuids.slice\(i, i \+ 6\);"""

good_replacement_layout = """            const logoData = appStore.state.appConfig.customLogoBase64 || '';
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
            
            let gridClasses = "grid-cols-2 grid-rows-3";
            if (cpp === 1) gridClasses = "grid-cols-1 grid-rows-1";
            else if (cpp === 2) gridClasses = "grid-cols-1 grid-rows-2";
            else if (cpp === 4) gridClasses = "grid-cols-2 grid-rows-2";
            else if (cpp === 6) gridClasses = "grid-cols-2 grid-rows-3";
            else if (cpp === 8) gridClasses = "grid-cols-2 grid-rows-4";

            // Split into pages
            for (let i = 0; i < uuids.length; i += cpp) {
                const batch = uuids.slice(i, i + cpp);"""
                
content = re.sub(bad_pattern_layout, good_replacement_layout, content)

bad_pattern_grid_classes = r"""                        <!-- MAIN GRIDS -->
                        <div class="flex-grow grid grid-cols-2 grid-rows-3 gap-1 pb-1 relative min-h-0">
                             \$\{resolvedBatchHTML.join\(''\)\}
                        </div>"""

good_replacement_grid_classes = """                        <!-- MAIN GRIDS -->
                        <div class="flex-grow grid ${gridClasses} gap-1 pb-1 relative min-h-0">
                             ${resolvedBatchHTML.join('')}
                        </div>"""
                        
content = re.sub(bad_pattern_grid_classes, good_replacement_grid_classes, content)


with open('index.tsx', 'w') as f:
    f.write(content)
