import re

with open("attendee.tsx") as f:
    tsx = f.read()

theme_logic = """
    // Theme logic
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
    }
"""

tsx = re.sub(r"document\.addEventListener\('DOMContentLoaded', \(\) => \{", "document.addEventListener('DOMContentLoaded', () => {\n" + theme_logic, tsx)

with open("attendee.tsx", "w") as f:
    f.write(tsx)
