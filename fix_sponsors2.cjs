const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const jsBindings = `
    const sponsorDisplayTimer = document.getElementById('sponsor-display-timer') as HTMLInputElement;
    const sponsorDisplayValue = document.getElementById('sponsor-display-value') as HTMLElement;
    const sponsorTransitionEffect = document.getElementById('sponsor-transition-effect') as HTMLSelectElement;

    if (sponsorDisplayTimer && appConfig.sponsorDisplaySeconds !== undefined) {
        sponsorDisplayTimer.value = appConfig.sponsorDisplaySeconds.toString();
        sponsorDisplayValue.textContent = appConfig.sponsorDisplaySeconds.toString();
    }
    if (sponsorTransitionEffect && appConfig.sponsorTransitionEffect !== undefined) {
        sponsorTransitionEffect.value = appConfig.sponsorTransitionEffect;
    }

    sponsorDisplayTimer?.addEventListener('input', (e) => {
        const seconds = parseInt((e.target as HTMLInputElement).value);
        appStore.state.appConfig.sponsorDisplaySeconds = seconds;
        if (sponsorDisplayValue) sponsorDisplayValue.textContent = seconds.toString();
    });
    sponsorDisplayTimer?.addEventListener('change', () => appStore.debouncedSave());
    
    sponsorTransitionEffect?.addEventListener('change', (e) => {
        appStore.state.appConfig.sponsorTransitionEffect = (e.target as HTMLSelectElement).value;
        appStore.debouncedSave();
    });
`;

if (!code.includes("const sponsorDisplayTimer")) {
    code = code.replace("const autocloseCheckbox = document.getElementById('enable-modal-autoclose')", jsBindings + "\n    const autocloseCheckbox = document.getElementById('enable-modal-autoclose')");
}

fs.writeFileSync('index.tsx', code);
