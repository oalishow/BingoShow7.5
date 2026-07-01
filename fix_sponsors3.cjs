const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const updateContentReplacement = `
            const applyTransition = (el: HTMLElement, state: 'out' | 'in') => {
                const effect = appStore.state.appConfig.sponsorTransitionEffect === 'random' 
                    ? ['fade', 'slide', 'zoom'][Math.floor(Math.random() * 3)] 
                    : appStore.state.appConfig.sponsorTransitionEffect || 'fade';
                
                el.style.transition = 'all 0.5s ease-in-out';
                el.classList.remove('opacity-0', 'translate-x-[100%]', 'scale-50');
                
                if (state === 'out') {
                    if (effect === 'fade') el.classList.add('opacity-0');
                    else if (effect === 'slide') el.classList.add('opacity-0', 'translate-x-[100%]');
                    else if (effect === 'zoom') el.classList.add('opacity-0', 'scale-50');
                }
            };

            const updateContent = () => {
                applyTransition(leftContentEl, 'out');
                setTimeout(() => {
                    leftContentEl.innerHTML = menuItems[leftIndex % menuItems.length];
                    applyTransition(leftContentEl, 'in');
                    leftIndex++;
                }, 500);

                if (rightColumnContent.length > 0) {
                    applyTransition(rightContentEl, 'out');
                    setTimeout(() => {
                        const item = rightColumnContent[rightIndex % rightColumnContent.length];
                        if (item.image) { 
                            rightContentEl.innerHTML = \`<img src="\${item.image}" class="max-h-64 object-contain mb-4 rounded-lg shadow-lg"><p>\${item.name}</p>\`;
                        } else { 
                            rightContentEl.innerHTML = \`<p>\${item.name}</p><p class="text-amber-400 text-5xl mt-2">\${item.prize}</p>\`;
                        }
                        applyTransition(rightContentEl, 'in');
                        rightIndex++;
                    }, 500);
                } else { 
                    rightContentEl.innerHTML = \`<p class="text-3xl text-slate-400">Ainda não há vencedores ou patrocinadores cadastrados.</p>\`;
                }
            };`;

code = code.replace(/const updateContent = \(\) => \{[\s\S]*?\};\s*const updateClock/, updateContentReplacement + '\n            const updateClock');
code = code.replace('intervalContentInterval = setInterval(updateContent, 6000);', 'const cycleTime = (appStore.state.appConfig.sponsorDisplaySeconds || 8) * 1000;\n            intervalContentInterval = setInterval(updateContent, cycleTime);');

fs.writeFileSync('index.tsx', code);
