function getLetterForNumber(number: number): string {
    if (number >= 1 && number <= 15) return 'B';
    if (number >= 16 && number <= 30) return 'I';
    if (number >= 31 && number <= 45) return 'N';
    if (number >= 46 && number <= 60) return 'G';
    if (number >= 61 && number <= 75) return 'O';
    return '';
}

import { initializeApp } from 'firebase/app';
import { getAuth, signInAnonymously } from 'firebase/auth';
import { getFirestore, doc, onSnapshot, clearIndexedDbPersistence } from 'firebase/firestore';
import firebaseConfig from './firebase-applet-config.json';
import './index.css';

const firebaseApp = initializeApp(firebaseConfig);
const auth = getAuth(firebaseApp);
const db = getFirestore(firebaseApp, firebaseConfig.firestoreDatabaseId);

clearIndexedDbPersistence(db).catch(() => {});

document.addEventListener('DOMContentLoaded', async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const targetEventId = urlParams.get('event');
    
    const statusBanner = document.getElementById('attendee-status-banner')!;
    const contentContainer = document.getElementById('attendee-content')!;
    
    const appNameEl = document.getElementById('attendee-app-name')!;
    const gameNameEl = document.getElementById('attendee-game-name')!;
    const prizesEl = document.getElementById('attendee-prizes')!;
    const logoEl = document.getElementById('attendee-logo') as HTMLImageElement;
    
    const lastNumberEl = document.getElementById('attendee-last-number')!;
    const lastNumberBallEl = document.getElementById('attendee-last-number-ball')!;
    const lastCardEl = document.getElementById('attendee-last-card')!;
    const lastTitleEl = document.getElementById('attendee-last-title')!;
    const recentCardEl = document.getElementById('attendee-recent-card')!;
    const recentTitleEl = document.getElementById('attendee-recent-title')!;
    
    const recentNumbersEl = document.getElementById('attendee-recent-numbers')!;
    const boardRowsContainer = document.getElementById('attendee-board-rows')!;
    const overlayEl = document.getElementById('attendee-overlay')!;
    const bingoOverlayEl = document.getElementById('attendee-bingo-overlay')!;
    const bingoOverlayTitleEl = document.getElementById('bingo-overlay-title')!;
    const bingoOverlayMsgEl = document.getElementById('bingo-overlay-msg')!;
    const overlayIconEl = document.getElementById('overlay-icon')!;
    const overlayTitleEl = document.getElementById('overlay-title')!;
    const overlayMsgEl = document.getElementById('overlay-msg')!;

    const attendeeAuctionCard = document.getElementById('attendee-auction-card')!;
    const attendeeAuctionItem = document.getElementById('attendee-auction-item')!;
    const attendeeAuctionBid = document.getElementById('attendee-auction-bid')!;


    if (!targetEventId) {
        statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-red-900 text-red-200 rounded-xl shadow border border-red-700";
        statusBanner.innerHTML = `⚠️ URL inválida. ID do evento ausente.`;
        return;
    }

    try {
        await signInAnonymously(auth);
    } catch (e: any) {
        statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-red-900 text-red-200 rounded-xl shadow border border-red-700";
        statusBanner.innerHTML = `⚠️ Erro de conexão com o painel: ${e.message}`;
        return;
    }

    const currentLetters = ['B', 'I', 'N', 'G', 'O'];
    
    const BINGO_CONFIG: Record<string, { min: number; max: number }> = {
        'B': { min: 1, max: 15 },
        'I': { min: 16, max: 30 },
        'N': { min: 31, max: 45 },
        'G': { min: 46, max: 60 },
        'O': { min: 61, max: 75 },
        'A': { min: 1, max: 15 },
        'J': { min: 16, max: 30 },
        'U': { min: 31, max: 45 },
        'D': { min: 46, max: 60 },
        'E': { min: 61, max: 75 },
    };

    function isLightColor(color: string) {
        if (!color) return false;
        let hex = color.replace('#', '');
        if (hex.length === 3) hex = hex.split('').map(c => c + c).join('');
        const r = parseInt(hex.substring(0, 2), 16);
        const g = parseInt(hex.substring(2, 2), 16);
        const b = parseInt(hex.substring(4, 2), 16);
        const brightness = ((r * 299) + (g * 587) + (b * 114)) / 1000;
        return brightness > 155;
    }

    let currentConfigLetters = currentLetters;
    let renderedLetters: string[] = [];
    let previousDrawnCount = 0;
    let lastBingoTs = 0;
    let lastRoundTs = 0;
    let isInitialLoad = true;
    let isVerifyingState = false;

    function renderBoardRows(letters: string[], activeColor?: string) {
        if (renderedLetters.join('') === letters.join('')) return;
        renderedLetters = letters;
        boardRowsContainer.innerHTML = '';

        letters.forEach((letter, index) => {
            const rowWrapper = document.createElement('div');
            rowWrapper.className = 'flex flex-row items-stretch border border-brand-border rounded-lg min-h-[48px] sm:min-h-[56px] relative z-10 overflow-hidden';

            const letterCol = document.createElement('div');
            letterCol.className = 'flex items-center justify-center w-12 sm:w-16 border-r border-brand-border bg-brand-card';
            const letterText = document.createElement('span');
            letterText.className = 'text-3xl sm:text-4xl font-black transition-colors duration-300';
            letterText.style.color = activeColor || '#38bdf8';
            letterText.textContent = letter;
            letterCol.appendChild(letterText);
            
            letterText.id = `attendee-letter-${index}`;

            const numbersCol = document.createElement('div');
            numbersCol.className = 'flex-1 flex flex-wrap gap-1.5 sm:gap-2 items-center p-1.5 sm:p-2 bg-brand-bg transition-colors duration-300';
            numbersCol.id = `attendee-row-${index}`;

            rowWrapper.appendChild(letterCol);
            rowWrapper.appendChild(numbersCol);
            boardRowsContainer.appendChild(rowWrapper);
        });
    }

    renderBoardRows(currentLetters);

    let lastNumbersStr = '';
    let lastAuctionStr = '';
    let lastRoundStatusStr = '';
    let lastLabelsStr = '';
    let lastWinnersStr = '';

    onSnapshot(doc(db, "events", targetEventId), (docSnap) => {
        if (docSnap.exists()) {
            const eventData = docSnap.data();
            
            if (!eventData.activeGameNumber) {
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
            contentContainer.classList.add('flex');
            
            if (eventData.fullStateJSON) {
                try {
                    const state = JSON.parse(eventData.fullStateJSON);
                    const game = state.gamesData[eventData.activeGameNumber];
                    const config = state.appConfig;

                    const labelsStr = JSON.stringify(state.appLabels || {});
                    if (lastLabelsStr !== labelsStr) {
                        lastLabelsStr = labelsStr;
                        const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };
                        if (labels.supportButton) {
                            const btnText = document.getElementById('donate-btn-text');
                            if (btnText) btnText.textContent = labels.supportButton;
                        }
                        if (labels.donationModalTitle) {
                            const mTitle = document.getElementById('donation-modal-title');
                            if (mTitle) mTitle.textContent = labels.donationModalTitle;
                        }
                        if (labels.donationModalDescription) {
                            const mDesc = document.getElementById('donation-modal-desc');
                            if (mDesc) mDesc.textContent = labels.donationModalDescription;
                        }
                        if (labels.donationModalPaypalLabel) {
                            const pLabel = document.getElementById('donation-modal-paypal-label');
                            if (pLabel) pLabel.textContent = labels.donationModalPaypalLabel;
                        }
                        if (labels.donationModalPixLabel) {
                            const pixLabel = document.getElementById('donation-modal-pix-label');
                            if (pixLabel) pixLabel.textContent = labels.donationModalPixLabel;
                        }
                        const pixDisplay = document.getElementById('pix-key-display-attendee');
                        if (pixDisplay && config.pixKey) {
                            pixDisplay.textContent = config.pixKey;
                        }
                        if (labels.donationModalCopyButton) {
                            const copyBtn = document.getElementById('copy-pix-btn-attendee');
                            if (copyBtn && !copyBtn.textContent?.includes('Copiado')) copyBtn.textContent = labels.donationModalCopyButton;
                        }
                    }

                    const winnersStr = JSON.stringify(game ? game.winners : []);
                    if (lastWinnersStr !== winnersStr) {
                        lastWinnersStr = winnersStr;
                        updateWinnersList(state.gamesData);
                    }





                    // Handle Round / Bingo timestamps
                    const roundTsStr = state.latestRoundTimestamp + '-' + state.latestBingoTimestamp;
                    if (lastRoundStatusStr !== roundTsStr) {
                        lastRoundStatusStr = roundTsStr;
                        
                        if (isInitialLoad || justRestoredConnection) {
                            lastRoundTs = state.latestRoundTimestamp || 0;
                            lastBingoTs = state.latestBingoTimestamp || 0;
                            (window as any).lastDrawnPrizeCount = (state.drawnPrizeNumbers || []).length;
                            isInitialLoad = false;
                        }

                        const isNewBingo = state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs;
                        if (state.latestRoundTimestamp && state.latestRoundTimestamp !== lastRoundTs) {
                            const showNovaRodada = () => {
                                if (config.customLogo) {
                                    overlayIconEl.innerHTML = `<img src="${config.customLogo}" alt="Logo" class="h-24 w-auto object-contain drop-shadow-md" />`;
                                } else {
                                    overlayIconEl.textContent = "🎯";
                                }
                                overlayTitleEl.textContent = "Nova Rodada";
                                overlayMsgEl.textContent = game ? (game.name || `Rodada ${eventData.activeGameNumber}`) : `Rodada ${eventData.activeGameNumber}`;
                                overlayEl.classList.remove("hidden");
                                overlayEl.classList.add("flex");
                                setTimeout(() => {
                                    overlayEl.classList.add("hidden");
                                    overlayEl.classList.remove("flex");
                                }, 4000);
                            };
                               
                            if (isNewBingo) {
                                // Delay Nova Rodada until BINGO modal finishes
                                setTimeout(showNovaRodada, 8000);
                            } else {
                                showNovaRodada();
                            }
                        }
                        lastRoundTs = state.latestRoundTimestamp || 0;

                        if (state.latestBingoTimestamp && state.latestBingoTimestamp !== lastBingoTs) {
                            if ((window as any).confetti) {
                                const duration = 5 * 1000;
                                const animationEnd = Date.now() + duration;
                                const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 60 };
                                const interval: any = setInterval(function() {
                                    const timeLeft = animationEnd - Date.now();
                                    if (timeLeft <= 0) return clearInterval(interval);
                                    const particleCount = 50 * (timeLeft / duration);
                                    (window as any).confetti(Object.assign({}, defaults, { particleCount, origin: { x: Math.random(), y: Math.random() - 0.2 } }));
                                }, 250);
                            }
                               
                            let lastWinner = null;
                            if (state.gamesData) {
                                const allWinners = Object.values(state.gamesData).flatMap((g: any) => g.winners || []);
                                if (allWinners.length > 0) {
                                    allWinners.sort((a, b) => a.id - b.id);
                                    lastWinner = allWinners[allWinners.length - 1];
                                }
                            }

                            if (lastWinner) {
                                bingoOverlayMsgEl.innerHTML = `<span class="text-3xl font-black text-slate-800 dark:text-white">${lastWinner.name}</span><br/><span class="text-2xl text-yellow-500 dark:text-yellow-400 font-bold mt-3 block">${lastWinner.prize}</span>`;
                                bingoOverlayEl.classList.remove("hidden");
                                bingoOverlayEl.classList.add("flex");
                                setTimeout(() => {
                                    bingoOverlayEl.classList.add("hidden");
                                    bingoOverlayEl.classList.remove("flex");
                                }, 8000);
                            }
                        }
                        lastBingoTs = state.latestBingoTimestamp || 0;
                    }

                    // Handle Pending Number
                    let pendingStr = JSON.stringify({ pending: state.pendingNumber, color: game ? game.color : '' });
                    if ((window as any).lastPendingStr !== pendingStr) {
                        (window as any).lastPendingStr = pendingStr;
                        const pendingOverlay = document.getElementById('attendee-pending-overlay')!;
                        const pendingMsg = document.getElementById('pending-overlay-msg')!;
                        if (state.pendingNumber) {
                            const letter = getLetterForNumber(state.pendingNumber);
                            pendingMsg.innerHTML = `<span class="text-4xl block mb-2">${letter}</span><span>${state.pendingNumber}</span>`;
                            if (game && game.color) {
                                pendingMsg.style.color = game.color;
                            } else {
                                pendingMsg.style.color = '';
                            }
                            pendingOverlay.classList.remove('hidden');
                            pendingOverlay.classList.add('flex');
                        } else {
                            pendingOverlay.classList.add('hidden');
                            pendingOverlay.classList.remove('flex');
                        }
                    }

                    // Drawn Cartelas
                    const drawnPrizes = state.drawnPrizeNumbers || [];
                    if (drawnPrizes.length > ((window as any).lastDrawnPrizeCount || 0)) {
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                    }

                    let verifyStr = JSON.stringify(state.isVerifying || false);
                    if ((window as any).lastVerifyStr !== verifyStr) {
                        (window as any).lastVerifyStr = verifyStr;
                        isVerifyingState = state.isVerifying || false;
                        if (isVerifyingState) {
                            overlayIconEl.textContent = "🔍";
                            overlayTitleEl.textContent = "Aguardando conferência...";
                            overlayMsgEl.textContent = "Verificando as cartelas chamadas";
                            overlayEl.classList.remove("hidden");
                            overlayEl.classList.add("flex");
                        } else if (!isVerifyingState && overlayIconEl.textContent === "🔍") {
                            overlayEl.classList.add("hidden");
                            overlayEl.classList.remove("flex");
                        }
                    }
                       
                    if (eventData.appName && appNameEl.textContent !== eventData.appName) {
                        appNameEl.textContent = eventData.appName;
                        appNameEl.classList.remove('hidden');
                    }
                       
                    // Auction
                    const auctionStr = JSON.stringify({
                        bid: config.auctionBid,
                        item: config.auctionItemName,
                        winner: config.auctionWinnerName
                    });
                    if (lastAuctionStr !== auctionStr) {
                        lastAuctionStr = auctionStr;
                        const currentBid = parseInt(config.auctionBid || '0', 10);
                        if (currentBid > 0) {
                            attendeeAuctionCard.classList.remove('hidden');
                            attendeeAuctionCard.classList.add('flex');
                            attendeeAuctionItem.textContent = config.auctionItemName || 'Item em Leilão';
                            const newBidText = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(currentBid);
                            if (attendeeAuctionBid.textContent !== newBidText) {
                                attendeeAuctionBid.textContent = newBidText;
                                attendeeAuctionBid.classList.add('text-green-400', 'scale-125');
                                setTimeout(() => {
                                    attendeeAuctionBid.classList.remove('text-green-400', 'scale-125');
                                }, 300);
                            }
                        } else {
                            attendeeAuctionCard.classList.add('hidden');
                            attendeeAuctionCard.classList.remove('flex');
                        }
                    }

                    let logoStr = config.customLogo || '';
                    if ((window as any).lastLogoStr !== logoStr) {
                        (window as any).lastLogoStr = logoStr;
                        if (config.customLogo) {
                            logoEl.src = config.customLogo;
                            logoEl.classList.remove('hidden');
                        } else {
                            logoEl.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj4KICAgIDxkZWZzPgogICAgICAgIDwhLS0gQmFja2dyb3VuZCBHcmFkaWVudCAtLT4KICAgICAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnR3JhZCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMxZTFiNGIiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSI1MCUiIHN0b3AtY29sb3I9IiMzMTJlODEiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNDMzOGNhIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgICAgICAKICAgICAgICA8IS0tIEdvbGRlbiBUZXh0IEdyYWRpZW50IC0tPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iZ29sZEdyYWQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMCUiIHkyPSIxMDAlIj4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2ZlZjA4YSIvPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjQwJSIgc3RvcC1jb2xvcj0iI2ZiYmYyNCIvPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjYwJSIgc3RvcC1jb2xvcj0iI2Q5NzcwNiIvPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNiNDUzMDkiLz4KICAgICAgICA8L2xpbmVhckdyYWRpZW50PgoKICAgICAgICA8bGluZWFyR3JhZGllbnQgaWQ9InJlZEdyYWQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZWY0NDQ0Ii8+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzk5MWIxYiIvPgogICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CgogICAgICAgIDwhLS0gRHJvcCBTaGFkb3dzIC0tPgogICAgICAgIDxmaWx0ZXIgaWQ9ImRyb3BTaGFkb3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICAgICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iMTIiIHN0ZERldmlhdGlvbj0iMTAiIGZsb29kLW9wYWNpdHk9IjAuOCIgZmxvb2QtY29sb3I9IiMwMDAiLz4KICAgICAgICA8L2ZpbHRlcj4KICAgICAgICA8ZmlsdGVyIGlkPSJnbG93IiB4PSItNTAlIiB5PSItNTAlIiB3aWR0aD0iMjAwJSIgaGVpZ2h0PSIyMDAlIj4KICAgICAgICAgICAgPGZlR2F1c3NpYW5CbHVyIHN0ZERldmlhdGlvbj0iOCIgcmVzdWx0PSJibHVyIi8+CiAgICAgICAgICAgIDxmZU1lcmdlPgogICAgICAgICAgICAgICAgPGZlTWVyZ2VOb2RlIGluPSJibHVyIi8+CiAgICAgICAgICAgICAgICA8ZmVNZXJnZU5vZGUgaW49IlNvdXJjZUdyYXBoaWMiLz4KICAgICAgICAgICAgPC9mZU1lcmdlPgogICAgICAgIDwvZmlsdGVyPgogICAgICAgIDxmaWx0ZXIgaWQ9InRleHRHbG93IiB4PSItNTAlIiB5PSItNTAlIiB3aWR0aD0iMjAwJSIgaGVpZ2h0PSIyMDAlIj4KICAgICAgICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjgiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2Qtb3BhY2l0eT0iMC45IiBmbG9vZC1jb2xvcj0iIzAwMCIvPgogICAgICAgIDwvZmlsdGVyPgogICAgPC9kZWZzPgoKICAgIDwhLS0gQmFja2dyb3VuZCBCYXNlIC0tPgogICAgPHJlY3Qgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHJ4PSIxMDAiIGZpbGw9InVybCgjYmdHcmFkKSIgZmlsdGVyPSJ1cmwoI2Ryb3BTaGFkb3cpIi8+CiAgICAKICAgIDwhLS0gRGVjb3JhdGl2ZSBPdXRsaW5lIC0tPgogICAgPHJlY3Qgd2lkdGg9IjQ3MiIgaGVpZ2h0PSI0NzIiIHg9IjIwIiB5PSIyMCIgcng9IjgwIiBmaWxsPSJub25lIiBzdHJva2U9InVybCgjZ29sZEdyYWQpIiBzdHJva2Utd2lkdGg9IjgiIHN0cm9rZS1kYXNoYXJyYXk9IjIwIDEwIiBvcGFjaXR5PSIwLjYiLz4KCiAgICA8IS0tIExpZ2h0IFJheXMgLyBTdGFyYnVyc3QgLS0+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNTYsIDIyMCkiPgogICAgICAgIDxwYXRoIGQ9Ik0wIC0xNTAgTDEwIDAgTDAgMTUwIEwtMTAgMCBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjEiIHRyYW5zZm9ybT0icm90YXRlKDApIi8+CiAgICAgICAgPHBhdGggZD0iTTAgLTE1MCBMMTAgMCBMMCAxNTAgTC0xMCAwIFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMSIgdHJhbnNmb3JtPSJyb3RhdGUoNDUpIi8+CiAgICAgICAgPHBhdGggZD0iTTAgLTE1MCBMMTAgMCBMMCAxNTAgTC0xMCAwIFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMSIgdHJhbnNmb3JtPSJyb3RhdGUoOTApIi8+CiAgICAgICAgPHBhdGggZD0iTTAgLTE1MCBMMTAgMCBMMCAxNTAgTC0xMCAwIFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMSIgdHJhbnNmb3JtPSJyb3RhdGUoMTM1KSIvPgogICAgPC9nPgoKICAgIDwhLS0gQ2VudGVyIEJpbmdvIEJhbGwgLS0+CiAgICA8Y2lyY2xlIGN4PSIyNTYiIGN5PSIyMjAiIHI9IjEzMCIgZmlsbD0idXJsKCNyZWRHcmFkKSIgZmlsdGVyPSJ1cmwoI2Ryb3BTaGFkb3cpIi8+CiAgICAKICAgIDwhLS0gQmFsbCBJbm5lciBoaWdobGlnaHQgLS0+CiAgICA8Y2lyY2xlIGN4PSIyNTYiIGN5PSIyMjAiIHI9IjEzMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjQiIG9wYWNpdHk9IjAuMyIvPgogICAgCiAgICA8IS0tIFdoaXRlIENpcmNsZSBjZW50ZXIgLS0+CiAgICA8Y2lyY2xlIGN4PSIyNTYiIGN5PSIyMjAiIHI9IjgwIiBmaWxsPSIjZmZmZmZmIiBmaWx0ZXI9InVybCgjZHJvcFNoYWRvdykiLz4KICAgIAogICAgPCEtLSBTdGFyIERldGFpbHMgb24gdGhlIGJhbGwgLS0+CiAgICA8cGF0aCBkPSJNIDE3MCAxNTAgTCAxODAgMTcwIEwgMjAwIDE3MCBMIDE4MCAxODUgTCAxODUgMjA1IEwgMTcwIDE5MCBMIDE1NSAyMDUgTCAxNjAgMTg1IEwgMTQwIDE3MCBMIDE2MCAxNzAgWiIgZmlsbD0idXJsKCNnb2xkR3JhZCkiIC8+CiAgICA8cGF0aCBkPSJNIDM0MCAxNTAgTCAzNTAgMTcwIEwgMzcwIDE3MCBMIDM1MCAxODUgTCAzNTUgMjA1IEwgMzQwIDE5MCBMIDMyNSAyMDUgTCAzMzAgMTg1IEwgMzEwIDE3MCBMIDMzMCAxNzAgWiIgZmlsbD0idXJsKCNnb2xkR3JhZCkiIC8+CgogICAgPCEtLSltIGJpZyBOdW1iZXIgb3IgQiAtLT4KICAgIDx0ZXh0IHg9IjI1NiIgeT0iMjcwIiBmb250LWZhbWlseT0iJ0ltcGFjdCcsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTQwIiBmb250LXdlaWdodD0iOTAwIiBmaWxsPSIjYjkxYzFjIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXN0eWxlPSJpdGFsaWMiPkI8L3RleHQ+CgogICAgPCEtLSBCSU5HTyBUZXh0IC0tPgogICAgPHRleHQgeD0iMjU2IiB5PSI0NDAiIGZvbnQtZmFtaWx5PSInQXJpYWwgQmxhY2snLCBJbXBhY3QsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iODUiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc3R5bGU9Iml0YWxpYyIgZmlsbD0idXJsKCNnb2xkR3JhZCkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbHRlcj0idXJsKCN0ZXh0R2xvdykiIHN0cm9rZT0iIzc4MzUwZiIgc3Ryb2tlLXdpZHRoPSI0IiBsZXR0ZXItc3BhY2luZz0iNCI+QklOR088L3RleHQ+CiAgICAKICAgIDwhLS0gU0hPVyBUZXh0IC0tPgogICAgPHRleHQgeD0iMjU2IiB5PSI0OTAiIGZvbnQtZmFtaWx5PSInQXJpYWwgQmxhY2snLCBJbXBhY3QsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNDUiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc3R5bGU9Iml0YWxpYyIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsdGVyPSJ1cmwoI3RleHRHbG93KSIgbGV0dGVyLXNwYWNpbmc9IjEyIj5TSE9XPC90ZXh0PgoKPC9zdmc+';
                            logoEl.classList.remove('hidden');
                        }
                    }
                       
                    let gameTitleStr = game ? game.name || `Rodada ${eventData.activeGameNumber}` : '';
                    if ((window as any).lastGameTitleStr !== gameTitleStr) {
                        (window as any).lastGameTitleStr = gameTitleStr;
                        gameNameEl.textContent = gameTitleStr;
                    }
                       
                    // Exibir Prêmios
                    let prizesStr = JSON.stringify({ winners: game ? game.winners : [], prizes: game ? game.prizes : {} });
                    if ((window as any).lastPrizesStr !== prizesStr) {
                        (window as any).lastPrizesStr = prizesStr;
                        const prizeParts = [];
                        const wonPrize1 = game && game.winners && game.winners.some((w: any) => w.bingoType === 'prize1');
                        const wonPrize2 = game && game.winners && game.winners.some((w: any) => w.bingoType === 'prize2');
                        const wonPrize3 = game && game.winners && game.winners.some((w: any) => w.bingoType === 'prize3');

                        const labels = state.appLabels || { prize1Label: '1º Prêmio', prize2Label: '2º Prêmio', prize3Label: '3º Prêmio' };
                        if (game && game.prizes?.prize1) prizeParts.push(`<span class="opacity-70">${labels.prize1Label}:</span> <span class="${wonPrize1 ? 'line-through opacity-50' : ''}">${game.prizes.prize1}</span>`);
                        if (game && game.prizes?.prize2) prizeParts.push(`<span class="opacity-70">${labels.prize2Label}:</span> <span class="${wonPrize2 ? 'line-through opacity-50' : ''}">${game.prizes.prize2}</span>`);
                        if (game && game.prizes?.prize3) prizeParts.push(`<span class="opacity-70">${labels.prize3Label}:</span> <span class="${wonPrize3 ? 'line-through opacity-50' : ''}">${game.prizes.prize3}</span>`);
                        
                        if (prizeParts.length > 0) {
                            prizesEl.innerHTML = prizeParts.join(' &nbsp;|&nbsp; ');
                            prizesEl.classList.remove('hidden');
                        } else {
                            prizesEl.classList.add('hidden');
                        }
                    }

                    // Called Numbers and Grid logic
                    const calledNumbers: number[] = game ? (game.calledNumbers || []) : [];
                    const numbersStr = JSON.stringify({ called: calledNumbers, letters: config.bingoTitle, color: game ? game.color : '#38bdf8' });
                    if (lastNumbersStr !== numbersStr) {
                        lastNumbersStr = numbersStr;

                        const activeColor = game ? (game.color || '#38bdf8') : '#38bdf8';
                        const activeColorLight = isLightColor(activeColor);
                           
                        lastTitleEl.style.color = activeColor;
                        recentTitleEl.style.color = activeColor;
                        lastCardEl.style.borderColor = activeColor;
                        lastNumberBallEl.style.borderColor = activeColor;
                           
                        const newLetters = config.bingoTitle === 'AJUDE' ? ['A', 'J', 'U', 'D', 'E'] : ['B', 'I', 'N', 'G', 'O'];
                        if (currentConfigLetters.join('') !== newLetters.join('')) {
                            currentConfigLetters = newLetters;
                            renderedLetters = []; // force re-render
                            renderBoardRows(currentConfigLetters, activeColor);
                        } else {
                            currentConfigLetters.forEach((_, idx) => {
                                const l = document.getElementById(`attendee-letter-${idx}`);
                                if (l) l.style.color = activeColor;
                            });
                        }
                           
                        const isNewNumber = calledNumbers.length > previousDrawnCount;
                        previousDrawnCount = calledNumbers.length;
                           
                        // Atualizar Último Sorteado
                        if (calledNumbers.length > 0) {
                            const last = calledNumbers[calledNumbers.length - 1];
                            lastNumberEl.textContent = last.toString();
                            lastNumberEl.style.color = activeColor;
                               
                            // Fazer o bola acender
                            lastNumberBallEl.style.boxShadow = `0 0 30px ${activeColor}80`;
                               
                            if (isNewNumber) {
                                lastNumberBallEl.classList.remove('animate-bounce-in');
                                void lastNumberBallEl.offsetWidth; // trigger reflow
                                lastNumberBallEl.classList.add('animate-bounce-in');
                            }
                        } else {
                            lastNumberEl.textContent = '- -';
                            lastNumberEl.style.color = 'white';
                            lastNumberBallEl.style.boxShadow = 'none';
                        }
                           
                        // Atualizar Últimos 3 Sorteados
                        recentNumbersEl.innerHTML = '';
                        if (calledNumbers.length > 0) {
                            const last3 = calledNumbers.slice(-4, -1).reverse();
                            if (last3.length > 0) {
                                last3.forEach((num, idx) => {
                                    const pill = document.createElement('div');
                                    // Se for o primeiro da lista de recentes (o que acabou de ser substituído) e houver novo sorteio, anima ele também
                                    const animateClass = (idx === 0 && isNewNumber) ? 'animate-bounce-in' : '';
                                       
                                    pill.className = `w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-brand-bg text-slate-800 dark:text-white border-2 flex items-center justify-center font-black text-lg shadow-sm ${animateClass} relative overflow-hidden`;
                                    pill.style.borderColor = activeColor;
                                       
                                    // Brilho de bola
                                    const glare = document.createElement('div');
                                    glare.className = 'absolute inset-0 rounded-full opacity-30 bg-gradient-to-br from-white/50 to-transparent mix-blend-overlay';
                                    pill.appendChild(glare);
                                       
                                    const numSpan = document.createElement('span');
                                    numSpan.className = 'z-10 relative';
                                    numSpan.textContent = num.toString();
                                    pill.appendChild(numSpan);
                                       
                                    recentNumbersEl.appendChild(pill);
                                });
                            } else {
                                recentNumbersEl.innerHTML = '<span class="text-slate-400 font-bold text-xs sm:text-sm">Nenhum número anterior</span>';
                            }
                        } else {
                            recentNumbersEl.innerHTML = '<span class="text-slate-400 font-bold text-xs sm:text-sm">Nenhum número anterior</span>';
                        }
                           
                        const lettersRange = newLetters.join('') === 'AJUDE' ? [
                            { letter: 'A', min: 1, max: 15 },
                            { letter: 'J', min: 16, max: 30 },
                            { letter: 'U', min: 31, max: 45 },
                            { letter: 'D', min: 46, max: 60 },
                            { letter: 'E', min: 61, max: 75 }
                        ] : [
                            { letter: 'B', min: 1, max: 15 },
                            { letter: 'I', min: 16, max: 30 },
                            { letter: 'N', min: 31, max: 45 },
                            { letter: 'G', min: 46, max: 60 },
                            { letter: 'O', min: 61, max: 75 }
                        ];


                        
                        document.querySelectorAll('[id^="attendee-row-"]').forEach(row => {
                            const nums = row.querySelectorAll('div');
                            nums.forEach(num => num.remove());
                        });
                        
                        calledNumbers.forEach((num: number, index: number) => {
                            const isLastNum = calledNumbers.length > 0 && num === calledNumbers[calledNumbers.length - 1];
                            const animNew = (isLastNum && isNewNumber);
                            
                            let targetIdx = 0;
                            lettersRange.forEach((rng, idx) => {
                                if (num >= rng.min && num <= rng.max) {
                                    targetIdx = idx;
                                }
                            });
                            
                            const row = document.getElementById(`attendee-row-${targetIdx}`);
                            if (row) {
                                const isLast = index === calledNumbers.length - 1;
                                const numDiv = document.createElement('div');
                                
                                const animClass = (isLast && animNew) ? 'animate-bounce-in' : '';
                                numDiv.className = `w-7 h-7 sm:w-9 sm:h-9 rounded-full flex items-center justify-center font-black text-xs sm:text-sm transition-all duration-300 relative overflow-hidden ${animClass} ${isLast ? 'scale-[1.15] shadow-lg z-10' : 'bg-brand-border text-slate-300'}`;
                                
                                if (isLast) {
                                    numDiv.style.backgroundColor = activeColor;
                                    numDiv.style.color = activeColorLight ? '#060a16' : 'white';
                                    numDiv.style.boxShadow = `0 0 12px ${activeColor}`;
                                    
                                    // Brilho de bola no last (grid)
                                    const glare = document.createElement('div');
                                    glare.className = 'absolute inset-0 rounded-full opacity-40 bg-gradient-to-br from-white/60 to-transparent mix-blend-overlay pointer-events-none';
                                    numDiv.appendChild(glare);
                                } else {
                                    numDiv.style.backgroundColor = '';
                                    numDiv.style.color = '';
                                    numDiv.style.boxShadow = '';
                                }
                                
                                const numSpan = document.createElement('span');
                                numSpan.className = 'z-10 relative';
                                numSpan.textContent = num.toString();
                                numDiv.appendChild(numSpan);
                                
                                row.appendChild(numDiv);
                            }
                        });
                    }
                } catch (e) {
                    console.error("Erro ao analisar estado do painel", e);
                }
            }
        } else {
            statusBanner.classList.remove('hidden');
            contentContainer.classList.add('hidden');
            statusBanner.className = "w-full p-4 text-center text-sm font-bold bg-red-900 text-red-200 rounded-xl shadow border border-red-700";
            statusBanner.innerHTML = `⚠️ Evento não encontrado. O organizador pode ter fechado a sala.`;
        }
    });
});



