const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regexLogic = /const updateContent = \(\) => \{[\s\S]*?const updateClock = \(\) => \{/g;

const newLogic = `const updateContent = () => {
                if (hasMenu) {
                    applyTransition(leftContentEl, 'out');
                    setTimeout(() => {
                        leftContentEl.innerHTML = menuItems[leftIndex % menuItems.length] || '';
                        applyTransition(leftContentEl, 'in');
                        leftIndex++;
                    }, 500);
                }

                if (rightColumnContent.length > 0) {
                    applyTransition(rightContentEl, 'out');
                    setTimeout(() => {
                        const item = rightColumnContent[rightIndex % rightColumnContent.length];
                        
                        let innerHTML = '';
                        if (useSponsors) {
                            if (item.image) {
                                innerHTML += \`<img src="\${item.image}" class="max-w-full max-h-[60vh] object-contain mb-6 drop-shadow-2xl">\`;
                            }
                            if (item.name) {
                                innerHTML += \`<p class="text-5xl md:text-7xl text-center font-black text-amber-400">\${item.name}</p>\`;
                            }
                        } else {
                            if (item.name) {
                                innerHTML += \`<p class="text-5xl md:text-7xl text-center font-bold text-slate-100 mb-6">\${item.name}</p>\`;
                            }
                            if (item.prize) {
                                innerHTML += \`<p class="text-6xl md:text-8xl text-center font-black text-amber-400">\${item.prize}</p>\`;
                            }
                        }
                        
                        rightContentEl.innerHTML = \`<div class="flex flex-col items-center justify-center bg-black/40 rounded-xl p-8 w-full h-full border border-sky-900/40 shadow-xl overflow-hidden">\${innerHTML}</div>\`;
                        applyTransition(rightContentEl, 'in');
                        rightIndex++;
                    }, 500);
                } else {
                     rightContentEl.innerHTML = \`<div class="flex flex-col items-center justify-center h-full w-full bg-black/40 rounded-xl border border-sky-900/40"><p class="text-4xl text-slate-400 font-bold">Nenhum dado cadastrado.</p></div>\`;
                }
            };
            
            const updateClock = () => {`;

if (regexLogic.test(code)) {
    code = code.replace(regexLogic, newLogic);
    fs.writeFileSync('index.tsx', code);
    console.log("REPLACED updateContent!");
} else {
    console.log("REGEX FAILED for updateContent");
}
