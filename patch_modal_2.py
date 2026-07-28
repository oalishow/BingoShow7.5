import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_modal = """                                        <div class="flex items-center justify-between border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                            <label class="text-slate-700 dark:text-slate-300 font-bold" for="card-color">Cor das Cartelas:</label>
                                            <input type="color" id="card-color" value="#000000" class="w-12 h-10 p-0 border-0 rounded cursor-pointer">
                                        </div>
                                        <div class="flex items-center gap-2 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                            <input type="checkbox" id="card-reset-series" class="w-5 h-5 rounded cursor-pointer focus:ring-2 focus:ring-sky-500 accent-sky-600 border-gray-300">
                                            <label class="text-slate-700 dark:text-slate-300 font-bold cursor-pointer" for="card-reset-series">Zerar numeração de série na geração</label>
                                        </div>
                                    </div>
                                    <div class="flex justify-center gap-4 mb-4">
                                         <button id="generate-and-print-cards-btn" class="bg-sky-600 hover:bg-sky-700 text-white font-bold py-3 px-8 rounded-full text-lg w-full">Gerar e Imprimir</button>"""

new_modal = """                                        <div class="flex flex-col sm:flex-row gap-2">
                                            <div class="flex-1 flex items-center justify-between border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                                <label class="text-slate-700 dark:text-slate-300 font-bold" for="card-color">Cor das Cartelas:</label>
                                                <input type="color" id="card-color" value="#000000" class="w-12 h-10 p-0 border-0 rounded cursor-pointer">
                                            </div>
                                            <div class="flex-1 flex items-center justify-between border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                                <label class="text-slate-700 dark:text-slate-300 font-bold" for="card-layout">Layout (A4):</label>
                                                <select id="card-layout" class="text-sm font-bold bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 rounded p-1 outline-none">
                                                    <option value="6">6 por folha</option>
                                                    <option value="4">4 por folha</option>
                                                    <option value="2">2 por folha</option>
                                                    <option value="1">1 por folha</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="flex flex-col gap-2 mt-2">
                                            <div class="flex items-center gap-2 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                                <input type="checkbox" id="card-include-qr" checked class="w-5 h-5 rounded cursor-pointer focus:ring-2 focus:ring-sky-500 accent-sky-600 border-gray-300">
                                                <label class="text-slate-700 dark:text-slate-300 font-bold cursor-pointer" for="card-include-qr">Incluir QR Code (Jogar pelo Celular)</label>
                                            </div>
                                            <div class="flex items-center gap-2 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                                <input type="checkbox" id="card-include-logo" checked class="w-5 h-5 rounded cursor-pointer focus:ring-2 focus:ring-sky-500 accent-sky-600 border-gray-300">
                                                <label class="text-slate-700 dark:text-slate-300 font-bold cursor-pointer" for="card-include-logo">Exibir Logo do Evento (se configurada)</label>
                                            </div>
                                            <div class="flex items-center gap-2 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                                <input type="checkbox" id="card-reset-series" class="w-5 h-5 rounded cursor-pointer focus:ring-2 focus:ring-sky-500 accent-sky-600 border-gray-300">
                                                <label class="text-slate-700 dark:text-slate-300 font-bold cursor-pointer" for="card-reset-series">Zerar numeração de série na geração</label>
                                            </div>
                                        </div>
                                        <div class="mt-2">
                                            <input type="text" id="card-extra-instructions" placeholder="Instruções Extras / Regras (Ex: Proibido menores de 18 anos)" class="w-full text-sm font-bold p-3 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500">
                                        </div>
                                    </div>
                                    <div class="flex justify-center gap-4 mb-4">
                                         <button id="generate-and-print-cards-btn" class="bg-sky-600 hover:bg-sky-700 text-white font-bold py-3 px-8 rounded-full text-lg w-full shadow-lg transition-transform active:scale-95">Gerar e Imprimir</button>"""

if old_modal in content:
    content = content.replace(old_modal, new_modal)
    print("Modal patched")
else:
    print("Old modal not found")
    
with open('index.tsx', 'w') as f:
    f.write(content)
