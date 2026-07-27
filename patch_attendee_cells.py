import re

with open("attendee.tsx") as f:
    content = f.read()

bad_block = """                        Object.values(cellsByNumber).forEach(cell => {
                            cell.dataset.drawn = 'false';
                        });"""

content = content.replace(bad_block, "")

with open("attendee.tsx", "w") as f:
    f.write(content)
print("attendee.tsx fixed")
