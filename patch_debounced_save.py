import re

with open("index.tsx") as f:
    content = f.read()

# Replace the push without save
content = content.replace("appStore.state.drawnPrizeNumbers.push(finalNumber);\n", "appStore.state.drawnPrizeNumbers.push(finalNumber);\n            appStore.debouncedSave(true);\n")

with open("index.tsx", "w") as f:
    f.write(content)
