import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"globalStatusEl\.innerHTML = `✅ Nuvem Ativa \(ID: \$\{eventId\}\)`;"
good_replacement = r"globalStatusEl.innerHTML = `<div class=\"cursor-pointer select-none flex items-center\" onclick=\"const idEl = document.getElementById('event-id-display'); if(idEl) idEl.classList.toggle('hidden');\">✅ Modo Online <span id=\"event-id-display\" class=\"hidden text-xs ml-2 opacity-80 font-normal\">ID: ${eventId}</span></div>`;"

content = re.sub(bad_pattern, good_replacement, content)

bad_pattern2 = r"this.state.versionHistory = state.versionHistory \|\| this.state.versionHistory;"
good_replacement2 = r"this.state.versionHistory = state.versionHistory || this.state.versionHistory;\n                if (!this.state.versionHistory.includes('v7.6')) this.state.versionHistory = currentVersionHistory;"

# Let's define the currentVersionHistory at the top so it's always up to date if migrated
bad_pattern_history = r"versionHistory: `\*\*v7\.3\.0 \(Atual\)\*\*"
good_replacement_history = r"versionHistory: `**v7.6.0 (Atual)**\n- **MODO CLARO OTIMIZADO:** Melhoria na legibilidade dos patrocinadores e cardápio durante o modo claro no painel de intervalo.\n- **SEGURANÇA:** Inclusão de senha opcional de 4 dígitos para proteger o Gerador de Cartelas.\n- **LAYOUT DE IMPRESSÃO:** Novas opções automáticas e manuais para impressão de cartelas em PDF.\n- **CÓDIGO DE CARTELAS:** Código de verificação (CÓD) reduzido para 4 caracteres visando facilitar a checagem manual.\n- **BACKUP:** Download automático de cartelas geradas via HTML para evitar perda.\n\n**v7.3.0**"

content = re.sub(bad_pattern_history, good_replacement_history, content)

bad_pattern_ver = r"const currentVersion = \"7\.5\"; // Foco 100% Local"
good_replacement_ver = r"const currentVersion = \"7.6\"; // Otimizações"

content = re.sub(bad_pattern_ver, good_replacement_ver, content)

with open('index.tsx', 'w') as f:
    f.write(content)
