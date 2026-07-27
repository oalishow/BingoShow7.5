import re

with open("index.tsx") as f:
    tsx = f.read()

# Remove the event listener
tsx = re.sub(r"if \(document\.getElementById\('show-card-scanner-btn'\)\) \{\s*document\.getElementById\('show-card-scanner-btn'\)!\.addEventListener\('click', showCardScannerModal\);\s*\}", "", tsx)

# Remove the showCardScannerModal function
tsx = re.sub(r"function showCardScannerModal\(\) \{.*?(?=function |$)", "", tsx, flags=re.DOTALL)

with open("index.tsx", "w") as f:
    f.write(tsx)
