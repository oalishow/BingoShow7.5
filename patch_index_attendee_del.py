import re

with open("index.tsx") as f:
    content = f.read()

start_marker = "        async function renderAttendeeMode(targetEventId: string) {"
end_marker = "        // --- Inicialização ---"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]
    with open("index.tsx", "w") as f:
        f.write(content)
    print("Deleted renderAttendeeMode successfully.")
else:
    print("Could not find markers to delete function.")
