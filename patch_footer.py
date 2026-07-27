import re

with open("attendee.html") as f:
    html = f.read()

new_footer = """        <footer class="text-center py-6 px-4 text-xs text-slate-500 font-medium flex-shrink-0 relative z-30 bg-brand-card/50 border-t border-brand-border backdrop-blur-sm mt-auto">
            <p class="max-w-4xl mx-auto">
                Este programa é o resultado do Trabalho de Conclusão de Curso de <a href="https://www.instagram.com/oalison.rodrigues" target="_blank" class="text-brand-text hover:underline">Alison Fernando Rodrigues dos Santos</a>, sob orientação do <a href="https://www.instagram.com/danilonobresant" target="_blank" class="text-brand-text hover:underline">Prof. Pe. Dr. Danilo Nobre dos Santos</a> Título: "E O VERBO SE FEZ I.A.? DA REFLEXÃO TEOLÓGICA E COMUNICATIVA AO DESENVOLVIMENTO DE SOLUÇÕES PASTORAIS COM INTELIGÊNCIA ARTIFICIAL". (<a href="https://drive.google.com/file/d/14uPBeHCT5aP1ACPLlPpIjfD5J1iLQfyD/view?usp=drive_link" target="_blank" class="text-brand-text hover:underline">Link para acessar</a>)
                <br><br>
                Desenvolvido inteiramente com a Inteligência Artificial Gemini 3.1 PRO da Google, este projeto demonstra como é possível criar soluções pastorais inovadoras com criatividade e ferramentas de baixo custo ou gratuitas, mesmo sem conhecimentos prévios em programação.
            </p>
            <div class="flex items-center justify-center gap-3 mt-4">
                <button id="donate-btn-attendee" class="flex items-center gap-1.5 px-4 py-2 bg-amber-500 hover:bg-amber-600 text-white rounded-lg font-bold transition-colors shadow-lg text-sm" data-label-key="supportButton">
                    🤝 <span id="donate-btn-text">Faça sua Doação</span>
                </button>
            </div>
        </footer>"""

# replace the old footer
html = re.sub(r'<footer class="w-full mt-auto flex flex-col items-center gap-3 pt-6 pb-2 text-center relative z-30">.*?</footer>', new_footer, html, flags=re.DOTALL)

with open("attendee.html", "w") as f:
    f.write(html)
