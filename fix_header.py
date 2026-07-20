import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""                        <!-- MASTER HEADER -->\s*<div class="border-\[2px\] border-black mb-1 flex flex-col flex-shrink-0">\s*<h1 class="text-center font-black text-3xl uppercase py-1\.5 m-0 leading-none tracking-widest" style="background-color: \$\{cardColor\}; color: \$\{headerTextColor\};">\s*\$\{title\}\s*</h1>\s*<div class="flex border-t-\[2px\] border-black text-\[9px\] font-bold uppercase divide-x-\[2px\] divide-black">\s*<div class="flex-1 px-1 py-1 flex items-center">ONDE:&nbsp;<span class="font-normal border-b border-black flex-grow ml-1 min-w-\[20px\] truncate">\$\{locationVal\}</span></div>\s*<div class="w-32 px-1 py-1 flex items-center">DATA:&nbsp;<span class="font-normal border-b border-black flex-grow ml-1 min-w-\[20px\] truncate">\$\{dateVal\}</span></div>"""

good_replacement = """                        <!-- MASTER HEADER -->
                        <div class="border-[2px] border-black mb-1 flex flex-col flex-shrink-0">
                            ${optTitle ? `
                            <h1 class="text-center font-black text-3xl uppercase py-1.5 m-0 leading-none tracking-widest" style="background-color: ${cardColor}; color: ${headerTextColor};">
                                ${title}
                            </h1>
                            ` : ''}
                            <div class="flex border-t-[2px] border-black text-[9px] font-bold uppercase divide-x-[2px] divide-black">
                                ${optLocDate ? `
                                <div class="flex-1 px-1 py-1 flex items-center">ONDE:&nbsp;<span class="font-normal border-b border-black flex-grow ml-1 min-w-[20px] truncate">${locationVal}</span></div>
                                <div class="w-32 px-1 py-1 flex items-center">DATA:&nbsp;<span class="font-normal border-b border-black flex-grow ml-1 min-w-[20px] truncate">${dateVal}</span></div>
                                ` : '<div class="flex-1 bg-white"></div>'}"""

content = re.sub(bad_pattern, good_replacement, content)

bad_pattern2 = r"""                        <!-- MASTER BOTTOM STUB -->\s*<div class="border-\[2px\] border-black mt-auto flex flex-col uppercase text-\[9px\] font-bold leading-none flex-shrink-0 bg-white">\s*<div class="flex border-b-\[2px\] border-black divide-x-\[2px\] divide-black bg-gray-100">\s*<div class="flex-1 px-2 py-1 flex items-center justify-center"><span class="font-black text-sm tracking-widest truncate max-w-\[250px\]">\$\{title\}</span></div>\s*<div class="w-28 px-2 py-1 flex items-center">VALOR:&nbsp;<span class="font-black text-xs ml-auto min-w-\[20px\]">\$\{priceVal\}</span></div>"""

good_replacement2 = """                        <!-- MASTER BOTTOM STUB -->
                        <div class="border-[2px] border-black mt-auto flex flex-col uppercase text-[9px] font-bold leading-none flex-shrink-0 bg-white">
                            <div class="flex border-b-[2px] border-black divide-x-[2px] divide-black bg-gray-100">
                                 ${optTitle ? `
                                 <div class="flex-1 px-2 py-1 flex items-center justify-center"><span class="font-black text-sm tracking-widest truncate max-w-[250px]">${title}</span></div>
                                 ` : '<div class="flex-1 bg-gray-100"></div>'}
                                 
                                 ${optPrice ? `
                                 <div class="w-28 px-2 py-1 flex items-center">VALOR:&nbsp;<span class="font-black text-xs ml-auto min-w-[20px]">${priceVal}</span></div>
                                 ` : ''}"""

content = re.sub(bad_pattern2, good_replacement2, content)

with open('index.tsx', 'w') as f:
    f.write(content)
