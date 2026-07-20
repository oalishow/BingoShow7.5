import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""             if \(appStore.state.appConfig.enableSoundEffects\) sounds.playClick\(\);
             DOMElements.cardGeneratorModal.innerHTML = getModalTemplates\(\).cardGenerator;
             DOMElements.cardGeneratorModal.classList.remove\('hidden'\);

        \}"""

good_replacement = r"""             if (appStore.state.appConfig.enableSoundEffects) sounds.playClick();
             DOMElements.cardGeneratorModal.innerHTML = getModalTemplates().cardGenerator;
             DOMElements.cardGeneratorModal.classList.remove('hidden');
             
             // Attach event listeners for Card Generator
             const generateBtn = document.getElementById('generate-and-print-cards-btn');
             if (generateBtn) {
                 generateBtn.addEventListener('click', generateAndPrintCards);
             }
             const closeBtn = document.getElementById('close-card-generator-btn');
             if (closeBtn) {
                 closeBtn.addEventListener('click', () => DOMElements.cardGeneratorModal.classList.add('hidden'));
             }
        }"""

content = re.sub(bad_pattern, good_replacement, content)

with open('index.tsx', 'w') as f:
    f.write(content)
