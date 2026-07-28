import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

new_logic = """    const offlineOverlay = document.getElementById('attendee-offline-overlay')!;
    const onlineModal = document.getElementById('attendee-online-modal')!;

    window.addEventListener('offline', () => {
        if (offlineOverlay) {
            offlineOverlay.classList.remove('hidden');
            offlineOverlay.classList.add('flex');
        }
    });

    window.addEventListener('online', () => {
        if (offlineOverlay) {
            offlineOverlay.classList.add('hidden');
            offlineOverlay.classList.remove('flex');
        }
        if (onlineModal) {
            onlineModal.classList.remove('hidden');
            onlineModal.classList.add('flex');
            setTimeout(() => {
                onlineModal.classList.add('hidden');
                onlineModal.classList.remove('flex');
            }, 3000);
        }
    });
"""

# add it near the top of DOMContentLoaded
target = "document.addEventListener('DOMContentLoaded', async () => {\n"
content = content.replace(target, target + new_logic)

with open('attendee.tsx', 'w') as f:
    f.write(content)
print("Attendee TSX patched for offline events")
