import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""        async function generateAndPrintCards\(\) \{"""

good_replacement = r"""        async function generateAndPrintCards() {
            try {"""

content = re.sub(bad_pattern, good_replacement, content)

bad_pattern2 = r"""            // Auto close modal
            DOMElements\.cardGeneratorModal\.classList\.add\('hidden'\);
        \}

        function showCardGeneratorModal\(\) \{"""

good_replacement2 = r"""            // Auto close modal
            DOMElements.cardGeneratorModal.classList.add('hidden');
            } catch (err: any) {
                console.error("Generator Error:", err);
                showAlert("Erro ao gerar cartelas: " + (err.message || err.toString()));
                const printBtn = document.getElementById('generate-and-print-cards-btn') as HTMLButtonElement | null;
                if (printBtn) {
                    printBtn.innerHTML = "Gerar e Imprimir";
                    printBtn.disabled = false;
                }
            }
        }

        function showCardGeneratorModal() {"""

content = re.sub(bad_pattern2, good_replacement2, content)

with open('index.tsx', 'w') as f:
    f.write(content)

