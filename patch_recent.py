import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

# Replace the default "Nenhum número anterior" with "Aguardando início do sorteio..."
content = content.replace(
    """recentNumbersEl.innerHTML = '<span class="text-slate-400 font-bold text-xs sm:text-sm">Nenhum número anterior</span>';""",
    """recentNumbersEl.innerHTML = '<span class="text-slate-400 font-bold text-xs sm:text-sm animate-pulse">⏳ Aguardando Início do Sorteio...</span>';"""
)

with open('attendee.tsx', 'w') as f:
    f.write(content)
print("Attendee recent numbers patched")
