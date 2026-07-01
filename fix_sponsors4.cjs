const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

code = code.replace(
    '<div id="final-sponsors-list" class="bg-gray-100 dark:bg-gray-900 p-3 rounded-lg max-h-40 overflow-y-auto flex flex-wrap justify-center gap-4">\\n                                        <!-- Lista de patrocinadores aqui -->\\n                                    </div>',
    '<div id="final-sponsors-list" class="bg-gray-100 dark:bg-gray-900 p-3 rounded-lg h-48 flex flex-col items-center justify-center transition-all duration-500 overflow-hidden"></div>'
);

code = code.replace(
    '<div id="final-sponsors-list" class="bg-gray-100 dark:bg-gray-900 p-3 rounded-lg max-h-40 overflow-y-auto flex flex-wrap justify-center gap-4">\n                                        <!-- Lista de patrocinadores aqui -->\n                                    </div>',
    '<div id="final-sponsors-list" class="bg-gray-100 dark:bg-gray-900 p-3 rounded-lg h-48 flex flex-col items-center justify-center transition-all duration-500 overflow-hidden"></div>'
);

fs.writeFileSync('index.tsx', code);
