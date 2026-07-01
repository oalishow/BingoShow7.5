const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regex = /function showIntervalModal\(\) \{[\s\S]*?            document\.getElementById\('close-break-modal-btn'\)!\.onclick = \(\) => \{[\s\S]*?            \};\n        \}/g;

const newLogic = `function showIntervalModal() {
            const { gamesData, appConfig, menuItems } = appStore.state;
            DOMElements.eventBreakModal.innerHTML = getModalTemplates().eventBreak;
            DOMElements.eventBreakModal.classList.remove('hidden');
            DOMElements.confettiCanvas.style.zIndex = '51'; 
            
            const leftColumnEl = document.getElementById('break-left-column')!;
            const leftContentEl = document.getElementById('break-left-content')!;
            const rightColumnEl = document.getElementById('break-right-column')!;
            const rightContentEl = document.getElementById('break-right-content')!;
            const rightTitleEl = document.getElementById('break-right-title')!;
            const clockEl = document.getElementById('break-clock')!;
            
            const mainGrid = DOMElements.eventBreakModal.querySelector('main');
            
            // Handle Menu Visibility
            const hasMenu = appConfig.showMenuInBreak !== false && menuItems.length > 0;
            if (!hasMenu && mainGrid) {
                leftColumnEl.style.display = 'none';
                mainGrid.classList.remove('md:grid-cols-2');
                mainGrid.classList.add('grid-cols-1');
            } else if (mainGrid) {
                leftColumnEl.style.display = 'flex';
                mainGrid.classList.add('md:grid-cols-2');
            }

            const allWinners = Object.values(gamesData).flatMap(g => g.winners || []);
            const allSponsors = Object.values(appConfig.sponsorsByNumber).filter(s => (s.name && s.name.trim() !== "") || s.image);
            if ((appConfig.globalSponsor.name && appConfig.globalSponsor.name.trim() !== "") || appConfig.globalSponsor.image) {
                if (!allSponsors.find(s => s === appConfig.globalSponsor)) {
                     allSponsors.push(appConfig.globalSponsor);
                }
            }
            
            const useSponsors = appConfig.enableSponsorsByNumber && allSponsors.length > 0;
            const rightColumnContent = useSponsors ? allSponsors : allWinners;
            rightTitleEl.textContent = useSponsors ? "Nossos Patrocinadores" : "Vencedores";

            let leftIndex = 0;
            let rightIndex = 0;

            const applyTransition = (el: HTMLElement, state: 'out' | 'in') => {
                const effect = appConfig.sponsorTransitionEffect === 'random' 
                    ? ['fade', 'slide', 'zoom'][Math.floor(Math.random() * 3)] 
                    : appConfig.sponsorTransitionEffect || 'fade';
                
                el.style.transition = 'all 0.5s ease-in-out';
                el.classList.remove('opacity-0', 'translate-x-full', 'scale-50');
                
                if (state === 'out') {
                    if (effect === 'fade') el.classList.add('opacity-0');
                    else if (effect === 'slide') el.classList.add('opacity-0', 'translate-x-full');
                    else if (effect === 'zoom') el.classList.add('opacity-0', 'scale-50');
                }
            };

            const updateContent = () => {
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
                        
                        rightContentEl.innerHTML = '';
                        const itemContainer = document.createElement('div');
                        itemContainer.className = "flex flex-col items-center justify-center bg-black/30 rounded-xl p-8 w-full h-full border border-sky-900/30";
                        
                        if (useSponsors) {
                            if (item.image) {
                                const img = document.createElement('img');
                                img.src = item.image;
                                img.className = "max-w-full max-h-[45vh] object-contain mb-6 drop-shadow-2xl";
                                itemContainer.appendChild(img);
                            }
                            if (item.name) {
                                const p = document.createElement('p');
                                p.className = "text-4xl md:text-5xl text-center font-black text-amber-400";
                                p.textContent = item.name;
                                itemContainer.appendChild(p);
                            }
                        } else {
                            if (item.name) {
                                const pName = document.createElement('p');
                                pName.className = "text-4xl md:text-5xl text-center font-bold text-slate-100 mb-4";
                                pName.textContent = item.name;
                                itemContainer.appendChild(pName);
                            }
                            if (item.prize) {
                                const pPrize = document.createElement('p');
                                pPrize.className = "text-5xl md:text-6xl text-center font-black text-amber-400";
                                pPrize.textContent = item.prize;
                                itemContainer.appendChild(pPrize);
                            }
                        }
                        
                        rightContentEl.appendChild(itemContainer);
                        applyTransition(rightContentEl, 'in');
                        rightIndex++;
                    }, 500);
                } else {
                     rightContentEl.innerHTML = \`<div class="flex flex-col items-center justify-center h-full w-full"><p class="text-3xl text-slate-400">Nenhum dado cadastrado.</p></div>\`;
                }
            };
            
            const updateClock = () => {
                clockEl.textContent = new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
            };

            updateContent();
            updateClock();
            
            if (intervalContentInterval) clearInterval(intervalContentInterval);
            if (intervalClockInterval) clearInterval(intervalClockInterval);
            if (breakConfettiInterval) clearInterval(breakConfettiInterval);
            
            const cycleTime = (appConfig.sponsorDisplaySeconds || 8) * 1000;
            intervalContentInterval = setInterval(updateContent, cycleTime);
            intervalClockInterval = setInterval(updateClock, 1000);
            
            document.getElementById('close-break-modal-btn')!.onclick = () => {
                DOMElements.eventBreakModal.classList.add('hidden');
                clearInterval(intervalContentInterval);
                clearInterval(intervalClockInterval);
                clearInterval(breakConfettiInterval);
                DOMElements.confettiCanvas.style.zIndex = '50';
            };
        }`;

if(regex.test(code)) {
    code = code.replace(regex, newLogic);
    fs.writeFileSync('index.tsx', code);
    console.log("REPLACED showIntervalModal!");
} else {
    console.log("REGEX FAILED for showIntervalModal");
}