// Offline / Online detection
const offlineModal = document.getElementById('attendee-offline-modal');
const onlineModal = document.getElementById('attendee-online-modal');
let justRestoredConnection = false;

window.addEventListener('offline', () => {
    if (offlineModal) {
        offlineModal.classList.remove('hidden');
        offlineModal.classList.add('flex');
    }
});
window.addEventListener('online', () => {
    if (offlineModal) {
        offlineModal.classList.add('hidden');
        offlineModal.classList.remove('flex');
    }
    justRestoredConnection = true;
    if (onlineModal) {
        onlineModal.classList.remove('hidden');
        onlineModal.classList.add('flex');
        setTimeout(() => {
            onlineModal.classList.add('hidden');
            onlineModal.classList.remove('flex');
            justRestoredConnection = false;
        }, 3000);
    } else {
        setTimeout(() => { justRestoredConnection = false; }, 3000);
    }
});


// Winners Modal Logic
const winnersBtn = document.getElementById('show-winners-attendee-btn');
const winnersModal = document.getElementById('attendee-winners-modal');
const closeWinnersBtn = document.getElementById('close-winners-attendee-btn');
const winnersContainer = document.getElementById('attendee-winners-container');

if (winnersBtn && winnersModal && closeWinnersBtn) {
    winnersBtn.addEventListener('click', () => {
        winnersModal.classList.remove('hidden');
        winnersModal.classList.add('flex');
    });
    
    closeWinnersBtn.addEventListener('click', () => {
        winnersModal.classList.add('hidden');
        winnersModal.classList.remove('flex');
    });
}

