import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_logic = """                    if (updateSW) {
                        try {
                            await updateSW(true);
                        } catch (e) {
                            console.error('Failed to update SW:', e);
                        }
                    }
                    window.location.reload();"""

new_logic = """                    if (updateSW) {
                        try {
                            await updateSW(true);
                        } catch (e) {
                            console.error('Failed to update SW:', e);
                            window.location.reload(); // fallback
                        }
                    }"""

content = content.replace(old_logic, new_logic)

with open('index.tsx', 'w') as f:
    f.write(content)
print("PWA patched")
