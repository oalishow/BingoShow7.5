import re

with open('index.tsx', 'r') as f:
    content = f.read()

# 1. Default config
content = re.sub(r'sponsorDisplaySeconds:\s*\d+,', 'sponsorDisplaySeconds: 10,', content)

# 2. HTML defaults
content = re.sub(
    r'<span id="sponsor-display-value">8</span>',
    '<span id="sponsor-display-value">10</span>',
    content
)
content = re.sub(
    r'<input type="range" id="sponsor-display-timer" min="3" max="30" value="8"',
    '<input type="range" id="sponsor-display-timer" min="3" max="30" value="10"',
    content
)

# 3. Fallbacks
content = re.sub(
    r'\(appStore\.state\.appConfig\.sponsorDisplaySeconds \|\| 8\)',
    '(appStore.state.appConfig.sponsorDisplaySeconds || 10)',
    content
)
content = re.sub(
    r'\(appConfig\.sponsorDisplaySeconds \|\| 8\)',
    '(appConfig.sponsorDisplaySeconds || 10)',
    content
)

# 4. showSponsorDisplayModal
content = content.replace(
    "let currentCountdownValue = appConfig.modalAutocloseSeconds;",
    "let currentCountdownValue = appConfig.sponsorDisplaySeconds || 10;"
)

content = content.replace(
    "appStore.state.appConfig.modalAutocloseSeconds = speed;",
    "appStore.state.appConfig.sponsorDisplaySeconds = speed;\n                    const sponsorDisplayTimer = document.getElementById('sponsor-display-timer') as HTMLInputElement;\n                    const sponsorDisplayValue = document.getElementById('sponsor-display-value') as HTMLElement;\n                    if (sponsorDisplayTimer) sponsorDisplayTimer.value = speed.toString();\n                    if (sponsorDisplayValue) sponsorDisplayValue.textContent = speed.toString();"
)

with open('index.tsx', 'w') as f:
    f.write(content)

print("Patch applied.")
