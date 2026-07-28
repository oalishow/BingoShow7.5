import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_code = """                activeGame.verifiedWinningCards.push({
                    series: cardData.series,
                    uuid: uuid,
                    numbers: cardData.numbers
                });"""

new_code = """                activeGame.verifiedWinningCards.push({
                    series: cardData.series,
                    uuid: uuid,
                    numbers: cardData.numbers,
                    drawnCount: calledNumbers.length
                });"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.tsx', 'w') as f:
        f.write(content)
    print("Patch index successful!")
else:
    print("Old code not found in index!")

with open('attendee.tsx', 'r') as f:
    content = f.read()

old_code = """                        if (lastVerifiedCard) {"""

new_code = """                        if (lastVerifiedCard && lastVerifiedCard.drawnCount >= calledNumbers.length) {"""

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('attendee.tsx', 'w') as f:
        f.write(content)
    print("Patch attendee successful!")
else:
    print("Old code not found in attendee!")
