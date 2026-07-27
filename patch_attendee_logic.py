import re

with open("attendee.tsx") as f:
    tsx = f.read()

# Update Theme Logic
theme_logic_old = """    // Theme logic
    const themeBtn = document.getElementById('theme-toggle-attendee-btn');
    const loadTheme = () => {
        const isDark = localStorage.getItem('attendee-theme') !== 'light';
        if (isDark) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    };
    loadTheme();
    
    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            const isDark = document.documentElement.classList.contains('dark');
            if (isDark) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('attendee-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('attendee-theme', 'dark');
            }
        });
    }"""

theme_logic_new = """    // Theme logic
    const themeBtn = document.getElementById('theme-toggle-attendee-btn');
    const loadTheme = () => {
        const storedTheme = localStorage.getItem('attendee-theme');
        let isDark = true;
        if (storedTheme) {
            isDark = storedTheme === 'dark';
        } else {
            isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        }
        
        if (isDark) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    };
    loadTheme();
    
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('attendee-theme')) {
            if (e.matches) document.documentElement.classList.add('dark');
            else document.documentElement.classList.remove('dark');
        }
    });

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            const isDark = document.documentElement.classList.contains('dark');
            if (isDark) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('attendee-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('attendee-theme', 'dark');
            }
        });
    }"""

tsx = tsx.replace(theme_logic_old, theme_logic_new)

# Update donation modal logic
donate_logic_old = """    const donateBtn = document.getElementById('donate-btn-attendee');
    const pixModal = document.getElementById('pix-donation-modal-attendee');
    const closeBtn = document.getElementById('close-donation-btn-attendee');

    if (donateBtn && pixModal && closeBtn) {
        donateBtn.addEventListener('click', () => {
            pixModal.classList.remove('hidden');
            pixModal.classList.add('flex');
        });
        
        closeBtn.addEventListener('click', () => {
            pixModal.classList.add('hidden');
            pixModal.classList.remove('flex');
        });
    }"""

donate_logic_new = """    const donateBtn = document.getElementById('donate-btn-attendee');
    const pixModal = document.getElementById('pix-donation-modal-attendee');
    const closeBtn = document.getElementById('close-donation-btn-attendee');
    const copyPixBtn = document.getElementById('copy-pix-btn-attendee');
    
    if (donateBtn && pixModal && closeBtn) {
        donateBtn.addEventListener('click', () => {
            pixModal.classList.remove('hidden');
            pixModal.classList.add('flex');
        });
        
        closeBtn.addEventListener('click', () => {
            pixModal.classList.add('hidden');
            pixModal.classList.remove('flex');
        });
    }
    
    if (copyPixBtn) {
        copyPixBtn.addEventListener('click', () => {
            const pixKey = document.getElementById('pix-key-display-attendee')?.textContent;
            if (pixKey) {
                navigator.clipboard.writeText(pixKey);
                copyPixBtn.textContent = '✅ Copiado!';
                setTimeout(() => {
                    copyPixBtn.textContent = '📋 Copiar Chave PIX';
                }, 2000);
            }
        });
    }"""

tsx = tsx.replace(donate_logic_old, donate_logic_new)

# In onSnapshot, update donation labels and pix key
snapshot_update = """
                    const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };
                    
                    // Update donation modal contents
                    if (labels.supportButton) {
                        const btnText = document.getElementById('donate-btn-text');
                        if (btnText) btnText.textContent = labels.supportButton;
                    }
                    if (labels.donationModalTitle) {
                        const mTitle = document.getElementById('donation-modal-title');
                        if (mTitle) mTitle.textContent = labels.donationModalTitle;
                    }
                    if (labels.donationModalDescription) {
                        const mDesc = document.getElementById('donation-modal-desc');
                        if (mDesc) mDesc.textContent = labels.donationModalDescription;
                    }
                    if (labels.donationModalPaypalLabel) {
                        const pLabel = document.getElementById('donation-modal-paypal-label');
                        if (pLabel) pLabel.textContent = labels.donationModalPaypalLabel;
                    }
                    if (labels.donationModalPixLabel) {
                        const pixLabel = document.getElementById('donation-modal-pix-label');
                        if (pixLabel) pixLabel.textContent = labels.donationModalPixLabel;
                    }
                    
                    const pixDisplay = document.getElementById('pix-key-display-attendee');
                    if (pixDisplay && config.pixKey) {
                        pixDisplay.textContent = config.pixKey;
                    }
                    if (labels.donationModalCopyButton) {
                        const copyBtn = document.getElementById('copy-pix-btn-attendee');
                        if (copyBtn && !copyBtn.textContent?.includes('Copiado')) copyBtn.textContent = labels.donationModalCopyButton;
                    }
"""

tsx = tsx.replace("const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };", snapshot_update)


with open("attendee.tsx", "w") as f:
    f.write(tsx)
