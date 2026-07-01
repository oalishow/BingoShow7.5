const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regex = /if \(uniqueSponsors\.length > 0\) \{[\s\S]*?\} else \{[\s\S]*?document\.getElementById\('final-sponsors-section'\)!\.classList\.add\('hidden'\);\s*\}/;

const replacement = `
    let finalSponsorsInterval: any;
    
    if (uniqueSponsors.length > 0) {
        document.getElementById('final-sponsors-section')!.classList.remove('hidden');
        let sponsorIndex = 0;
        
        const applyTransition = (el: HTMLElement, state: 'out' | 'in') => {
            const effect = appStore.state.appConfig.sponsorTransitionEffect === 'random' 
                ? ['fade', 'slide', 'zoom'][Math.floor(Math.random() * 3)] 
                : appStore.state.appConfig.sponsorTransitionEffect || 'fade';
            
            el.style.transition = 'all 0.5s ease-in-out';
            el.classList.remove('opacity-0', 'translate-x-full', 'scale-50');
            
            if (state === 'out') {
                if (effect === 'fade') el.classList.add('opacity-0');
                else if (effect === 'slide') el.classList.add('opacity-0', 'translate-x-full');
                else if (effect === 'zoom') el.classList.add('opacity-0', 'scale-50');
            }
        };

        const cycleFinalSponsors = () => {
            applyTransition(sponsorsList, 'out');
            setTimeout(() => {
                const s = uniqueSponsors[sponsorIndex % uniqueSponsors.length];
                sponsorsList.innerHTML = \`
                    <img src="\${s.image}" alt="\${s.name}" class="w-24 h-24 object-contain rounded-md bg-white p-1 mb-2">
                    <span class="text-lg font-bold text-slate-700 dark:text-slate-300">\${s.name}</span>
                \`;
                applyTransition(sponsorsList, 'in');
                sponsorIndex++;
            }, 500);
        };
        
        cycleFinalSponsors();
        const cycleTime = (appStore.state.appConfig.sponsorDisplaySeconds || 8) * 1000;
        finalSponsorsInterval = setInterval(cycleFinalSponsors, cycleTime);
    } else {
        document.getElementById('final-sponsors-section')!.classList.add('hidden');
    }
`;

code = code.replace(regex, replacement);

// Also need to clear the interval when closing modal
code = code.replace(
    'if (finalConfettiInterval) clearInterval(finalConfettiInterval);',
    'if (finalConfettiInterval) clearInterval(finalConfettiInterval);\n        if (typeof finalSponsorsInterval !== "undefined" && finalSponsorsInterval) clearInterval(finalSponsorsInterval);'
);

// We need to define finalSponsorsInterval higher up or globally to be accessible?
// It's defined inside showFinalWinnersModal, so the clear inside the click handler will see it.
fs.writeFileSync('index.tsx', code);
