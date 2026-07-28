import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_vis = """        // Tentar verificar por atualizações quando o app ganha foco novamente (útil em mobile)
        window.addEventListener('visibilitychange', () => {
            if (document.visibilityState === 'visible' && 'serviceWorker' in navigator) {
                navigator.serviceWorker.ready.then(reg => {
                    reg.update();
                });
            }
        });"""

content = content.replace(old_vis, "")

with open('index.tsx', 'w') as f:
    f.write(content)
print("PWA visibility check removed")
