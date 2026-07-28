import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """    tabs.forEach(tabId => {
        document.getElementById(`tab-${tabId}`)!.addEventListener('click', () => switchTab(tabId));
    });

    // --- Appearance Tab ---"""

new_code = """    tabs.forEach(tabId => {
        document.getElementById(`tab-${tabId}`)!.addEventListener('click', () => switchTab(tabId));
    });

    if (typeof updateBlockedUsersUI === 'function') {
        updateBlockedUsersUI();
    }

    // --- Appearance Tab ---"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch showSettingsModal successful!")
else:
    print("Old showSettingsModal not found!")
