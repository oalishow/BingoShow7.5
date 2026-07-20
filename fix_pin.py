import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"        function showCardGeneratorModal\(\) \{"
good_replacement = """        function showCardGeneratorModal() {
             const pin = appStore.state.appConfig.cardGeneratorPin;
             if (pin) {
                 const entered = prompt("Digite a senha de 4 dígitos para acessar o Gerador de Cartelas:");
                 if (entered !== pin) {
                     showAlert("Senha incorreta!");
                     return;
                 }
             }
"""
content = re.sub(bad_pattern, good_replacement, content)

with open('index.tsx', 'w') as f:
    f.write(content)
