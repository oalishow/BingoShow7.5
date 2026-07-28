import re

with open('index.html', 'r') as f:
    content = f.read()

new_buttons = """                    <div class="flex flex-col sm:flex-row gap-2 mt-2">
                        <button id="show-attendee-qr-btn" class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-full font-bold shadow-md text-sm transition-transform hover:scale-105 flex items-center gap-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                              <path fill-rule="evenodd" d="M3 4a1 1 0 011-1h3a1 1 0 011 1v3a1 1 0 01-1 1H4a1 1 0 01-1-1V4zm2 1v1h1V5H5zm0 7a1 1 0 011-1h3a1 1 0 011 1v3a1 1 0 01-1 1H4a1 1 0 01-1-1v-3zm2 1v1h1v-1H5zm6-9a1 1 0 011-1h3a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1V4zm2 1v1h1V5h-1zm-2 7a1 1 0 00-1 1v3a1 1 0 001 1h3a1 1 0 001-1v-3a1 1 0 00-1-1h-3zm1 2v1h1v-1h-1z" clip-rule="evenodd" />
                            </svg>
                            Mostrar QR Code (Público)
                        </button>
                        <button id="simple-controller-btn" class="bg-teal-600 hover:bg-teal-700 text-white px-4 py-2 rounded-full font-bold shadow-md text-sm transition-transform hover:scale-105 flex items-center justify-center gap-2">
                            📱 Painel Simples (Mobile)
                        </button>
                    </div>"""

content = re.sub(r'<button id="show-attendee-qr-btn".*?</button>', new_buttons, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)
print("Mobile controller button added")
