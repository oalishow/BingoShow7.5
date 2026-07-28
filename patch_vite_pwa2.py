import re

with open('vite.config.ts', 'r') as f:
    content = f.read()

content = content.replace("navigateFallbackDenylist: [/^\/attendee\.html/]", "navigateFallbackDenylist: [/attendee\.html/]")

with open('vite.config.ts', 'w') as f:
    f.write(content)
print("vite.config.ts patched 2")
