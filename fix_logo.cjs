const fs = require('fs');

let code = fs.readFileSync('index.tsx', 'utf8');

const regex = /function renderCustomLogo\(\) \{[\s\S]*?const settingsPreview/;
const target = `function renderCustomLogo() {
    const headerLogoContainer = document.getElementById('app-logo');
    if (!headerLogoContainer) return;

    const defaultLogo = DEFAULT_LOGO_BASE64_PLACEHOLDER;
    const currentLogo = appStore.state.appConfig.customLogoBase64 || defaultLogo;

    if (currentLogo) {
        headerLogoContainer.innerHTML = \`<img id="header-logo" src="\${currentLogo}" alt="Logo do Evento" class="w-full h-full object-contain">\`;
    } else {
        headerLogoContainer.innerHTML = ''; 
    }
    
    const settingsPreview`;

// First, I need to extract the base64 from the initial state
const defaultLogoMatch = code.match(/customLogoBase64:\s*'([^']+)'/);
if (defaultLogoMatch) {
    const replacement = target.replace('DEFAULT_LOGO_BASE64_PLACEHOLDER', `'${defaultLogoMatch[1]}'`);
    code = code.replace(regex, replacement);
    fs.writeFileSync('index.tsx', code);
}
