const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const regex = /<!-- 2\. BOTÕES DE CONTROLE GERAIS -->[\s\S]*?<!-- AÇÕES EXTRAS -->\s*<div class="flex flex-col gap-2 mb-4 flex-shrink-0">/;
const replacement = `<!-- 2. BOTÕES DE CONTROLE GERAIS -->
                <div class="grid grid-cols-2 gap-2 mb-4 flex-shrink-0">
                    <button id="shortcut-rounds-btn" class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all" onclick="document.getElementById('add-extra-game-btn').scrollIntoView({behavior: 'smooth'})">🎲 Rodadas</button>
                    <button id="interval-btn" class="bg-amber-600 hover:bg-amber-700 text-white font-bold py-2 px-2 rounded-lg text-sm shadow-lg transition-all text-center" data-label-key="intervalButton">⏱️ Intervalo</button>
                </div>
                
                <!-- AÇÕES EXTRAS -->
                <div class="flex flex-col gap-2 mb-4 flex-shrink-0">
                    <div class="grid grid-cols-2 gap-2">
                        <button id="show-card-generator-btn" class="w-full bg-teal-500 hover:bg-teal-600 text-white font-bold py-2 px-4 rounded-lg text-xs shadow-lg transition-all text-center">Gerar Cartelas</button>
                        <button id="show-card-scanner-btn" class="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg text-xs shadow-lg transition-all text-center">Verificar Cartela</button>
                    </div>`;

html = html.replace(regex, replacement);
fs.writeFileSync('index.html', html);
