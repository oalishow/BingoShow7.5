import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"this\.state\.versionHistory = state\.versionHistory \|\| this\.state\.versionHistory;"
good_replacement = r"""this.state.versionHistory = state.versionHistory || this.state.versionHistory;
                if (!this.state.versionHistory.includes('v7.6')) {
                    this.state.versionHistory = `**v7.6.0 (Atual)**
- **MODO CLARO OTIMIZADO:** Melhoria na legibilidade dos patrocinadores e cardápio durante o modo claro no painel de intervalo.
- **SEGURANÇA:** Inclusão de senha opcional de 4 dígitos para proteger o Gerador de Cartelas.
- **LAYOUT DE IMPRESSÃO:** Novas opções automáticas e manuais para impressão de cartelas em PDF.
- **CÓDIGO DE CARTELAS:** Código de verificação (CÓD) reduzido para 4 caracteres visando facilitar a checagem manual.
- **BACKUP:** Download automático de cartelas geradas via HTML para evitar perda.

` + this.state.versionHistory.replace('(Atual)', '');
                }"""

content = re.sub(bad_pattern, good_replacement, content)

with open('index.tsx', 'w') as f:
    f.write(content)
