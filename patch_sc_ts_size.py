import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_str = """                if (DOMElements.scLastNumber) {
                    DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center gap-x-2 rounded-full aspect-square w-48 sm:w-56 transition-all duration-300" style="font-size: 4rem; line-height: 1; background-color: ${bgColor}; color: ${mainColor}; -webkit-text-stroke: ${strokeStyle}; box-shadow: 0 0 30px 10px ${bgColor}80;"><span>${letter}</span><span>${last}</span></div>`;
                }
            } else {
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center rounded-full aspect-square w-48 sm:w-56 bg-slate-800/50 text-slate-500 border-4 border-slate-700/50 shadow-inner" style="font-size: 4rem;">--</div>`;
            }"""

new_str = """                if (DOMElements.scLastNumber) {
                    DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center gap-x-2 rounded-full aspect-square w-56 sm:w-72 transition-all duration-300" style="font-size: clamp(4.5rem, 15vw, 6rem); line-height: 1; background-color: ${bgColor}; color: ${mainColor}; -webkit-text-stroke: ${strokeStyle}; box-shadow: 0 0 40px 10px ${bgColor};"><span>${letter}</span><span>${last}</span></div>`;
                }
            } else {
                if (DOMElements.scLastNumber) DOMElements.scLastNumber.innerHTML = `<div class="font-black flex justify-center items-center rounded-full aspect-square w-56 sm:w-72 bg-slate-800/50 text-slate-500 border-4 border-slate-700/50 shadow-inner" style="font-size: clamp(4.5rem, 15vw, 6rem);">--</div>`;
            }"""

content = content.replace(old_str, new_str)

with open('index.tsx', 'w') as f:
    f.write(content)
print("sc size patched")
