import re

with open("index.tsx") as f:
    tsx = f.read()

# We can find `show-card-scanner-btn` in DOMElements and remove the listener
tsx = re.sub(r'const showCardScannerBtn = document\.getElementById\(\'show-card-scanner-btn\'\);.*', '', tsx)
tsx = re.sub(r'DOMElements\.cardScannerModal\.innerHTML = getModalTemplates\(\)\.cardScanner;.*?\s+const scannerIdInput = document\.getElementById\(\'scanner-id-input\'\) as HTMLInputElement;.*?\s+const closeScannerBtn = document\.getElementById\(\'close-scanner-btn\'\);.*?\}\);', '', tsx, flags=re.DOTALL)

with open("index.tsx", "w") as f:
    f.write(tsx)
