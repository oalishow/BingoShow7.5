const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace(/<div class="grid grid-cols-2 gap-2">\s*<button id="show-card-generator-btn"[^>]*>Gerar Cartelas<\/button>\s*<button id="show-card-scanner-btn"[^>]*>Verificar Cartela<\/button>\s*<\/div>/, '<button id="show-card-generator-btn" class="w-full bg-teal-500 hover:bg-teal-600 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all text-center">Gerar Cartelas</button>');

fs.writeFileSync('index.html', html);