function updateWinnersList(gamesData: any) {
    if (!winnersContainer) return;
    
    const allWinners: any[] = [];
    if (gamesData) {
        Object.values(gamesData).forEach((game: any) => {
            if (game.winners && game.winners.length > 0) {
                allWinners.push(...game.winners);
            }
        });
    }
    
    allWinners.sort((a, b) => b.id - a.id);
    
    if (allWinners.length === 0) {
        winnersContainer.innerHTML = '<p class="text-slate-500 text-center italic mt-4">Nenhum vencedor registrado ainda.</p>';
        return;
    }
    
    winnersContainer.innerHTML = '';
    allWinners.forEach(winnerData => {
        const winnerCard = document.createElement('div');
        winnerCard.className = 'bg-white dark:bg-slate-800 p-3 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm flex items-center justify-between';
        
        let prizeText = winnerData.prize;
        if (winnerData.bingoType === 'prize1' || winnerData.bingoType === 'prize2' || winnerData.bingoType === 'prize3') {
             prizeText = `${winnerData.prize} (${winnerData.bingoType === 'prize1' ? '1º' : winnerData.bingoType === 'prize2' ? '2º' : '3º'})`;
        }

        const gameName = (winnerData.gameNumber === 'Brinde' || winnerData.gameNumber === 'Leilão') 
                ? '' 
                : (gamesData[winnerData.gameNumber]?.name || `Rodada ${winnerData.gameNumber}`);
        
        winnerCard.innerHTML = `
            <div>
                 <p class="font-bold text-slate-800 dark:text-white text-lg">${winnerData.name}</p>
                 <p class="text-sm font-semibold text-amber-500 dark:text-amber-400">${prizeText}</p>
                 <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">${gameName}</p>
            </div>
            <div class="text-3xl">🏆</div>
        `;
        winnersContainer.appendChild(winnerCard);
    });
}

