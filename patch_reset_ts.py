import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

target = "            const eventData = docSnap.data();\n"
new_code = """            const eventData = docSnap.data();
            
            if (eventData.isReset) {
                showFatalError('O evento foi encerrado ou resetado pelo organizador. Feche esta página e escaneie o novo QR Code caso um novo evento tenha sido iniciado.');
                if (waitingScreen) waitingScreen.classList.add('hidden');
                if (contentContainer) contentContainer.classList.add('hidden');
                return;
            }\n"""

content = content.replace(target, new_code)

with open('attendee.tsx', 'w') as f:
    f.write(content)
print("Attendee reset logic patched")
