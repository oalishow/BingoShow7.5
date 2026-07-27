import re

with open("attendee.html") as f:
    html = f.read()

new_modal = """        <div id="pix-donation-modal-attendee" class="fixed inset-0 bg-black bg-opacity-70 backdrop-blur-sm hidden z-[70] flex-col items-center justify-center p-4">
            <div class="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-2xl max-w-sm w-full text-center relative animate-bounce-in">
                <button id="close-donation-btn-attendee" class="absolute top-3 right-3 text-slate-400 hover:text-slate-200">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <h2 id="donation-modal-title" class="text-3xl font-black text-amber-400 mb-6">Apoio ao Projeto Seminarista</h2>
                <p id="donation-modal-desc" class="text-slate-700 dark:text-slate-300 mb-4">Sua doação ajuda a manter este projeto ativo. Agradecemos imensamente!</p>
                <div class="space-y-6 text-left">
                    <div class="text-center border-b border-gray-700 pb-6">
                        <p id="donation-modal-paypal-label" class="text-lg font-bold text-gray-900 dark:text-white mb-4">Doação via PayPal</p>
                        <div class="flex justify-center">
                            <form action="https://www.paypal.com/donate" method="post" target="_blank">
                                <input type="hidden" name="hosted_button_id" value="FLVDNY994MNQS" />
                                <input type="image" src="https://www.paypalobjects.com/pt_BR/BR/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Faça doações com o botão do PayPal" />
                            </form>
                        </div>
                    </div>
                    <div class="pt-6">
                        <p id="donation-modal-pix-label" class="text-lg font-bold text-gray-900 dark:text-white mb-2">PIX (Chave Aleatória)</p>
                        <div class="flex flex-col items-center">
                            <div id="pix-key-display-attendee" contenteditable="false" class="bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white p-3 rounded-lg text-center text-sm font-mono select-all cursor-text max-w-full overflow-hidden whitespace-nowrap overflow-ellipsis"></div>
                            <button id="copy-pix-btn-attendee" class="mt-3 w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg text-sm transition-all">📋 Copiar Chave PIX</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""

html = re.sub(r'<div id="pix-donation-modal-attendee".*?</p>\s*</div>\s*</div>', new_modal, html, flags=re.DOTALL)

with open("attendee.html", "w") as f:
    f.write(html)
