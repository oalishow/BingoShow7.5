const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

// 1. Add appConfig defaults
if (!code.includes('sponsorDisplaySeconds:')) {
    code = code.replace("modalAutocloseSeconds: 5,", "modalAutocloseSeconds: 5,\n                    sponsorDisplaySeconds: 8,\n                    sponsorTransitionEffect: 'fade',");
}

// 2. Add UI to Settings Tab
const uiToInsert = `
                           <div class="border-b border-gray-700 pb-6 mb-6">
                               <h3 class="text-xl font-bold text-slate-700 dark:text-slate-300 mb-2">Exibição no Telão (Intervalo/Fim)</h3>
                               <div class="space-y-4">
                                   <div>
                                       <label for="sponsor-display-timer" class="block text-sm font-bold text-slate-600 dark:text-slate-400 mb-1">Tempo de exibição por patrocinador (<span id="sponsor-display-value">8</span>s)</label>
                                       <input type="range" id="sponsor-display-timer" min="3" max="30" value="8" class="w-full h-2 bg-gray-200 dark:bg-gray-700 rounded-lg appearance-none cursor-pointer range-lg">
                                   </div>
                                   <div>
                                       <label for="sponsor-transition-effect" class="block text-sm font-bold text-slate-600 dark:text-slate-400 mb-1">Efeito de transição</label>
                                       <select id="sponsor-transition-effect" class="block w-full text-sm p-2 bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-white rounded-lg border border-slate-300 dark:border-gray-600 focus:ring-2 focus:ring-amber-500 outline-none">
                                           <option value="fade">Fade In / Fade Out</option>
                                           <option value="slide">Deslizar</option>
                                           <option value="zoom">Zoom</option>
                                           <option value="random">Aleatório</option>
                                       </select>
                                   </div>
                               </div>
                           </div>`;
if (!code.includes('sponsor-display-timer')) {
    code = code.replace('<div id="tab-content-sponsors" class="hidden space-y-4 text-left">', '<div id="tab-content-sponsors" class="hidden space-y-4 text-left">' + uiToInsert);
}

// 3. Add JS bindings
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
if (!code.includes('sponsor-display-timer')) {
    // Note: since I just injected it in HTML, the file will contain it. 
}

fs.writeFileSync('index.tsx', code);
