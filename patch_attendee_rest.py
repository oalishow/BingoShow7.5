import re

with open("attendee.tsx") as f:
    content = f.read()

replacement = """
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
                        const wonPrize1 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize1');
                        const wonPrize2 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize2');
                        const wonPrize3 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize3');

                        if (game.prizes?.prize1) prizeParts.push(`<span class="opacity-70">${labels.prize1Label}:</span> <span class="${wonPrize1 ? 'line-through opacity-50' : ''}">${game.prizes.prize1}</span>`);
                        if (game.prizes?.prize2) prizeParts.push(`<span class="opacity-70">${labels.prize2Label}:</span> <span class="${wonPrize2 ? 'line-through opacity-50' : ''}">${game.prizes.prize2}</span>`);
                        if (game.prizes?.prize3) prizeParts.push(`<span class="opacity-70">${labels.prize3Label}:</span> <span class="${wonPrize3 ? 'line-through opacity-50' : ''}">${game.prizes.prize3}</span>`);
                        
                        gamePrizesEl.innerHTML = prizeParts.join('<span class="mx-2 opacity-30">|</span>');
                    }

                    // Called Numbers
                    const calledNumbers = game ? game.calledNumbers || [] : [];
                    const numbersStr = JSON.stringify({ called: calledNumbers, color: config.boardColor });
                    if (lastNumbersStr !== numbersStr) {
                        lastNumbersStr = numbersStr;
                        lastDrawn = calledNumbers.length > 0 ? calledNumbers[calledNumbers.length - 1] : null;
                        
                        lastNumberEl.textContent = lastDrawn ? lastDrawn.toString() : '-';
                        if (lastDrawn) {
                            lastNumberEl.classList.add('scale-110', 'text-amber-500', 'dark:text-amber-400');
                            setTimeout(() => {
                                lastNumberEl.classList.remove('scale-110', 'text-amber-500', 'dark:text-amber-400');
                            }, 500);
                        }

                        const activeColor = config.boardColor !== 'default' ? config.boardColor : '#ef4444';
                        const activeColorLight = activeColor && (activeColor === '#fef08a' || activeColor === '#fde047' || activeColor.toLowerCase() === '#ffffff');

                        Object.values(cellsByNumber).forEach(cell => {
                            cell.dataset.drawn = 'false';
                        });
                        
                        document.querySelectorAll('[id^="attendee-row-"]').forEach(row => {
                            const nums = row.querySelectorAll('div');
                            nums.forEach(num => num.remove());
                        });

                        calledNumbers.forEach((num: number, index: number) => {
                            const isNewNumber = lastDrawn === num && !lastNumbersStr.includes(`[${num}]`);
                            
                            let targetIdx = 0;
                            ['B', 'I', 'N', 'G', 'O'].forEach((letter, idx) => {
                                const min = BINGO_CONFIG[letter].min;
                                const max = BINGO_CONFIG[letter].max;
                                if (num >= min && num <= max) {
                                    targetIdx = idx;
                                }
                            });
                            const row = document.getElementById(`attendee-row-${targetIdx}`);
                            if (row) {
                                const isLast = index === calledNumbers.length - 1;
                                const numDiv = document.createElement('div');
                                
                                const animClass = (isLast && isNewNumber) ? 'animate-bounce-in' : '';
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
                    }"""

