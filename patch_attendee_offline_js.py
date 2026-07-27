import re

with open("attendee.tsx") as f:
    tsx = f.read()

offline_js = """
// Offline / Online detection
const offlineModal = document.getElementById('attendee-offline-modal');
window.addEventListener('offline', () => {
    if (offlineModal) {
        offlineModal.classList.remove('hidden');
        offlineModal.classList.add('flex');
    }
});
window.addEventListener('online', () => {
    if (offlineModal) {
        offlineModal.classList.add('hidden');
        offlineModal.classList.remove('flex');
    }
});
"""

tsx = tsx.replace("// Modal Logic", offline_js + "\n// Modal Logic")

with open("attendee.tsx", "w") as f:
    f.write(tsx)
