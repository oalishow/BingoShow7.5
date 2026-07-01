const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

code = code.replace(/cell\.classList\.remove\('bg-gray-200', 'dark:bg-gray-700', 'text-gray-800', 'dark:text-slate-300', 'text-gray-900', 'text-white', 'text-slate-200', 'text-slate-800'\);/g, "cell.classList.remove('bg-gray-200', 'dark:bg-gray-700', 'text-gray-800', 'dark:text-slate-300', 'text-gray-900', 'text-white', 'text-slate-200', 'text-slate-800', 'dark:text-slate-200');");

fs.writeFileSync('index.tsx', code);
