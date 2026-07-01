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

// 4. Update shortcuts block
const oldShortcutsBlock = /<!-- 2\. BOTÕES DE CONTROLE GERAIS -->\s*<div class="flex flex-col gap-2 mb-4 flex-shrink-0">[\s\S]*?<!-- LEGENDA DE ATALHOS -->/;

const newShortcutsHTML = `<!-- 2. BOTÕES DE CONTROLE GERAIS -->
                <div class="grid grid-cols-2 gap-2 mb-4 flex-shrink-0">
                    <button id="shortcut-rounds-btn" class="col-span-2 bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all" onclick="document.getElementById('add-extra-game-btn').scrollIntoView({behavior: 'smooth'})">🎲 Rodadas</button>
                    
                    <button id="show-card-scanner-btn" class="bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center">🔎 Verificar Cartela</button>
                    <button id="shortcut-auto-draw-btn" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center" onclick="document.getElementById('auto-draw-btn-bottom').click()">⚙️ Sorteio Auto</button>
                    
                    <button id="shortcut-verify-btn" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center" onclick="document.getElementById('verify-btn-bottom').click()">✔️ Verificar Nºs</button>
                    <button id="interval-btn" class="bg-teal-600 hover:bg-teal-700 text-white font-bold py-2 px-2 rounded-lg text-xs shadow-lg transition-all text-center" data-label-key="intervalButton">⏱️ Intervalo</button>
                </div>
                
                <!-- AÇÕES EXTRAS -->
                <div class="flex flex-col gap-2 mb-4 flex-shrink-0">
                    <button id="show-card-generator-btn" class="w-full bg-teal-500 hover:bg-teal-600 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all">Gerar Cartelas</button>
                    <div class="grid grid-cols-2 gap-2">
                        <button id="save-to-file-btn" class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg text-xs shadow-lg transition-all text-center" data-label-key="saveToFileButton">Salvar (PC)</button>
                        <label id="load-from-file-btn" for="load-from-file-input" class="w-full bg-sky-600 hover:bg-sky-700 text-white font-bold py-2 px-4 rounded-lg text-xs shadow-lg transition-all text-center cursor-pointer" data-label-key="loadFromFileButton">Carregar</label>
                        <input type="file" id="load-from-file-input" class="hidden" accept=".json,application/json">
                    </div>
                    <div class="flex gap-2 items-center">
                        <button id="edit-menu-btn" title="Editar Cardápio" class="flex-grow bg-slate-300 dark:bg-gray-600 hover:bg-slate-400 dark:hover:bg-gray-500 text-slate-800 dark:text-white font-bold p-2 rounded-lg text-sm shadow-lg transition-all flex justify-center items-center gap-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z" /><path fill-rule="evenodd" d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z" clip-rule="evenodd" /></svg>
                             Editar Cardápio
                        </button>
                    </div>
                    <button id="share-btn" class="hidden w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-xl text-base shadow-lg transition-all" data-label-key="generateProofButton">Gerar Prova</button>
                    <button id="end-event-btn" class="hidden w-full bg-purple-700 hover:bg-purple-800 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all" data-label-key="endEventButton">Encerrar Evento</button>
                    <button id="reset-event-btn" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all" data-label-key="resetEventButton">Reiniciar Evento</button>
                </div>
                
                <!-- LEGENDA DE ATALHOS -->`;

html = html.replace(oldShortcutsBlock, newShortcutsHTML);

fs.writeFileSync('index.html', html);
