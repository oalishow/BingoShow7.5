import re

with open("index.tsx") as f:
    content = f.read()

# When loading appConfig, let's just forcefully set it to 3 or let the user change it.
# Actually, the user can just change it in the Settings, but I can enforce it to default to 3 if it was 5.
replacement = """                this.state.versionHistory = state.versionHistory || this.state.versionHistory;
                const loadedConfig = state.appConfig || {};
                
                // Força o tempo de exibição do número para 3 segundos se estiver em 5 (atendendo ao pedido)
                if (loadedConfig.modalAutocloseSeconds === 5) {
                    loadedConfig.modalAutocloseSeconds = 3;
                }
"""

content = content.replace("""                this.state.versionHistory = state.versionHistory || this.state.versionHistory;
                const loadedConfig = state.appConfig || {};""", replacement)

with open("index.tsx", "w") as f:
    f.write(content)
