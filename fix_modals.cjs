const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

// Replace bg-gray-700 text-slate-300 with bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-slate-300
code = code.replace(/bg-gray-700',\s*'text-slate-300'/g, "'bg-gray-200', 'dark:bg-gray-700', 'text-gray-800', 'dark:text-slate-300'");
code = code.replace(/bg-gray-700 text-slate-300/g, 'bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-slate-300');
code = code.replace(/'bg-gray-700', 'text-slate-300', 'text-gray-900', 'text-white', 'text-slate-200', 'text-slate-800'/g, "'bg-gray-200', 'dark:bg-gray-700', 'text-gray-800', 'dark:text-slate-300', 'text-gray-900', 'text-white', 'text-slate-200', 'text-slate-800'");

// Fix text-white inside modals that should be text-gray-900 dark:text-white
code = code.replace(/<h2 class="text-3xl font-bold text-white mb-2">Resultado da Verificação<\/h2>/g, '<h2 class="text-3xl font-bold text-gray-900 dark:text-white mb-2">Resultado da Verificação</h2>');
code = code.replace(/<h3 class="text-xl text-slate-300 mb-4">Cartela/g, '<h3 class="text-xl text-slate-800 dark:text-slate-300 mb-4">Cartela');
code = code.replace(/bg-gray-800 p-8 rounded-2xl shadow-2xl transition-transform/g, 'bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-2xl transition-transform');

// Input border formatting
code = code.replace(/bg-gray-800 text-white/g, 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white');
code = code.replace(/bg-gray-900 text-white/g, 'bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-white');

fs.writeFileSync('index.tsx', code);
