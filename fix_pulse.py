import re

with open("attendee.html") as f:
    html = f.read()

html = html.replace('animate-bounce-in bg-brand-card animate-pulse', 'animate-bounce-in bg-brand-card')
html = html.replace(
    '<div id="pending-overlay-msg" class="text-8xl font-black text-brand-text"></div>',
    '<div class="animate-pulse flex flex-col items-center justify-center w-full h-full"><div id="pending-overlay-msg" class="text-8xl sm:text-9xl font-black text-brand-text drop-shadow-md"></div></div>'
)

with open("attendee.html", "w") as f:
    f.write(html)
