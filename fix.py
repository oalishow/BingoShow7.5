import re

with open('index.tsx', 'r') as f:
    content = f.read()

# Fix the BINGO Numbers header deletion
bad_pattern1 = r"<!-- 5x5 GRID Layout \(Left side\) -->\s*<!-- BINGO Numbers -->"
good_replacement1 = """<!-- 5x5 GRID Layout (Left side) -->
                                <div class="w-[72%] flex flex-col border-r-[2px] border-black">
                                    <!-- BINGO Header -->
                                    <div class="grid grid-cols-5 border-b-[2px] border-black bg-gray-100 flex-shrink-0">
                                        ${['B', 'I', 'N', 'G', 'O'].map((letter, colIndex) => `
                                            <div class="font-black text-[11px] uppercase flex items-center justify-center py-0.5 ${colIndex === 4 ? '' : 'border-r-[2px] border-black'}">${letter}</div>
                                        `).join('')}
                                    </div>
                                    <!-- BINGO Numbers -->"""
content = re.sub(bad_pattern1, good_replacement1, content)

# Fix the duplicate block at the end
bad_pattern2 = r"                }\);\s*<!-- Premiações abaixo do QR Code -->\s*<div class=\"flex-grow w-full border-t-\[2px\] border-black pt-0\.5 px-0 flex flex-col gap-\[1px\] mt-auto bg-gray-50 overflow-hidden\">\s*<div class=\"text-\[5px\] font-black uppercase text-center w-full leading-tight bg-gray-200 border border-black py-\[1px\]\">Premiações</div>\s*\$\{gridSideText\}\s*</div>\s*</div>\s*</div>\s*</div>\s*`;\s*}\);"
good_replacement2 = "                });"

content = re.sub(bad_pattern2, good_replacement2, content)

with open('index.tsx', 'w') as f:
    f.write(content)
