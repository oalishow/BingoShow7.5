import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""                                            <div class="flex-1 text-left text-sm font-bold text-slate-500 dark:text-slate-400">Total de Grades:</div>\s*<input type="number" id="card-quantity" placeholder="Ex: 120 \(rendem 20 folhas\)" value="120" class="w-48 text-center text-lg font-bold p-3 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500">"""

good_replacement = """                                            <div class="flex-1 text-left text-sm font-bold text-slate-500 dark:text-slate-400">Total de Grades:</div>
                                            <input type="number" id="card-quantity" placeholder="Ex: 120 (rendem 20 folhas)" value="120" class="w-32 text-center text-lg font-bold p-3 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500">
                                       </div>
                                       
                                       <div class="flex items-center justify-between gap-2">
                                            <div class="flex-1 text-left text-sm font-bold text-slate-500 dark:text-slate-400">Layout de Impressão:</div>
                                            <select id="card-cards-per-page" class="w-48 text-center text-sm font-bold p-3 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500">
                                                <option value="auto">Automático</option>
                                                <option value="1">1 por Folha</option>
                                                <option value="2">2 por Folha</option>
                                                <option value="4">4 por Folha</option>
                                                <option value="6">6 por Folha (Padrão)</option>
                                                <option value="8">8 por Folha</option>
                                            </select>"""

content = re.sub(bad_pattern, good_replacement, content)

bad_pattern2 = r"""                                       <div class="flex items-center gap-2 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">\s*<input type="checkbox" id="card-save-template" class="w-5 h-5 rounded cursor-pointer focus:ring-2 focus:ring-sky-500 accent-sky-600 border-gray-300">\s*<label class="text-slate-700 dark:text-slate-300 font-bold cursor-pointer flex-1" for="card-save-template">Salvar estas configurações como padrão</label>\s*</div>"""

good_replacement2 = """                                       <div class="flex items-center gap-2 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                           <input type="checkbox" id="card-save-template" class="w-5 h-5 rounded cursor-pointer focus:ring-2 focus:ring-sky-500 accent-sky-600 border-gray-300">
                                           <label class="text-slate-700 dark:text-slate-300 font-bold cursor-pointer flex-1" for="card-save-template">Salvar estas configurações como padrão</label>
                                       </div>
                                       <div class="flex items-center gap-2 border-2 border-slate-300 dark:border-gray-600 bg-white dark:bg-gray-700 p-3 rounded-lg">
                                           <input type="checkbox" id="card-download-backup" checked class="w-5 h-5 rounded cursor-pointer focus:ring-2 focus:ring-sky-500 accent-sky-600 border-gray-300">
                                           <label class="text-slate-700 dark:text-slate-300 font-bold cursor-pointer flex-1" for="card-download-backup">Baixar backup das cartelas (Arquivo HTML)</label>
                                       </div>"""
                                       
content = re.sub(bad_pattern2, good_replacement2, content)

with open('index.tsx', 'w') as f:
    f.write(content)
