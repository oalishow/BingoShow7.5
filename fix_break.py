import re

with open('index.tsx', 'r') as f:
    content = f.read()

content = content.replace('text-6xl font-black text-sky-400', 'text-6xl font-black text-sky-600 dark:text-sky-400')
content = content.replace('<div id="break-left-column" class="flex flex-col items-center bg-black/20 p-6 rounded-xl h-full overflow-hidden min-h-0">', '<div id="break-left-column" class="flex flex-col items-center bg-gray-100 dark:bg-black/20 p-6 rounded-xl border border-gray-200 dark:border-transparent h-full overflow-hidden min-h-0">')
content = content.replace('<div id="break-right-column" class="flex flex-col items-center bg-black/20 p-6 rounded-xl h-full overflow-hidden relative min-h-0">', '<div id="break-right-column" class="flex flex-col items-center bg-gray-100 dark:bg-black/20 p-6 rounded-xl border border-gray-200 dark:border-transparent h-full overflow-hidden relative min-h-0">')
content = content.replace('<h3 id="break-left-title" class="text-5xl font-bold text-amber-400 mb-6 flex-shrink-0">Cardápio</h3>', '<h3 id="break-left-title" class="text-5xl font-bold text-amber-600 dark:text-amber-400 mb-6 flex-shrink-0">Cardápio</h3>')
content = content.replace('<h3 id="break-right-title" class="text-5xl font-bold text-amber-400">Apoio</h3>', '<h3 id="break-right-title" class="text-5xl font-bold text-amber-600 dark:text-amber-400">Apoio</h3>')

bad_pattern_inner = r"""                                if \(item.image\) \{
                                    innerHTML \+= `<div class="w-full flex-1 min-h-0 flex items-center justify-center p-2 md:p-6"><img src="\$\{item.image\}" class="max-w-full max-h-full object-contain drop-shadow-2xl \$\{isFullscreen \? 'transform scale-125' : ''\} transition-transform duration-700"></div>`;
                                \} else \{
                                    innerHTML \+= `<p class="text-6xl md:text-8xl text-center font-black text-amber-400 flex-shrink-0">\$\{item.name \|\| 'Patrocinador'\}</p>`;
                                \}
                            \} else \{
                                rightTitleEl.textContent = "Vencedores";
                                if \(item.name\) \{
                                    innerHTML \+= `<p class="text-5xl md:text-7xl text-center font-bold text-slate-100 mb-6">\$\{item.name\}</p>`;
                                \}
                                if \(item.prize\) \{
                                    innerHTML \+= `<p class="text-6xl md:text-8xl text-center font-black text-amber-400">\$\{item.prize\}</p>`;
                                \}
                            \}
                            
                            rightContentEl.innerHTML = `<div class="flex flex-col items-center justify-center bg-black/40 rounded-xl p-4 md:p-8 w-full h-full border border-sky-900/40 shadow-xl overflow-hidden min-h-0">\$\{innerHTML\}</div>`;"""

good_replacement_inner = """                                if (item.image) {
                                    innerHTML += `<div class="w-full flex-1 min-h-0 flex items-center justify-center p-2 md:p-6"><img src="${item.image}" class="max-w-full max-h-full object-contain drop-shadow-2xl ${isFullscreen ? 'transform scale-125' : ''} transition-transform duration-700"></div>`;
                                } else {
                                    innerHTML += `<p class="text-6xl md:text-8xl text-center font-black text-amber-600 dark:text-amber-400 flex-shrink-0">${item.name || 'Patrocinador'}</p>`;
                                }
                            } else {
                                rightTitleEl.textContent = "Vencedores";
                                if (item.name) {
                                    innerHTML += `<p class="text-5xl md:text-7xl text-center font-bold text-gray-800 dark:text-slate-100 mb-6">${item.name}</p>`;
                                }
                                if (item.prize) {
                                    innerHTML += `<p class="text-6xl md:text-8xl text-center font-black text-amber-600 dark:text-amber-400">${item.prize}</p>`;
                                }
                            }
                            
                            rightContentEl.innerHTML = `<div class="flex flex-col items-center justify-center bg-white dark:bg-black/40 rounded-xl p-4 md:p-8 w-full h-full border border-gray-300 dark:border-sky-900/40 shadow-xl overflow-hidden min-h-0">${innerHTML}</div>`;"""

content = re.sub(bad_pattern_inner, good_replacement_inner, content)

with open('index.tsx', 'w') as f:
    f.write(content)
