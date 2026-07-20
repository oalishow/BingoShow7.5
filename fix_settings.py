import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""                            <div class="border-b border-gray-700 pb-6">
                                <label class="block text-xl font-bold text-slate-700 dark:text-slate-300 mb-2">\$\{appLabels.settingsBingoTitleLabel\}</label>"""

good_replacement = """                            <div class="border-b border-gray-700 pb-6 mt-6">
                                <h3 class="text-xl font-bold text-slate-700 dark:text-slate-300 mb-2">Segurança (Área Restrita)</h3>
                                <p class="text-sm text-slate-600 dark:text-slate-400 mb-2">Configure uma senha para proteger o acesso ao Gerador de Cartelas e impedir edições indesejadas.</p>
                                <label class="block text-sm font-bold text-slate-700 dark:text-slate-300 mb-1">Senha (PIN de 4 dígitos):</label>
                                <input type="password" id="card-generator-pin-input" maxlength="4" placeholder="Ex: 1234 (Deixe vazio para desativar)" class="w-full md:w-1/2 p-3 bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg focus:ring-sky-500 focus:border-sky-500 font-black tracking-widest">
                            </div>
                            
                            <div class="border-b border-gray-700 pb-6">
                                <label class="block text-xl font-bold text-slate-700 dark:text-slate-300 mb-2">${appLabels.settingsBingoTitleLabel}</label>"""

content = re.sub(bad_pattern, good_replacement, content)

bad_pattern2 = r"""    const enableAutoclose = document.getElementById\('enable-modal-autoclose'\) as HTMLInputElement;"""

good_replacement2 = """    const pinInput = document.getElementById('card-generator-pin-input') as HTMLInputElement;
    if (pinInput) {
        pinInput.value = appConfig.cardGeneratorPin || '';
        pinInput.addEventListener('input', (e) => {
            let val = (e.target as HTMLInputElement).value.replace(/[^0-9]/g, '');
            if (val.length > 4) val = val.substring(0, 4);
            (e.target as HTMLInputElement).value = val;
            appStore.state.appConfig.cardGeneratorPin = val;
            appStore.debouncedSave();
        });
    }

    const enableAutoclose = document.getElementById('enable-modal-autoclose') as HTMLInputElement;"""

content = re.sub(bad_pattern2, good_replacement2, content)


with open('index.tsx', 'w') as f:
    f.write(content)
