import re

with open("index.tsx") as f:
    tsx = f.read()

# Add pendingNumber to AppState
tsx = re.sub(
    r"activeGameNumber: string \| null;",
    "activeGameNumber: string | null;\n    pendingNumber: number | null;",
    tsx
)

tsx = re.sub(
    r"activeGameNumber: null,",
    "activeGameNumber: null,\n            pendingNumber: null,",
    tsx
)

with open("index.tsx", "w") as f:
    f.write(tsx)
