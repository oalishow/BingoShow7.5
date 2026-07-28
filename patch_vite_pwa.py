import re

with open('vite.config.ts', 'r') as f:
    content = f.read()

new_workbox = """          workbox: {
            cleanupOutdatedCaches: true,
            navigateFallbackDenylist: [/^\/attendee\.html/],
            globPatterns: ['**/*.{js,css,html,ico,png,svg,json,tsx,ts}'],"""

content = content.replace("""          workbox: {
            cleanupOutdatedCaches: true,
            globPatterns: ['**/*.{js,css,html,ico,png,svg,json,tsx,ts}'],""", new_workbox)

with open('vite.config.ts', 'w') as f:
    f.write(content)
print("vite.config.ts patched")
