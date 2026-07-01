const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

// For HTML
code = code.replace(/class="text-slate-200 font-medium"/g, 'class="text-slate-800 dark:text-slate-200 font-medium"');
code = code.replace(/class="ml-3 text-sm text-slate-200"/g, 'class="ml-3 text-sm text-slate-800 dark:text-slate-200"');
code = code.replace(/p class="text-slate-200"/g, 'p class="text-slate-800 dark:text-slate-200"');

// For bingo cells CSS
code = code.replace(/cell.classList.add\('text-slate-200'\)/g, "if (document.documentElement.classList.contains('dark')) cell.classList.add('text-slate-200'); else cell.classList.add('text-slate-800');");
code = code.replace(/numberEl.classList.toggle\('text-slate-200'\)/g, "if (document.documentElement.classList.contains('dark')) numberEl.classList.toggle('text-slate-200'); else numberEl.classList.toggle('text-slate-800');");
code = code.replace(/cell.classList.remove\('scale-125', 'text-gray-900', 'text-slate-200', 'text-white'\)/g, "cell.classList.remove('scale-125', 'text-gray-900', 'text-slate-200', 'text-slate-800', 'text-white')");
code = code.replace(/cell.classList.remove\('bg-gray-700', 'text-slate-300', 'text-gray-900', 'text-white', 'text-slate-200'\)/g, "cell.classList.remove('bg-gray-700', 'text-slate-300', 'text-gray-900', 'text-white', 'text-slate-200', 'text-slate-800')");

// For verification numberEl
code = code.replace(/cursor-pointer bg-gray-700 text-slate-200'/g, "cursor-pointer bg-gray-200 dark:bg-gray-700 text-slate-800 dark:text-slate-200'");
code = code.replace(/numberEl.classList.toggle\('bg-gray-700'\)/g, "numberEl.classList.toggle('bg-gray-200'); numberEl.classList.toggle('dark:bg-gray-700')");

fs.writeFileSync('index.tsx', code);

