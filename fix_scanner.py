import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""                let foundUuid = "";
                for \(const \[uuid, card\] of Object.entries\(appStore.state.cardsData\)\) \{
                    if \(card.series.toString\(\) === searchId\) \{
                        foundUuid = uuid;
                        break;
                    \}
                \}"""

good_replacement = """                let foundUuid = "";
                const searchUpper = searchId.toUpperCase();
                for (const [uuid, card] of Object.entries(appStore.state.cardsData)) {
                    if (card.series.toString() === searchId || (card.code && card.code === searchUpper) || uuid.startsWith(searchId) || uuid.toUpperCase().startsWith(searchUpper)) {
                        foundUuid = uuid;
                        break;
                    }
                }"""
                
content = re.sub(bad_pattern, good_replacement, content)

bad_pattern2 = r"""<input type="text" id="manual-card-id-input" placeholder="Nº da Cartela \(Série\)" class="flex-1 p-4 border-2 border-slate-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 text-center text-xl font-bold">"""
good_replacement2 = """<input type="text" id="manual-card-id-input" placeholder="Nº de Série ou CÓD (ex: 15 ou AB34)" class="flex-1 p-4 border-2 border-slate-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 text-center text-xl font-bold uppercase">"""

content = re.sub(bad_pattern2, good_replacement2, content)

with open('index.tsx', 'w') as f:
    f.write(content)
