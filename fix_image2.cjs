const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regex = /let innerHTML = '';[\s\S]*?rightIndex\+\+;/g;
const newStr = `let innerHTML = '';
                        if (useSponsors) {
                            if (item.image) {
                                innerHTML += \`<div class="w-full flex-1 min-h-0 flex items-center justify-center mb-6"><img src="\${item.image}" class="max-w-full max-h-full object-contain drop-shadow-2xl"></div>\`;
                            }
                            if (item.name) {
                                innerHTML += \`<p class="text-5xl md:text-7xl text-center font-black text-amber-400 flex-shrink-0">\${item.name}</p>\`;
                            }
                        } else {
                            if (item.name) {
                                innerHTML += \`<p class="text-5xl md:text-7xl text-center font-bold text-slate-100 mb-6">\${item.name}</p>\`;
                            }
                            if (item.prize) {
                                innerHTML += \`<p class="text-6xl md:text-8xl text-center font-black text-amber-400">\${item.prize}</p>\`;
                            }
                        }
                        
                        rightContentEl.innerHTML = \`<div class="flex flex-col items-center justify-center bg-black/40 rounded-xl p-8 w-full h-full border border-sky-900/40 shadow-xl overflow-hidden min-h-0">\${innerHTML}</div>\`;
                        applyTransition(rightContentEl, 'in');
                        rightIndex++;`;

code = code.replace(regex, newStr);

// Also need to make sure main and break-right-column can stretch to full height.
const eventBreakOld = `eventBreak: \`<div class="modal-content bg-white dark:bg-gray-800/90 backdrop-blur-sm p-8 rounded-2xl shadow-2xl w-full h-full text-center flex flex-col justify-between">
                                <header class="flex-shrink-0">
                                    <h2 id="event-break-title" class="text-6xl font-black text-sky-400">\${appLabels.intervalModalTitle}</h2>
                                </header>
                                <main class="flex-grow my-8 grid grid-cols-1 md:grid-cols-2 gap-8 overflow-hidden relative z-10 min-h-0">`;
const eventBreakOld2 = `                                <main class="flex-grow my-8 grid grid-cols-1 md:grid-cols-2 gap-8 overflow-hidden relative z-10">`;

if (code.includes(eventBreakOld2)) {
    code = code.replace(eventBreakOld2, eventBreakOld2.replace('relative z-10"', 'relative z-10 min-h-0"'));
}

fs.writeFileSync('index.tsx', code);
console.log('Fixed image scaling');
