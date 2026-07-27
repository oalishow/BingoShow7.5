import re

with open("attendee.tsx") as f:
    tsx = f.read()

replacement = """
// Offline / Online detection
const offlineModal = document.getElementById('attendee-offline-modal');
const onlineModal = document.getElementById('attendee-online-modal');
let justRestoredConnection = false;

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
    justRestoredConnection = true;
    if (onlineModal) {
        onlineModal.classList.remove('hidden');
        onlineModal.classList.add('flex');
        setTimeout(() => {
            onlineModal.classList.add('hidden');
            onlineModal.classList.remove('flex');
            justRestoredConnection = false;
        }, 3000);
    } else {
        setTimeout(() => { justRestoredConnection = false; }, 3000);
    }
});"""

tsx = tsx.replace(
"""// Offline / Online detection
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
});""", replacement)

snapshot_mod = """
                    if (isInitialLoad || justRestoredConnection) {
                        lastRoundTs = state.latestRoundTimestamp || 0;
                        lastBingoTs = state.latestBingoTimestamp || 0;
                        (window as any).lastDrawnPrizeCount = (state.drawnPrizeNumbers || []).length;
                        isInitialLoad = false;
                    }
"""

tsx = tsx.replace(
"""                    if (isInitialLoad) {
                        lastRoundTs = state.latestRoundTimestamp || 0;
                        lastBingoTs = state.latestBingoTimestamp || 0;
                        (window as any).lastDrawnPrizeCount = (state.drawnPrizeNumbers || []).length;
                        isInitialLoad = false;
                    }""", snapshot_mod)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
