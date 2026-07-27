import re

with open("attendee.html") as f:
    html = f.read()

pending_overlay = """
        <div id="attendee-pending-overlay" class="fixed inset-0 bg-brand-bg/90 backdrop-blur-sm z-[45] hidden flex-col items-center justify-center p-4 text-center">
            <div id="pending-overlay-content" class="animate-bounce-in bg-brand-card p-6 sm:p-12 rounded-3xl border-4 border-brand-border shadow-2xl flex flex-col items-center justify-center min-w-[250px] min-h-[250px]">
                <div id="pending-overlay-msg" class="text-8xl font-black text-brand-text"></div>
            </div>
        </div>
"""

html = html.replace('<div id="attendee-overlay"', pending_overlay + '        <div id="attendee-overlay"')

with open("attendee.html", "w") as f:
    f.write(html)
