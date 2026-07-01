const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const target1 = '<div id="break-right-column" class="flex flex-col items-center bg-black/20 p-6 rounded-xl h-full overflow-hidden relative">';
const replace1 = '<div id="break-right-column" class="flex flex-col items-center bg-black/20 p-6 rounded-xl h-full overflow-hidden relative min-h-0">';

code = code.replace(target1, replace1);

const target2 = '<div id="break-left-column" class="flex flex-col items-center bg-black/20 p-6 rounded-xl h-full overflow-hidden">';
const replace2 = '<div id="break-left-column" class="flex flex-col items-center bg-black/20 p-6 rounded-xl h-full overflow-hidden min-h-0">';

code = code.replace(target2, replace2);

const target3 = '<div id="break-right-content" class="flex-grow w-full h-full flex items-center justify-center transition-opacity duration-500 opacity-0">';
const replace3 = '<div id="break-right-content" class="flex-grow w-full h-full flex items-center justify-center transition-opacity duration-500 opacity-0 min-h-0">';

code = code.replace(target3, replace3);

const target4 = '<div id="break-left-content" class="flex-grow w-full h-full flex items-center justify-center text-7xl font-black text-gray-900 dark:text-white text-center transition-opacity duration-500 opacity-0">';
const replace4 = '<div id="break-left-content" class="flex-grow w-full h-full flex items-center justify-center text-7xl font-black text-gray-900 dark:text-white text-center transition-opacity duration-500 opacity-0 min-h-0">';

code = code.replace(target4, replace4);

fs.writeFileSync('index.tsx', code);
console.log('Fixed more image scaling issues');
