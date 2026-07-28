import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """                drawnPrizeNumbers: [] as number[],
                versionHistory: """

new_code = """                drawnPrizeNumbers: [] as number[],
                blockedUsers: [] as string[],
                versionHistory: """

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch state blockedUsers successful!")
else:
    print("Old state not found!")

old_code_2 = """                    menuItems: this.state.menuItems,
                    drawnPrizeNumbers: this.state.drawnPrizeNumbers,
                    versionText: currentVersion,
                    versionHistory: this.state.versionHistory,"""

new_code_2 = """                    menuItems: this.state.menuItems,
                    drawnPrizeNumbers: this.state.drawnPrizeNumbers,
                    blockedUsers: this.state.blockedUsers,
                    versionText: currentVersion,
                    versionHistory: this.state.versionHistory,"""

if old_code_2 in content:
    content = content.replace(old_code_2, new_code_2)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch save blockedUsers successful!")
else:
    print("Old save not found!")

old_code_3 = """                if (savedState.drawnPrizeNumbers) this.state.drawnPrizeNumbers = savedState.drawnPrizeNumbers;
                if (savedState.appConfig) this.state.appConfig = { ...this.state.appConfig, ...savedState.appConfig };"""

new_code_3 = """                if (savedState.drawnPrizeNumbers) this.state.drawnPrizeNumbers = savedState.drawnPrizeNumbers;
                if (savedState.blockedUsers) this.state.blockedUsers = savedState.blockedUsers;
                if (savedState.appConfig) this.state.appConfig = { ...this.state.appConfig, ...savedState.appConfig };"""

if old_code_3 in content:
    content = content.replace(old_code_3, new_code_3)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch load blockedUsers successful!")
else:
    print("Old load not found!")
