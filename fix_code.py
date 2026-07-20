import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""CÓD: \$\{uuid\.substring\(0,8\)\}</div>"""
good_replacement = """CÓD: ${cardData.code}</div>"""
content = re.sub(bad_pattern, good_replacement, content)

bad_pattern_download = r"""            printWindow.document.close\(\);
            
            // Auto close modal"""

good_replacement_download = """            printWindow.document.close();
            
            if (downloadBackup) {
                try {
                    const htmlContent = "<!DOCTYPE html>\\n" + printWindow.document.documentElement.outerHTML;
                    const blob = new Blob([htmlContent], { type: 'text/html' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `Cartelas_Bingo_${title.replace(/[^a-z0-9]/gi, '_')}.html`;
                    a.click();
                    URL.revokeObjectURL(url);
                } catch(err) {
                    console.error("Erro ao baixar backup:", err);
                }
            }
            
            if (printBtn) {
                printBtn.innerHTML = "Gerar e Imprimir";
                printBtn.disabled = false;
            }
            
            // Auto close modal"""
            
content = re.sub(bad_pattern_download, good_replacement_download, content)

with open('index.tsx', 'w') as f:
    f.write(content)
