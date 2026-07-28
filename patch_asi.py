import re

with open('index.tsx', 'r') as f:
    content = f.read()

content = content.replace("        (window as any).unblockUser =", "        ;(window as any).unblockUser =")
content = content.replace("        (window as any).updateBlockedUsersUI =", "        ;(window as any).updateBlockedUsersUI =")
content = content.replace("        (window as any).blockUser =", "        ;(window as any).blockUser =")

with open('index.tsx', 'w') as f:
    f.write(content)
