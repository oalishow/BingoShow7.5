import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """                            <button id="tab-appearance" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-sky-500 text-sky-400">${appLabels.settingsTabAppearance}</button>
                            <button id="tab-sponsors" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-transparent text-gray-400 hover:text-gray-200 hover:border-gray-500">${appLabels.settingsTabSponsors}</button>
                            <button id="tab-labels" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-transparent text-gray-400 hover:text-gray-200 hover:border-gray-500">${appLabels.settingsTabLabels}</button>
                            <button id="tab-shortcuts" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-transparent text-gray-400 hover:text-gray-200 hover:border-gray-500">${appLabels.settingsTabShortcuts}</button>
                        </nav>
                    </div>

                    <div id="settings-content-container" class="max-h-[60vh] overflow-y-auto pr-4">"""

new_code = """                            <button id="tab-appearance" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-sky-500 text-sky-400">${appLabels.settingsTabAppearance}</button>
                            <button id="tab-sponsors" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-transparent text-gray-400 hover:text-gray-200 hover:border-gray-500">${appLabels.settingsTabSponsors}</button>
                            <button id="tab-labels" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-transparent text-gray-400 hover:text-gray-200 hover:border-gray-500">${appLabels.settingsTabLabels}</button>
                            <button id="tab-shortcuts" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-transparent text-gray-400 hover:text-gray-200 hover:border-gray-500">${appLabels.settingsTabShortcuts}</button>
                            <button id="tab-security" class="whitespace-nowrap py-4 px-1 border-b-2 font-medium text-lg border-transparent text-gray-400 hover:text-gray-200 hover:border-gray-500">Segurança</button>
                        </nav>
                    </div>

                    <div id="settings-content-container" class="max-h-[60vh] overflow-y-auto pr-4">
                        <div id="tab-content-security" class="hidden space-y-6 text-left">
                            <h3 class="text-xl font-bold text-slate-700 dark:text-slate-300 mb-2">Usuários Bloqueados</h3>
                            <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">Gerencie os usuários que foram bloqueados por falsos alertas de BINGO.</p>
                            <div id="blocked-users-list" class="space-y-2"></div>
                        </div>"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch settings tabs successful!")
else:
    print("Old settings tabs not found!")

old_code_2 = """    const tabs = ['appearance', 'sponsors', 'labels', 'shortcuts'];"""

new_code_2 = """    const tabs = ['appearance', 'sponsors', 'labels', 'shortcuts', 'security'];"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch tabs list successful!")
else:
    print("Old tabs list not found!")
