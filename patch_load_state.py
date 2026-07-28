import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """                this.state.activeGameNumber = state.activeGameNumber || null;
                this.state.menuItems = state.menuItems || [ "Refrigerante - R$ 5,00", "Cerveja - R$ 7,00", "Água - R$ 3,00", "Espetinho - R$ 8,00", "Pastel - R$ 6,00", "Porção de Fritas - R$ 15,00" ];
                this.state.drawnPrizeNumbers = state.drawnPrizeNumbers || [];"""

new_code = """                this.state.activeGameNumber = state.activeGameNumber || null;
                this.state.menuItems = state.menuItems || [ "Refrigerante - R$ 5,00", "Cerveja - R$ 7,00", "Água - R$ 3,00", "Espetinho - R$ 8,00", "Pastel - R$ 6,00", "Porção de Fritas - R$ 15,00" ];
                this.state.drawnPrizeNumbers = state.drawnPrizeNumbers || [];
                this.state.blockedUsers = state.blockedUsers || [];"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch loadStateFromObject successful!")
else:
    print("Old loadStateFromObject not found!")
