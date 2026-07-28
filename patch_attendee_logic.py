import re

with open('attendee.tsx', 'r') as f:
    content = f.read()

# Add DOM elements for waiting screen at the top
dom_elements = """    const contentContainer = document.getElementById('attendee-content')!;
    
    // Waiting Screen Elements
    const waitingScreen = document.getElementById('attendee-waiting-screen')!;
    const waitingLogo = document.getElementById('waiting-logo') as HTMLImageElement;
    const waitingAppName = document.getElementById('waiting-app-name')!;
    const waitingTitle = document.getElementById('waiting-title')!;
    const waitingMessage = document.getElementById('waiting-message')!;"""

content = content.replace("    const contentContainer = document.getElementById('attendee-content')!;", dom_elements)

# Replace the block that handles !eventData.activeGameNumber
old_wait_block = """            if (!eventData.activeGameNumber) {
                statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-yellow-900/50 text-yellow-200 rounded-xl shadow-sm border border-yellow-700/50 animate-pulse";
                statusBanner.innerHTML = `⏳ Aguardando próxima rodada...`;
                contentContainer.classList.add('hidden');
                statusBanner.classList.remove('hidden');
                lastNumbersStr = '';
                lastAuctionStr = '';
                lastRoundStatusStr = '';
                return;
            }
            
            statusBanner.classList.add('hidden');
            contentContainer.classList.remove('hidden');
            contentContainer.classList.add('flex');"""

new_wait_block = """            if (!eventData.activeGameNumber) {
                // Populate waiting screen
                if (eventData.fullStateJSON) {
                    try {
                        const state = JSON.parse(eventData.fullStateJSON);
                        const config = state.appConfig;
                        waitingAppName.textContent = config.bingoTitle || 'Bingo Show';
                        if (config.customLogoBase64) {
                            waitingLogo.src = config.customLogoBase64;
                            waitingLogo.classList.remove('hidden');
                        } else {
                            waitingLogo.classList.add('hidden');
                        }
                    } catch(e) {}
                }
                
                contentContainer.classList.add('hidden');
                contentContainer.classList.remove('flex');
                waitingScreen.classList.remove('hidden');
                waitingScreen.classList.add('flex');
                statusBanner.classList.add('hidden');
                
                lastNumbersStr = '';
                lastAuctionStr = '';
                lastRoundStatusStr = '';
                return;
            }
            
            waitingScreen.classList.add('hidden');
            waitingScreen.classList.remove('flex');
            statusBanner.classList.add('hidden');
            contentContainer.classList.remove('hidden');
            contentContainer.classList.add('flex');"""

if old_wait_block in content:
    content = content.replace(old_wait_block, new_wait_block)
    print("Wait block patched")
else:
    print("Wait block not found")

with open('attendee.tsx', 'w') as f:
    f.write(content)