// Modal Logic
document.addEventListener('DOMContentLoaded', () => {

    // Theme logic
    const themeBtn = document.getElementById('theme-toggle-attendee-btn');
    const loadTheme = () => {
        const storedTheme = localStorage.getItem('attendee-theme');
        let isDark = true;
        if (storedTheme) {
            isDark = storedTheme === 'dark';
        } else {
            isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        }
        
        if (isDark) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    };
    loadTheme();
    
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('attendee-theme')) {
            if (e.matches) document.documentElement.classList.add('dark');
            else document.documentElement.classList.remove('dark');
        }
    });

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            const isDark = document.documentElement.classList.contains('dark');
            if (isDark) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('attendee-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('attendee-theme', 'dark');
            }
        });
    }

    const donateBtn = document.getElementById('donate-btn-attendee');
    const pixModal = document.getElementById('pix-donation-modal-attendee');
    const closeBtn = document.getElementById('close-donation-btn-attendee');

    if (donateBtn && pixModal && closeBtn) {
        donateBtn.addEventListener('click', () => {
            pixModal.classList.remove('hidden');
            pixModal.classList.add('flex');
        });

        closeBtn.addEventListener('click', () => {
            pixModal.classList.add('hidden');
            pixModal.classList.remove('flex');
        });
    }
});
