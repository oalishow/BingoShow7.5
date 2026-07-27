import re

with open("index.tsx") as f:
    content = f.read()

# Replace the if block
old_block = """            if (viewMode === 'attendee' && eventParam) {
                renderAttendeeMode(eventParam);
                return;
            }"""

new_block = """            if (viewMode === 'attendee' && eventParam) {
                window.location.href = `${window.location.origin}${basePath}attendee.html?event=${encodeURIComponent(eventParam)}`;
                return;
            }"""

if old_block in content:
    content = content.replace(old_block, new_block)
else:
    print("Not found old_block")

# Now delete the renderAttendeeMode function
start_marker = "        async function renderAttendeeMode(targetEventId: string) {"
end_marker = "        function exportToCSV(filename: string, rows: any[]) {"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]
    with open("index.tsx", "w") as f:
        f.write(content)
    print("Deleted renderAttendeeMode and redirected.")
else:
    print("Could not find markers to delete function.")

