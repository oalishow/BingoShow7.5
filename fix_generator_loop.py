import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""            const startSeries = resetSeries \? 1 : Object\.keys\(appStore\.state\.cardsData\)\.length \+ 1;
            const newCardsBatch: Record<string, any> = \{\};
            const uuids = \[\];
            for \(let i = 0; i < quantity; i\+\+\) \{
                const uuid = generateUUID\(\);
                uuids\.push\(uuid\);
                const numbers = generateSingleBingoCardNumbers\(\);
                let code = '';
                do \{
                    code = Math\.random\(\)\.toString\(36\)\.substring\(2, 6\)\.toUpperCase\(\);
                \} while \(Object\.values\(appStore\.state\.cardsData\)\.some\(c => c\.code === code\) \|\| Object\.values\(newCardsBatch\)\.some\(c => c\.code === code\)\);
                
                const cardData = \{
                    series: startSeries \+ i,
                    numbers: numbers,
                    code: code
                \};
                appStore\.state\.cardsData\[uuid\] = cardData;
                newCardsBatch\[uuid\] = cardData;
            \}"""

good_replacement = r"""            const startSeries = resetSeries ? 1 : Object.keys(appStore.state.cardsData).length + 1;
            const newCardsBatch: Record<string, any> = {};
            const uuids = [];
            
            // Optimize code generation to prevent UI freeze
            const usedCodes = new Set<string>();
            for (const c of Object.values(appStore.state.cardsData)) {
                if (c && c.code) usedCodes.add(c.code);
            }
            
            for (let i = 0; i < quantity; i++) {
                const uuid = generateUUID();
                uuids.push(uuid);
                const numbers = generateSingleBingoCardNumbers();
                let code = '';
                do {
                    code = Math.random().toString(36).substring(2, 6).toUpperCase();
                } while (usedCodes.has(code));
                usedCodes.add(code);
                
                const cardData = {
                    series: startSeries + i,
                    numbers: numbers,
                    code: code
                };
                appStore.state.cardsData[uuid] = cardData;
                newCardsBatch[uuid] = cardData;
            }"""

if bad_pattern in content:
    print("Found with regex")
    content = re.sub(bad_pattern, good_replacement, content)
else:
    print("Not found with regex, using replace")
    bad = """            const startSeries = resetSeries ? 1 : Object.keys(appStore.state.cardsData).length + 1;
            const newCardsBatch: Record<string, any> = {};
            const uuids = [];
            for (let i = 0; i < quantity; i++) {
                const uuid = generateUUID();
                uuids.push(uuid);
                const numbers = generateSingleBingoCardNumbers();
                let code = '';
                do {
                    code = Math.random().toString(36).substring(2, 6).toUpperCase();
                } while (Object.values(appStore.state.cardsData).some(c => c.code === code) || Object.values(newCardsBatch).some(c => c.code === code));
                
                const cardData = {
                    series: startSeries + i,
                    numbers: numbers,
                    code: code
                };
                appStore.state.cardsData[uuid] = cardData;
                newCardsBatch[uuid] = cardData;
            }"""
    content = content.replace(bad, good_replacement)

with open('index.tsx', 'w') as f:
    f.write(content)

