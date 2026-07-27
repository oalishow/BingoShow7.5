sed -i '/<!-- Board (Letras Verticais) -->/i \
            <!-- Leilão em Andamento -->\
            <div id="attendee-auction-card" class="hidden bg-brand-card border border-brand-border rounded-xl p-3 shadow-lg flex-col relative overflow-hidden transition-colors duration-500">\
                <span class="w-full text-left text-[10px] sm:text-xs font-black text-amber-500 uppercase tracking-widest mb-2 z-10 flex items-center gap-1">\
                    💎 Leilão\
                </span>\
                <div class="bg-brand-bg border border-brand-border rounded-lg p-3 flex flex-col justify-center items-center z-10 transition-colors duration-500">\
                    <span id="attendee-auction-item" class="text-white font-bold text-sm sm:text-base text-center">Item</span>\
                    <div class="flex items-baseline gap-2 mt-1">\
                        <span class="text-amber-500 font-bold text-xs">LANCE:</span>\
                        <span id="attendee-auction-bid" class="text-3xl sm:text-4xl font-black text-amber-500 drop-shadow-md">R$ 0,00</span>\
                    </div>\
                </div>\
            </div>\
' attendee.html
