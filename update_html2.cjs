const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Remove old changelog button and old theme toggle
html = html.replace(/<!-- NOVO: Histórico de Versões -->[\s\S]*?(?=<!-- NOVO: Botão de Configurações de Personalização -->)/, '');

// 2. Put version history button in the footer
const footerRegex = /Versão <span id="version">([\s\S]*?)<\/span> - <span id="last-updated">([\s\S]*?)<\/span>/;
html = html.replace(footerRegex, `<button id="show-changelog-btn" class="hover:underline text-sky-600 dark:text-sky-400">Histórico de Versões</button> | Versão <span id="version">$1</span> - <span id="last-updated">$2</span>`);

// 3. Add discrete theme toggle to header
const headerRegex = /<header class="text-center py-4 flex-shrink-0 relative mt-6">/;
const themeButtonHTML = `<header class="text-center py-4 flex-shrink-0 relative mt-6">
            <button id="theme-toggle-main-btn" class="absolute top-0 right-4 p-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white transition-colors h-10 w-10 flex items-center justify-center rounded-full bg-white dark:bg-gray-800 shadow-sm" title="Alternar Modo Claro/Escuro">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 dark:hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 hidden dark:block" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
            </button>`;
html = html.replace(headerRegex, themeButtonHTML);

// 4. Update shortcuts in sidebar
// Replace the start of section 2
const oldShortcutsStart = /<!-- 2\. BOTÕES DE CONTROLE GERAIS -->\s*<div class="flex flex-col gap-2 mb-4 flex-shrink-0">/;
const newShortcutsHTML = `<!-- 2. BOTÕES DE CONTROLE GERAIS (ATALHOS) -->
                <div class="grid grid-cols-2 gap-2 mb-4 flex-shrink-0">
                    <button id="shortcut-rounds-btn" class="col-span-2 bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all" onclick="document.getElementById('add-extra-game-btn').scrollIntoView({behavior: 'smooth'})">🎲 Rodadas</button>
                    
                    <button id="shortcut-verify-btn" class="bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center">🔎 Verificar Cartela</button>
                    <button id="shortcut-auto-draw-btn" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center">⚙️ Sorteio Auto</button>
                    
                    <button id="shortcut-verify-numbers-btn" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center">✔️ Verificar Nºs</button>
                    <button id="shortcut-interval-btn" class="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center">⏱️ Intervalo</button>
                </div>
                
                <!-- 3. ARQUIVOS E OUTRAS AÇÕES -->
                <div class="flex flex-col gap-2 mb-4 flex-shrink-0">`;
html = html.replace(oldShortcutsStart, newShortcutsHTML);

// Remove the old buttons that were moved to shortcuts, since we have them in the DOM already?
// Wait, I need to keep the real buttons but hide them or just wire up the shortcuts to call their logic.
// The real "interval-btn" is inside the old layout, I'll need to remove it from there to not duplicate IDs.
// Same for "show-card-scanner-btn". If I use "shortcut-verify-btn" for "show-card-scanner-btn" I can just wire it up.
// But wait, the original `show-card-scanner-btn` is bound in JS. If I remove it, JS will throw errors!
// I will just use the exactly same IDs for the new buttons so JS binds to them!

fs.writeFileSync('index.html', html);
