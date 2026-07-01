const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const oldControls = `                                    <div class="flex-shrink-0 mt-4 flex flex-col items-center z-10">
                                         <div class="my-2 max-w-xs mx-auto w-full flex flex-col items-center justify-center gap-2">
                                           <div class="flex items-center gap-2">
                                               <span class="text-sm font-bold text-slate-400 w-24 text-right">Geral:</span>
                                               <button id="zoom-out-btn-sponsor" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">-</button>
                                               <span id="sponsor-display-zoom-value" class="font-bold text-lg w-16 text-center">100%</span>
                                               <button id="zoom-in-btn-sponsor" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">+</button>
                                           </div>
                                           <div class="flex items-center gap-2">
                                               <span class="text-sm font-bold text-slate-400 w-24 text-right">Número:</span>
                                               <button id="zoom-out-btn-sponsor-number" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">-</button>
                                               <span id="sponsor-number-zoom-value" class="font-bold text-lg w-16 text-center">100%</span>
                                               <button id="zoom-in-btn-sponsor-number" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">+</button>
                                           </div>
                                       </div>`;

const newControls = `                                    <div class="flex-shrink-0 mt-4 flex flex-col items-center z-10">
                                         <div class="my-2 mx-auto w-full flex flex-row items-center justify-center gap-6">
                                           <div class="flex items-center gap-2">
                                               <span class="text-sm font-bold text-slate-400 text-right">Geral:</span>
                                               <button id="zoom-out-btn-sponsor" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">-</button>
                                               <span id="sponsor-display-zoom-value" class="font-bold text-lg w-16 text-center">100%</span>
                                               <button id="zoom-in-btn-sponsor" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">+</button>
                                           </div>
                                           <div class="flex items-center gap-2">
                                               <span class="text-sm font-bold text-slate-400 text-right">Número:</span>
                                               <button id="zoom-out-btn-sponsor-number" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">-</button>
                                               <span id="sponsor-number-zoom-value" class="font-bold text-lg w-16 text-center">100%</span>
                                               <button id="zoom-in-btn-sponsor-number" class="bg-gray-200 dark:bg-gray-700 w-10 h-10 rounded-full font-bold text-2xl">+</button>
                                           </div>
                                       </div>`;

code = code.replace(oldControls, newControls);
fs.writeFileSync('index.tsx', code);
