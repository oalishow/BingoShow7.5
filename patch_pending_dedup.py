import re

with open("index.tsx") as f:
    content = f.read()

content = content.replace("                pendingNumber: null as number | null,\n                pendingNumber: null as number | null,", "                pendingNumber: null as number | null,")

with open("index.tsx", "w") as f:
    f.write(content)
print("Done")
