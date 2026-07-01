const fs = require('fs');

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#4F46E5" />
            <stop offset="100%" stop-color="#7C3AED" />
        </linearGradient>
        <filter id="shadow">
            <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity="0.4"/>
        </filter>
    </defs>
    <circle cx="256" cy="256" r="240" fill="url(#bg)" filter="url(#shadow)" />
    <g transform="translate(60, 160)">
        <g transform="translate(0, 0)">
            <circle cx="40" cy="40" r="40" fill="#EF4444" filter="url(#shadow)"/>
            <circle cx="40" cy="40" r="30" fill="#FFFFFF" opacity="0.95"/>
            <text x="40" y="52" font-family="sans-serif" font-weight="900" font-size="40" fill="#1F2937" text-anchor="middle">B</text>
        </g>
        <g transform="translate(85, -40)">
            <circle cx="40" cy="40" r="40" fill="#3B82F6" filter="url(#shadow)"/>
            <circle cx="40" cy="40" r="30" fill="#FFFFFF" opacity="0.95"/>
            <text x="40" y="52" font-family="sans-serif" font-weight="900" font-size="40" fill="#1F2937" text-anchor="middle">I</text>
        </g>
        <g transform="translate(170, -60)">
            <circle cx="40" cy="40" r="40" fill="#10B981" filter="url(#shadow)"/>
            <circle cx="40" cy="40" r="30" fill="#FFFFFF" opacity="0.95"/>
            <text x="40" y="52" font-family="sans-serif" font-weight="900" font-size="40" fill="#1F2937" text-anchor="middle">N</text>
        </g>
        <g transform="translate(255, -40)">
            <circle cx="40" cy="40" r="40" fill="#F59E0B" filter="url(#shadow)"/>
            <circle cx="40" cy="40" r="30" fill="#FFFFFF" opacity="0.95"/>
            <text x="40" y="52" font-family="sans-serif" font-weight="900" font-size="40" fill="#1F2937" text-anchor="middle">G</text>
        </g>
        <g transform="translate(340, 0)">
            <circle cx="40" cy="40" r="40" fill="#EC4899" filter="url(#shadow)"/>
            <circle cx="40" cy="40" r="30" fill="#FFFFFF" opacity="0.95"/>
            <text x="40" y="52" font-family="sans-serif" font-weight="900" font-size="40" fill="#1F2937" text-anchor="middle">O</text>
        </g>
    </g>
    <text x="256" y="380" font-family="sans-serif" font-weight="900" font-size="70" fill="#FFFFFF" text-anchor="middle" filter="url(#shadow)" letter-spacing="2">BINGO</text>
    <text x="256" y="440" font-family="sans-serif" font-weight="700" font-size="40" fill="#E0E7FF" text-anchor="middle" letter-spacing="4">SHOW</text>
</svg>`;

const b64 = 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');

let code = fs.readFileSync('index.tsx', 'utf8');
code = code.replace(/customLogoBase64:\s*'data:image\/svg\+xml;base64,[^']+'/, `customLogoBase64: '${b64}'`);

// Apenas garantindo que o tema claro nas rodadas também seja atualizado:
code = code.replace(/bg-gray-700 p-4 rounded-xl shadow-lg transition-all/g, 'bg-gray-100 dark:bg-gray-700 p-4 rounded-xl shadow-lg transition-all');
code = code.replace(/text-lg font-bold text-white/g, 'text-lg font-bold text-slate-800 dark:text-white');
// Ícone reabrir rodada e jogar
code = code.replace(/<button class="w-full bg-gray-500 text-white font-bold py-2 px-4 rounded-lg text-sm cursor-pointer reopen-btn">Reabrir Rodada<\/button>/g, '<button class="w-full bg-gray-500 text-white font-bold py-2 px-4 rounded-lg text-sm cursor-pointer reopen-btn">🔄 Reabrir Rodada</button>');
code = code.replace(/isActive \? 'Jogando\.\.\.' : 'Jogar'/g, 'isActive ? \'▶️ Jogando...\' : \'▶️ Jogar\'');

fs.writeFileSync('index.tsx', code);
