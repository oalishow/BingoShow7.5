import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_logic = """            if (called.length > 0) {
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
                    DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center gap-x-2 rounded-full aspect-square w-56 sm:w-72 transition-all duration-300" style="font-size: clamp(4.5rem, 15vw, 6rem); line-height: 1; background-color: ${bgColor}; color: ${mainColor}; -webkit-text-stroke: ${strokeStyle}; box-shadow: 0 0 40px 10px ${bgColor};"><span>${letter}</span><span>${last}</span></div>`;
                }
            } else {
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center rounded-full aspect-square w-56 sm:w-72 bg-slate-800/50 text-slate-500 border-4 border-slate-700/50 shadow-inner" style="font-size: clamp(4.5rem, 15vw, 6rem);">--</div>`;
            }"""

new_logic = """            const scLastNumberBall = document.getElementById('sc-last-number-ball');
            if (called.length > 0) {
                const lastNum = called[called.length - 1];
                const letter = getLetterForNumber(lastNum);
                const activeColor = game.color || '#14b8a6';
                if (scLastNumberBall) {
                    scLastNumberBall.style.borderColor = activeColor;
                }
                if (DOMElements.scLastNumber) {
                    DOMElements.scLastNumber.innerHTML = `<span>${letter}</span><span class="ml-1">${lastNum}</span>`;
                    DOMElements.scLastNumber.classList.remove('text-slate-600');
                    DOMElements.scLastNumber.classList.add('text-white');
                }
            } else {
                if (scLastNumberBall) {
                    scLastNumberBall.style.borderColor = '#475569';
                }
                if (DOMElements.scLastNumber) {
                    DOMElements.scLastNumber.innerHTML = `--`;
                    DOMElements.scLastNumber.classList.remove('text-white');
                    DOMElements.scLastNumber.classList.add('text-slate-600');
                }
            }"""

content = content.replace(old_logic, new_logic)

with open('index.tsx', 'w') as f:
    f.write(content)
print("sc ts 2 patched")
