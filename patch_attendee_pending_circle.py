import re

with open("attendee.html") as f:
    html = f.read()

# Make pending overlay a circle
html = html.replace(
    '<div id="pending-overlay-content" class="animate-bounce-in bg-brand-card p-6 sm:p-12 rounded-3xl border-4 border-brand-border shadow-2xl flex flex-col items-center justify-center min-w-[250px] min-h-[250px]">',
    '<div id="pending-overlay-content" class="animate-bounce-in bg-brand-card rounded-full border-8 border-brand-border shadow-[0_0_50px_rgba(0,0,0,0.5)] flex flex-col items-center justify-center w-64 h-64 sm:w-80 sm:h-80 relative overflow-hidden ring-4 ring-brand-text/50">'
)

with open("attendee.html", "w") as f:
    f.write(html)
