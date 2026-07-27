import re

with open("attendee.html") as f:
    html = f.read()

bingo_overlay = """
        <div id="attendee-bingo-overlay" class="fixed inset-0 bg-slate-900/90 backdrop-blur-md z-[50] hidden flex-col items-center justify-center p-4 text-center">
            <div id="bingo-overlay-content" class="animate-bounce-in bg-white dark:bg-slate-800 p-8 sm:p-12 rounded-3xl border-4 border-yellow-400 shadow-[0_0_50px_rgba(250,204,21,0.5)] flex flex-col items-center">
                <div class="text-6xl sm:text-8xl mb-6 animate-pulse">🎉</div>
                <h2 id="bingo-overlay-title" class="text-5xl sm:text-7xl font-black uppercase tracking-widest text-yellow-400 mb-4 drop-shadow-md">BINGO!</h2>
                <div id="bingo-overlay-msg" class="text-xl sm:text-3xl text-slate-800 dark:text-white"></div>
            </div>
        </div>
"""

html = html.replace('<div id="attendee-overlay"', bingo_overlay + '\n        <div id="attendee-overlay"')

with open("attendee.html", "w") as f:
    f.write(html)
