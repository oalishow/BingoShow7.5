import re

with open('index.tsx', 'r') as f:
    content = f.read()

# Remove the Info Column if !includeQr, or change CSS class based on it
# And replace the grid structure.

old_grid = """                                <!-- Info Column (Right side) -->
                                <div class="w-[28%] flex flex-col items-center bg-white p-[2px] justify-between flex-shrink-0 min-h-0">
                                    <div class="text-[7px] font-bold leading-tight uppercase mb-[1px] text-center px-1">Acompanhe ao<br>vivo</div>
                                    <img src="${qrDataUrl}" alt="QR" class="w-20 h-20 border-[2px] border-black object-contain bg-white" />
                                    <div class="text-[4px] text-gray-500 uppercase tracking-widest break-all font-mono mb-[2px]">ID: ${uuid.substring(0,8)}</div>
                                    
                                    <!-- Premiações abaixo do QR Code -->
                                    <div class="flex-grow w-full border-t-[2px] border-black pt-0.5 px-0 flex flex-col gap-[1px] mt-auto bg-gray-50 overflow-hidden">
                                        <div class="text-[5px] font-black uppercase text-center w-full leading-tight bg-gray-200 border border-black py-[1px]">Premiações</div>
                                        ${gridSideText}
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                });"""

new_grid = """                                <!-- Info Column (Right side) -->
                                ${includeQr ? `
                                <div class="w-[28%] flex flex-col items-center bg-white p-[2px] justify-between flex-shrink-0 min-h-0">
                                    <div class="text-[7px] font-bold leading-tight uppercase mb-[1px] text-center px-1">Acompanhe ao<br>vivo</div>
                                    <img src="${qrDataUrl}" alt="QR" class="w-20 h-20 border-[2px] border-black object-contain bg-white" />
                                    <div class="text-[4px] text-gray-500 uppercase tracking-widest break-all font-mono mb-[2px]">ID: ${uuid.substring(0,8)}</div>
                                    
                                    <!-- Premiações abaixo do QR Code -->
                                    <div class="flex-grow w-full border-t-[2px] border-black pt-0.5 px-0 flex flex-col gap-[1px] mt-auto bg-gray-50 overflow-hidden">
                                        <div class="text-[5px] font-black uppercase text-center w-full leading-tight bg-gray-200 border border-black py-[1px]">Premiações</div>
                                        ${gridSideText}
                                    </div>
                                </div>
                                ` : `
                                <div class="w-[28%] flex flex-col items-center bg-white p-1 flex-shrink-0 min-h-0 bg-gray-50">
                                    <div class="text-[4px] text-gray-500 uppercase tracking-widest break-all font-mono mb-[2px] mt-1 text-center">ID: ${uuid.substring(0,8)}</div>
                                    <div class="flex-grow flex items-center justify-center opacity-10">
                                        <!-- Placeholder if no QR -->
                                        <div class="text-4xl font-black rotate-[-45deg] whitespace-nowrap">BINGO</div>
                                    </div>
                                    <div class="w-full flex flex-col gap-[1px] mt-auto">
                                        <div class="text-[5px] font-black uppercase text-center w-full leading-tight bg-gray-200 border border-black py-[1px]">Premiações</div>
                                        ${gridSideText}
                                    </div>
                                </div>
                                `}
                            </div>
                        </div>
                    `;
                });"""

if old_grid in content:
    content = content.replace(old_grid, new_grid)
    print("Grid patched")
else:
    print("Grid not found")

# Fix Left side width
old_left = """                                <!-- 5x5 GRID Layout (Left side) -->
                                <div class="w-[72%] flex flex-col border-r-[2px] border-black">"""
new_left = """                                <!-- 5x5 GRID Layout (Left side) -->
                                <div class="w-[72%] flex flex-col border-r-[2px] border-black">"""

content = content.replace(old_left, new_left)

old_chunk = """                        <!-- MAIN GRIDS -->
                        <div class="flex-grow grid grid-cols-2 grid-rows-3 gap-1 pb-1 relative min-h-0">
                             ${resolvedBatchHTML.join('')}
                        </div>
                        
                        <!-- MASTER BOTTOM STUB -->
                        <div class="border-[2px] border-black mt-auto flex flex-col uppercase text-[9px] font-bold leading-none flex-shrink-0 bg-white">"""

new_chunk = """                        <!-- MAIN GRIDS -->
                        <div class="flex-grow grid gap-1 pb-1 relative min-h-0 ${cardsPerPage === 1 ? 'grid-cols-1 grid-rows-1' : cardsPerPage === 2 ? 'grid-cols-1 grid-rows-2' : cardsPerPage === 4 ? 'grid-cols-2 grid-rows-2' : 'grid-cols-2 grid-rows-3'}">
                             ${resolvedBatchHTML.join('')}
                        </div>
                        
                        ${extraInstructions ? `<div class="border-[2px] border-black border-b-0 text-center font-bold text-[8px] bg-yellow-100 py-0.5">${extraInstructions}</div>` : ''}

                        <!-- MASTER BOTTOM STUB -->
                        <div class="border-[2px] border-black mt-auto flex flex-col uppercase text-[9px] font-bold leading-none flex-shrink-0 bg-white">"""

if old_chunk in content:
    content = content.replace(old_chunk, new_chunk)
    print("Chunk patched")
else:
    print("Chunk not found")


with open('index.tsx', 'w') as f:
    f.write(content)
