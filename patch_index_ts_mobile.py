import re

with open('index.tsx', 'r') as f:
    content = f.read()

# Add DOM elements
dom_elements = """            showAttendeeQrBtn: document.getElementById('show-attendee-qr-btn'),
            simpleControllerBtn: document.getElementById('simple-controller-btn'),
            scOverlay: document.getElementById('simple-controller-overlay'),
            scCloseBtn: document.getElementById('sc-close-btn'),
            scGameName: document.getElementById('sc-game-name'),
            scLastNumber: document.getElementById('sc-last-number'),
            scDrawBtn: document.getElementById('sc-draw-btn'),
            scRecents: document.getElementById('sc-recents'),
            scDrawnCount: document.getElementById('sc-drawn-count'),
            scClaimsBtn: document.getElementById('sc-claims-btn'),
            scClaimsBadge: document.getElementById('sc-claims-badge'),
            scStatusMessage: document.getElementById('sc-status-message'),"""

content = content.replace("            showAttendeeQrBtn: document.getElementById('show-attendee-qr-btn'),", dom_elements)

# Setup event listeners
listeners = """
            if (DOMElements.simpleControllerBtn) {
                DOMElements.simpleControllerBtn.addEventListener('click', () => {
                    if (DOMElements.scOverlay) {
                        DOMElements.scOverlay.classList.remove('hidden');
                        DOMElements.scOverlay.classList.add('flex');
                        updateSimpleControllerUI();
                    }
                });
            }
            if (DOMElements.scCloseBtn) {
                DOMElements.scCloseBtn.addEventListener('click', () => {
                    DOMElements.scOverlay?.classList.add('hidden');
                    DOMElements.scOverlay?.classList.remove('flex');
                });
            }
            if (DOMElements.scDrawBtn) {
                DOMElements.scDrawBtn.addEventListener('click', () => {
                    drawNumber(true);
                });
            }
            if (DOMElements.scClaimsBtn) {
                DOMElements.scClaimsBtn.addEventListener('click', () => {
                    DOMElements.scOverlay?.classList.add('hidden');
                    DOMElements.scOverlay?.classList.remove('flex');
                    document.getElementById('bingo-claims-container')?.scrollIntoView({ behavior: 'smooth' });
                });
            }
"""
content = content.replace("            DOMElements.shareBtn.addEventListener('click', () => showProofOptionsModal());", listeners + "\n            DOMElements.shareBtn.addEventListener('click', () => showProofOptionsModal());")

with open('index.tsx', 'w') as f:
    f.write(content)
print("Mobile controller TSX events added")
