import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """                            <div class="border-b border-slate-300 dark:border-gray-700 pb-6 mt-6">
                                <h3 class="text-xl font-bold text-slate-700 dark:text-slate-300 mb-2">🎈 Etapa 2: Online Sync</h3>
                                <p class="text-sm text-slate-600 dark:text-slate-400 mb-2">Ative o modo Online para permitir que os jogadores acessem suas cartelas diretamente pelo celular escaneando o QR Code. Ao ativar, você precisará aguardar a sincronização (host online).</p>
                                <div class="flex items-center gap-3 bg-indigo-100 dark:bg-indigo-900/50 p-3 rounded-lg border border-indigo-200 dark:border-indigo-800 mb-2">
                                    <input type="checkbox" id="online-sync-toggle" class="h-5 w-5 rounded border-indigo-300 text-indigo-600 focus:ring-indigo-500">
                                    <label for="online-sync-toggle" class="text-slate-800 dark:text-indigo-200 font-bold">Ativar Sincronização em Nuvem</label>
                                </div>"""

new_code = """                            <div class="border-b border-slate-300 dark:border-gray-700 pb-6 mt-6">
                                <h3 class="text-xl font-bold text-slate-700 dark:text-slate-300 mb-2">🎈 Etapa 2: Online Sync</h3>
                                <p class="text-sm text-slate-600 dark:text-slate-400 mb-2">Ative o modo Online para permitir que os jogadores acessem suas cartelas diretamente pelo celular escaneando o QR Code. Ao ativar, você precisará aguardar a sincronização (host online).</p>
                                
                                <div class="flex flex-col sm:flex-row gap-3 mb-4">
                                    <button id="host-login-facebook-btn" class="flex items-center justify-center gap-2 bg-[#1877F2] text-white hover:bg-[#166FE5] py-2 px-4 rounded-lg font-bold transition-colors shadow-sm">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                                        Logar Facebook
                                    </button>
                                    <button id="host-logout-btn" class="hidden flex items-center justify-center gap-2 bg-red-600 text-white hover:bg-red-700 py-2 px-4 rounded-lg font-bold transition-colors shadow-sm">
                                        Desconectar
                                    </button>
                                </div>
                                <div id="host-user-info" class="text-sm font-bold text-slate-700 dark:text-slate-300 mb-4 hidden"></div>

                                <div class="flex items-center gap-3 bg-indigo-100 dark:bg-indigo-900/50 p-3 rounded-lg border border-indigo-200 dark:border-indigo-800 mb-2">
                                    <input type="checkbox" id="online-sync-toggle" class="h-5 w-5 rounded border-indigo-300 text-indigo-600 focus:ring-indigo-500">
                                    <label for="online-sync-toggle" class="text-slate-800 dark:text-indigo-200 font-bold">Ativar Sincronização em Nuvem</label>
                                </div>"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch UI successful!")
else:
    print("Old UI code not found!")
