import re

with open("attendee.tsx") as f:
    tsx = f.read()

# Replace offline logic
old_offline_logic = """// Offline / Online detection
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
});"""

new_offline_logic = """// Offline / Online detection
const offlineModal = document.getElementById('attendee-offline-modal');
const onlineModal = document.getElementById('attendee-online-modal');
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
    if (onlineModal) {
        onlineModal.classList.remove('hidden');
        onlineModal.classList.add('flex');
        setTimeout(() => {
            onlineModal.classList.add('hidden');
            onlineModal.classList.remove('flex');
        }, 3000);
    }
});"""

tsx = tsx.replace(old_offline_logic, new_offline_logic)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
