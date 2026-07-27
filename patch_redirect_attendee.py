import re

with open("index.tsx") as f:
    content = f.read()

old_block = """            if (viewMode === 'attendee' && eventParam) {
                renderAttendeeMode(eventParam);
                return;
            }"""

new_block = """            if (viewMode === 'attendee' && eventParam) {
                const basePath = window.location.pathname.replace(/\/index\.html$/, '/').replace(/\/?$/, '/');
                window.location.href = `${window.location.origin}${basePath}attendee.html?event=${encodeURIComponent(eventParam)}`;
                return;
            }"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open("index.tsx", "w") as f:
        f.write(content)
    print("Replaced!")
else:
    print("Not replaced!")
