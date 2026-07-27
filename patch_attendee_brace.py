import re

with open("attendee.tsx") as f:
    content = f.read()

content = content.replace("                    });\n\n                } catch (e) {", "                } catch (e) {")

with open("attendee.tsx", "w") as f:
    f.write(content)
print("Done")
