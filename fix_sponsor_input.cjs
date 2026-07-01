const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const oldInputClasses = `nameInput.className = 'w-full bg-gray-100 dark:bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-white p-1 rounded-md text-sm';`;

const newInputClasses = `nameInput.className = 'w-full bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-white p-2 rounded-md text-sm border border-slate-300 dark:border-gray-600 focus:ring-2 focus:ring-amber-500 outline-none';`;

code = code.replace(oldInputClasses, newInputClasses);
fs.writeFileSync('index.tsx', code);
