const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace(/<button id="show-card-generator-btn" class="w-full bg-teal-500 hover:bg-teal-600 text-white font-bold py-2 px-4 rounded-lg text-sm shadow-lg transition-all">Gerar Cartelas<\/button>\s*/g, '');

fs.writeFileSync('index.html', html);
