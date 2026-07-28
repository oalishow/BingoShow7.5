import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """        async function showIntervalQrModal() {
            let modalEl = document.getElementById('interval-qr-modal');
            if (!modalEl) {
                modalEl = document.createElement('div');
                modalEl.id = 'interval-qr-modal';
                modalEl.className = 'fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center p-4 z-[120] hidden';
                document.body.appendChild(modalEl);
            }"""

new_code = """        async function showIntervalQrModal() {
            let modalEl = document.getElementById('interval-qr-modal');
            if (!modalEl) {
                modalEl = document.createElement('div');
                modalEl.id = 'interval-qr-modal';
                modalEl.className = 'fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center p-4 z-[120] hidden';
            }
            
            const targetContainer = document.fullscreenElement || document.body;
            if (modalEl.parentElement !== targetContainer) {
                targetContainer.appendChild(modalEl);
            }"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch interval QR successful!")
else:
    print("Old code not found for interval QR!")
