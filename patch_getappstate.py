import re

with open("index.tsx") as f:
    tsx = f.read()

replacement = """                    appLabels: this.state.appLabels,
                    pendingNumber: this.state.pendingNumber,"""

tsx = tsx.replace("                    appLabels: this.state.appLabels,", replacement)

with open("index.tsx", "w") as f:
    f.write(tsx)
