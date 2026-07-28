import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """        function updateBlockedUsersUI() {"""

new_code = """        (window as any).updateBlockedUsersUI = function updateBlockedUsersUI() {"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch window function successful!")
else:
    print("Old window function not found!")

old_code_2 = """    if (typeof updateBlockedUsersUI === 'function') {
        updateBlockedUsersUI();
    }"""

new_code_2 = """    if (typeof (window as any).updateBlockedUsersUI === 'function') {
        (window as any).updateBlockedUsersUI();
    }"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch showSettingsModal window call successful!")
else:
    print("Old showSettingsModal window call not found!")
