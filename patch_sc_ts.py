import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_logic = """            const called = game.calledNumbers;
            if (called.length > 0) {
                const last = called[called.length - 1];
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.innerHTML = `<span class="text-6xl text-teal-400 font-bold mr-2">${getLetterForNumber(last)}</span>${last}`;
            } else {
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.textContent = "--";
            }"""

new_logic = """            const appConfig = appStore.state.appConfig;
            const called = game.calledNumbers;
            
            if (called.length > 0) {
                const last = called[called.length - 1];
                const letter = getLetterForNumber(last);
                
                const roundColor = game.color;
                const mainColor = appConfig.drawnTextColor || '#ffffff';
                const strokeColor = appConfig.drawnTextStrokeColor || '#000000';
                const strokeWidth = appConfig.drawnTextStrokeWidth || 4;
                const strokeStyle = `${strokeWidth}px ${strokeColor}`;

                const isDarkTheme = document.documentElement.classList.contains('dark');
                const defaultBg = isDarkTheme ? '#1e293b' : '#f1f5f9';
                const bgColor = roundColor || (appConfig.boardColor && appConfig.boardColor !== 'default' ? appConfig.boardColor : defaultBg);

                if (DOMElements.scLastNumber) {
                    DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center gap-x-2 rounded-full aspect-square w-48 sm:w-56 transition-all duration-300" style="font-size: 4rem; line-height: 1; background-color: ${bgColor}; color: ${mainColor}; -webkit-text-stroke: ${strokeStyle}; box-shadow: 0 0 30px 10px ${bgColor}80;"><span>${letter}</span><span>${last}</span></div>`;
                }
            } else {
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center rounded-full aspect-square w-48 sm:w-56 bg-slate-800/50 text-slate-500 border-4 border-slate-700/50 shadow-inner" style="font-size: 4rem;">--</div>`;
            }"""

content = content.replace(old_logic, new_logic)

with open('index.tsx', 'w') as f:
    f.write(content)
print("sc ts patched")
