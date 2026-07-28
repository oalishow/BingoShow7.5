import re

with open('index.tsx', 'r') as f:
    content = f.read()

# Replace inputs retrieval
old_inputs = """            const quantityInput = document.getElementById('card-quantity') as HTMLInputElement;
            const colorInput = document.getElementById('card-color') as HTMLInputElement;
            
            if (!quantityInput) return;"""

new_inputs = """            const quantityInput = document.getElementById('card-quantity') as HTMLInputElement;
            const colorInput = document.getElementById('card-color') as HTMLInputElement;
            const layoutInput = document.getElementById('card-layout') as HTMLSelectElement;
            const includeQrInput = document.getElementById('card-include-qr') as HTMLInputElement;
            const includeLogoInput = document.getElementById('card-include-logo') as HTMLInputElement;
            const extraInstructionsInput = document.getElementById('card-extra-instructions') as HTMLInputElement;
            
            if (!quantityInput) return;"""

if old_inputs in content:
    content = content.replace(old_inputs, new_inputs)
    print("Inputs patched")
else:
    print("Inputs not found")

# Replace variable initializations
old_vars = """            const quantity = parseInt(quantityInput.value, 10);
            const cardColor = colorInput ? colorInput.value : '#0ea5e9';
            const isLight = isLightColor(cardColor);
            const headerTextColor = isLight ? '#000000' : '#ffffff';"""

new_vars = """            const quantity = parseInt(quantityInput.value, 10);
            const cardColor = colorInput ? colorInput.value : '#0ea5e9';
            const isLight = isLightColor(cardColor);
            const headerTextColor = isLight ? '#000000' : '#ffffff';
            const cardsPerPage = layoutInput ? parseInt(layoutInput.value, 10) : 6;
            const includeQr = includeQrInput ? includeQrInput.checked : true;
            const cardUseLogo = includeLogoInput ? includeLogoInput.checked : true;
            const extraInstructions = (extraInstructionsInput && extraInstructionsInput.value.trim()) || '';"""

if old_vars in content:
    content = content.replace(old_vars, new_vars)
    print("Vars patched")
else:
    print("Vars not found")

# Replace the HTML generation loop
old_loop = """            const logoData = appStore.state.appConfig.customLogoBase64 || '';
            const useLogo = !!logoData;

            // Split into pages of 6
            for (let i = 0; i < uuids.length; i += 6) {
                const batch = uuids.slice(i, i + 6);
                const firstSeriesOfFolha = appStore.state.cardsData[batch[0]].series;
                const folhaNumber = Math.floor((firstSeriesOfFolha - 1) / 6) + 1;"""

new_loop = """            const logoData = appStore.state.appConfig.customLogoBase64 || '';
            const useLogo = cardUseLogo && !!logoData;

            // Split into pages
            for (let i = 0; i < uuids.length; i += cardsPerPage) {
                const batch = uuids.slice(i, i + cardsPerPage);
                const firstSeriesOfFolha = appStore.state.cardsData[batch[0]].series;
                const folhaNumber = Math.floor((firstSeriesOfFolha - 1) / cardsPerPage) + 1;"""

if old_loop in content:
    content = content.replace(old_loop, new_loop)
    print("Loop patched")
else:
    print("Loop not found")
    
with open('index.tsx', 'w') as f:
    f.write(content)
