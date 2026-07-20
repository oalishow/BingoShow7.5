import re

with open('index.tsx', 'r') as f:
    content = f.read()

bad_pattern = r"""            // small delay to allow UI to update
            await new Promise\(res => setTimeout\(res, 100\)\);

            const printWindow = window\.open\('', '_blank'\);
            if \(!printWindow\) \{
                showAlert\('Não foi possível abrir a aba de impressão\. Verifique se o seu navegador está bloqueando pop-ups\.'\);
                if \(printBtn\) \{
                    printBtn\.innerHTML = "Gerar e Imprimir";
                    printBtn\.disabled = false;
                \}
                return;
            \}
            
            printWindow\.document\.write\('<html><head><title>Preparando\.\.\.</title></head><body style="font-family: sans-serif; text-align: center; padding: 50px;"><h2>Gerando ' \+ quantity \+ ' cartelas\.\.\.</h2></body></html>'\);
            showAlert\("Preparando PDF na nova aba\. Aguarde\.\.\."\);"""

good_replacement = r"""            const printWindow = window.open('', '_blank');
            if (!printWindow) {
                showAlert('Não foi possível abrir a aba de impressão. Verifique se o seu navegador está bloqueando pop-ups.');
                if (printBtn) {
                    printBtn.innerHTML = "Gerar e Imprimir";
                    printBtn.disabled = false;
                }
                return;
            }
            
            printWindow.document.write('<html><head><title>Preparando...</title></head><body style="font-family: sans-serif; text-align: center; padding: 50px;"><h2>Gerando ' + quantity + ' cartelas...</h2></body></html>');
            showAlert("Preparando PDF na nova aba. Aguarde...");

            // small delay to allow UI to update
            await new Promise(res => setTimeout(res, 100));"""

if bad_pattern in content:
    print("Found exact block, but didn't work because of regex. Let's use simple replace.")
else:
    print("Block not found with regex.")

content = content.replace("""            // small delay to allow UI to update
            await new Promise(res => setTimeout(res, 100));

            const printWindow = window.open('', '_blank');
            if (!printWindow) {
                showAlert('Não foi possível abrir a aba de impressão. Verifique se o seu navegador está bloqueando pop-ups.');
                if (printBtn) {
                    printBtn.innerHTML = "Gerar e Imprimir";
                    printBtn.disabled = false;
                }
                return;
            }
            
            printWindow.document.write('<html><head><title>Preparando...</title></head><body style="font-family: sans-serif; text-align: center; padding: 50px;"><h2>Gerando ' + quantity + ' cartelas...</h2></body></html>');
            showAlert("Preparando PDF na nova aba. Aguarde...");""", """            const printWindow = window.open('', '_blank');
            if (!printWindow) {
                showAlert('Não foi possível abrir a aba de impressão. Verifique se o seu navegador está bloqueando pop-ups.');
                if (printBtn) {
                    printBtn.innerHTML = "Gerar e Imprimir";
                    printBtn.disabled = false;
                }
                return;
            }
            
            printWindow.document.write('<html><head><title>Preparando...</title></head><body style="font-family: sans-serif; text-align: center; padding: 50px;"><h2>Gerando ' + quantity + ' cartelas...</h2></body></html>');
            showAlert("Preparando PDF na nova aba. Aguarde...");

            // small delay to allow UI to update
            await new Promise(res => setTimeout(res, 100));""")

with open('index.tsx', 'w') as f:
    f.write(content)