old_code = """
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


                    // Handle Pending Number
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

                    // Drawn Cartelas
                    const drawnPrizes = state.drawnPrizeNumbers || [];
                    if (drawnPrizes.length > (window as any).lastDrawnPrizeCount) {
                        (window as any).lastDrawnPrizeCount = drawnPrizes.length;
                    }

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
                       
                    if (eventData.appName) {
                        appNameEl.textContent = eventData.appName;
                        appNameEl.classList.remove('hidden');
                    }

                       
                    // Auction
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


                    if (config.customLogo) {
                        logoEl.src = config.customLogo;
                        logoEl.classList.remove('hidden');
                    } else {
                        logoEl.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj4KICAgIDxkZWZzPgogICAgICAgIDwhLS0gQmFja2dyb3VuZCBHcmFkaWVudCAtLT4KICAgICAgICA8bGluZWFyR3JhZGllbnQgaWQ9ImJnR3JhZCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMCUiIHN0b3AtY29sb3I9IiMxZTFiNGIiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSI1MCUiIHN0b3AtY29sb3I9IiMzMTJlODEiLz4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjNDMzOGNhIi8+CiAgICAgICAgPC9saW5lYXJHcmFkaWVudD4KICAgICAgICAKICAgICAgICA8IS0tIEdvbGRlbiBUZXh0IEdyYWRpZW50IC0tPgogICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iZ29sZEdyYWQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMCUiIHkyPSIxMDAlIj4KICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2ZlZjA4YSIvPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjQwJSIgc3RvcC1jb2xvcj0iI2ZiYmYyNCIvPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjYwJSIgc3RvcC1jb2xvcj0iI2Q5NzcwNiIvPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNiNDUzMDkiLz4KICAgICAgICA8L2xpbmVhckdyYWRpZW50PgoKICAgICAgICA8bGluZWFyR3JhZGllbnQgaWQ9InJlZEdyYWQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICAgICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjZWY0NDQ0Ii8+CiAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzk5MWIxYiIvPgogICAgICAgIDwvbGluZWFyR3JhZGllbnQ+CgogICAgICAgIDwhLS0gRHJvcCBTaGFkb3dzIC0tPgogICAgICAgIDxmaWx0ZXIgaWQ9ImRyb3BTaGFkb3ciIHg9Ii0yMCUiIHk9Ii0yMCUiIHdpZHRoPSIxNDAlIiBoZWlnaHQ9IjE0MCUiPgogICAgICAgICAgICA8ZmVEcm9wU2hhZG93IGR4PSIwIiBkeT0iMTIiIHN0ZERldmlhdGlvbj0iMTAiIGZsb29kLW9wYWNpdHk9IjAuOCIgZmxvb2QtY29sb3I9IiMwMDAiLz4KICAgICAgICA8L2ZpbHRlcj4KICAgICAgICA8ZmlsdGVyIGlkPSJnbG93IiB4PSItNTAlIiB5PSItNTAlIiB3aWR0aD0iMjAwJSIgaGVpZ2h0PSIyMDAlIj4KICAgICAgICAgICAgPGZlR2F1c3NpYW5CbHVyIHN0ZERldmlhdGlvbj0iOCIgcmVzdWx0PSJibHVyIi8+CiAgICAgICAgICAgIDxmZU1lcmdlPgogICAgICAgICAgICAgICAgPGZlTWVyZ2VOb2RlIGluPSJibHVyIi8+CiAgICAgICAgICAgICAgICA8ZmVNZXJnZU5vZGUgaW49IlNvdXJjZUdyYXBoaWMiLz4KICAgICAgICAgICAgPC9mZU1lcmdlPgogICAgICAgIDwvZmlsdGVyPgogICAgICAgIDxmaWx0ZXIgaWQ9InRleHRHbG93IiB4PSItNTAlIiB5PSItNTAlIiB3aWR0aD0iMjAwJSIgaGVpZ2h0PSIyMDAlIj4KICAgICAgICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjgiIHN0ZERldmlhdGlvbj0iNiIgZmxvb2Qtb3BhY2l0eT0iMC45IiBmbG9vZC1jb2xvcj0iIzAwMCIvPgogICAgICAgIDwvZmlsdGVyPgogICAgPC9kZWZzPgoKICAgIDwhLS0gQmFja2dyb3VuZCBCYXNlIC0tPgogICAgPHJlY3Qgd2lkdGg9IjUxMiIgaGVpZ2h0PSI1MTIiIHJ4PSIxMDAiIGZpbGw9InVybCgjYmdHcmFkKSIgZmlsdGVyPSJ1cmwoI2Ryb3BTaGFkb3cpIi8+CiAgICAKICAgIDwhLS0gRGVjb3JhdGl2ZSBPdXRsaW5lIC0tPgogICAgPHJlY3Qgd2lkdGg9IjQ3MiIgaGVpZ2h0PSI0NzIiIHg9IjIwIiB5PSIyMCIgcng9IjgwIiBmaWxsPSJub25lIiBzdHJva2U9InVybCgjZ29sZEdyYWQpIiBzdHJva2Utd2lkdGg9IjgiIHN0cm9rZS1kYXNoYXJyYXk9IjIwIDEwIiBvcGFjaXR5PSIwLjYiLz4KCiAgICA8IS0tIExpZ2h0IFJheXMgLyBTdGFyYnVyc3QgLS0+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNTYsIDIyMCkiPgogICAgICAgIDxwYXRoIGQ9Ik0wIC0xNTAgTDEwIDAgTDAgMTUwIEwtMTAgMCBaIiBmaWxsPSIjZmZmZmZmIiBvcGFjaXR5PSIwLjEiIHRyYW5zZm9ybT0icm90YXRlKDApIi8+CiAgICAgICAgPHBhdGggZD0iTTAgLTE1MCBMMTAgMCBMMCAxNTAgTC0xMCAwIFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMSIgdHJhbnNmb3JtPSJyb3RhdGUoNDUpIi8+CiAgICAgICAgPHBhdGggZD0iTTAgLTE1MCBMMTAgMCBMMCAxNTAgTC0xMCAwIFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMSIgdHJhbnNmb3JtPSJyb3RhdGUoOTApIi8+CiAgICAgICAgPHBhdGggZD0iTTAgLTE1MCBMMTAgMCBMMCAxNTAgTC0xMCAwIFoiIGZpbGw9IiNmZmZmZmYiIG9wYWNpdHk9IjAuMSIgdHJhbnNmb3JtPSJyb3RhdGUoMTM1KSIvPgogICAgPC9nPgoKICAgIDwhLS0gQ2VudGVyIEJpbmdvIEJhbGwgLS0+CiAgICA8Y2lyY2xlIGN4PSIyNTYiIGN5PSIyMjAiIHI9IjEzMCIgZmlsbD0idXJsKCNyZWRHcmFkKSIgZmlsdGVyPSJ1cmwoI2Ryb3BTaGFkb3cpIi8+CiAgICAKICAgIDwhLS0gQmFsbCBJbm5lciBoaWdobGlnaHQgLS0+CiAgICA8Y2lyY2xlIGN4PSIyNTYiIGN5PSIyMjAiIHI9IjEzMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjQiIG9wYWNpdHk9IjAuMyIvPgogICAgCiAgICA8IS0tIFdoaXRlIENpcmNsZSBjZW50ZXIgLS0+CiAgICA8Y2lyY2xlIGN4PSIyNTYiIGN5PSIyMjAiIHI9IjgwIiBmaWxsPSIjZmZmZmZmIiBmaWx0ZXI9InVybCgjZHJvcFNoYWRvdykiLz4KICAgIAogICAgPCEtLSBTdGFyIERldGFpbHMgb24gdGhlIGJhbGwgLS0+CiAgICA8cGF0aCBkPSJNIDE3MCAxNTAgTCAxODAgMTcwIEwgMjAwIDE3MCBMIDE4MCAxODUgTCAxODUgMjA1IEwgMTcwIDE5MCBMIDE1NSAyMDUgTCAxNjAgMTg1IEwgMTQwIDE3MCBMIDE2MCAxNzAgWiIgZmlsbD0idXJsKCNnb2xkR3JhZCkiIC8+CiAgICA8cGF0aCBkPSJNIDM0MCAxNTAgTCAzNTAgMTcwIEwgMzcwIDE3MCBMIDM1MCAxODUgTCAzNTUgMjA1IEwgMzQwIDE5MCBMIDMyNSAyMDUgTCAzMzAgMTg1IEwgMzEwIDE3MCBMIDMzMCAxNzAgWiIgZmlsbD0idXJsKCNnb2xkR3JhZCkiIC8+CgogICAgPCEtLSltIGJpZyBOdW1iZXIgb3IgQiAtLT4KICAgIDx0ZXh0IHg9IjI1NiIgeT0iMjcwIiBmb250LWZhbWlseT0iJ0ltcGFjdCcsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTQwIiBmb250LXdlaWdodD0iOTAwIiBmaWxsPSIjYjkxYzFjIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXN0eWxlPSJpdGFsaWMiPkI8L3RleHQ+CgogICAgPCEtLSBCSU5HTyBUZXh0IC0tPgogICAgPHRleHQgeD0iMjU2IiB5PSI0NDAiIGZvbnQtZmFtaWx5PSInQXJpYWwgQmxhY2snLCBJbXBhY3QsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iODUiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc3R5bGU9Iml0YWxpYyIgZmlsbD0idXJsKCNnb2xkR3JhZCkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbHRlcj0idXJsKCN0ZXh0R2xvdykiIHN0cm9rZT0iIzc4MzUwZiIgc3Ryb2tlLXdpZHRoPSI0IiBsZXR0ZXItc3BhY2luZz0iNCI+QklOR088L3RleHQ+CiAgICAKICAgIDwhLS0gU0hPVyBUZXh0IC0tPgogICAgPHRleHQgeD0iMjU2IiB5PSI0OTAiIGZvbnQtZmFtaWx5PSInQXJpYWwgQmxhY2snLCBJbXBhY3QsIHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iNDUiIGZvbnQtd2VpZ2h0PSI5MDAiIGZvbnQtc3R5bGU9Iml0YWxpYyIgZmlsbD0iI2ZmZmZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsdGVyPSJ1cmwoI3RleHRHbG93KSIgbGV0dGVyLXNwYWNpbmc9IjEyIj5TSE9XPC90ZXh0PgoKPC9zdmc+';
                        logoEl.classList.remove('hidden');
                    }
                       
                    gameNameEl.textContent = game.name || `Rodada ${eventData.activeGameNumber}`;
                       
                    // Exibir Prêmios
                    const prizeParts = [];
                    const wonPrize1 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize1');
                    const wonPrize2 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize2');
                    const wonPrize3 = game.winners && game.winners.some((w: any) => w.bingoType === 'prize3');

                    if (game.prizes?.prize1) prizeParts.push(`<span class="opacity-70">${labels.prize1Label}:</span> <span class="${wonPrize1 ? 'line-through opacity-50' : ''}">${game.prizes.prize1}</span>`);
                    if (game.prizes?.prize2) prizeParts.push(`<span class="opacity-70">${labels.prize2Label}:</span> <span class="${wonPrize2 ? 'line-through opacity-50' : ''}">${game.prizes.prize2}</span>`);
                    if (game.prizes?.prize3) prizeParts.push(`<span class="opacity-70">${labels.prize3Label}:</span> <span class="${wonPrize3 ? 'line-through opacity-50' : ''}">${game.prizes.prize3}</span>`);
                    
                    gamePrizesEl.innerHTML = prizeParts.join('<span class="mx-2 opacity-30">|</span>');
                       
                    // Called Numbers
                    const calledNumbers = game.calledNumbers || [];
                    lastDrawn = calledNumbers.length > 0 ? calledNumbers[calledNumbers.length - 1] : null;
                       
                    lastNumberEl.textContent = lastDrawn ? lastDrawn.toString() : '-';
                    if (lastDrawn) {
                        lastNumberEl.classList.add('scale-110', 'text-amber-500', 'dark:text-amber-400');
                        setTimeout(() => {
                            lastNumberEl.classList.remove('scale-110', 'text-amber-500', 'dark:text-amber-400');
                        }, 500);
                    }

                    const activeColor = config.boardColor !== 'default' ? config.boardColor : '#ef4444';
                    const activeColorLight = activeColor && (activeColor === '#fef08a' || activeColor === '#fde047' || activeColor.toLowerCase() === '#ffffff');

                    Object.values(cellsByNumber).forEach(cell => {
                        cell.dataset.drawn = 'false';
                    });
                       
                    document.querySelectorAll('[id^="attendee-row-"]').forEach(row => {
                        const nums = row.querySelectorAll('div');
                        nums.forEach(num => num.remove());
                    });

                    calledNumbers.forEach((num: number, index: number) => {
                        const isNewNumber = lastDrawn === num;
                        
                        let targetIdx = 0;
                        ['B', 'I', 'N', 'G', 'O'].forEach((letter, idx) => {
                            const min = BINGO_CONFIG[letter].min;
                            const max = BINGO_CONFIG[letter].max;
                            if (num >= min && num <= max) {
                                targetIdx = idx;
                            }
                        });
                        const row = document.getElementById(`attendee-row-${targetIdx}`);
                        if (row) {
                            const isLast = index === calledNumbers.length - 1;
                            const numDiv = document.createElement('div');
                            
                            const animClass = (isLast && isNewNumber) ? 'animate-bounce-in' : '';
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
                    });"""

if old_code in content:
    content = content.replace(old_code, replacement)
    with open("attendee.tsx", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Failed")
