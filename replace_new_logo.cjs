const fs = require('fs');

let content = fs.readFileSync('index.tsx', 'utf8');

const svgContent = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#4F46E5"/>
            <stop offset="100%" stop-color="#2563EB"/>
        </linearGradient>
        <radialGradient id="ballOuter" cx="30%" cy="30%" r="70%">
            <stop offset="0%" stop-color="#F87171"/>
            <stop offset="100%" stop-color="#991B1B"/>
        </radialGradient>
        <radialGradient id="ballHighlight" cx="35%" cy="35%" r="50%">
            <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="textGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#FEF08A"/>
            <stop offset="50%" stop-color="#F59E0B"/>
            <stop offset="100%" stop-color="#D97706"/>
        </linearGradient>
        <filter id="shadow">
            <feDropShadow dx="0" dy="10" stdDeviation="15" flood-opacity="0.5" flood-color="#000000"/>
        </filter>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <filter id="textShadow">
            <feDropShadow dx="0" dy="6" stdDeviation="5" flood-opacity="0.6" flood-color="#000000"/>
        </filter>
    </defs>

    <rect width="512" height="512" rx="128" fill="url(#bg)" filter="url(#shadow)"/>
    <rect width="472" height="472" x="20" y="20" rx="108" fill="none" stroke="#FFFFFF" stroke-opacity="0.2" stroke-width="4"/>

    <path d="M100 130 Q100 90 140 90 Q100 90 100 50 Q100 90 60 90 Q100 90 100 130" fill="#FDE047" opacity="0.9" filter="url(#glow)"/>
    <path d="M420 200 Q420 180 440 180 Q420 180 420 160 Q420 180 400 180 Q420 180 420 200" fill="#FDE047" opacity="0.7" filter="url(#glow)"/>
    <path d="M430 80 Q430 60 450 60 Q430 60 430 40 Q430 60 410 60 Q430 60 430 80" fill="#FDE047" opacity="0.8" filter="url(#glow)"/>

    <circle cx="256" cy="220" r="140" fill="url(#ballOuter)" filter="url(#shadow)"/>
    <circle cx="256" cy="220" r="140" fill="url(#ballHighlight)"/>
    <circle cx="256" cy="220" r="75" fill="#FFFFFF" filter="url(#shadow)"/>

    <text x="256" y="260" font-family="'Arial Black', Impact, sans-serif" font-size="110" font-weight="900" fill="#1F2937" text-anchor="middle" letter-spacing="-4">75</text>

    <text x="256" y="440" font-family="'Arial Black', Impact, sans-serif" font-size="76" font-weight="900" font-style="italic" fill="url(#textGrad)" text-anchor="middle" filter="url(#textShadow)" stroke="#451A03" stroke-width="3" letter-spacing="2">BINGO SHOW</text>
    <path d="M100 460 Q256 490 412 460" fill="none" stroke="#FDE047" stroke-width="6" stroke-linecap="round" filter="url(#glow)"/>
</svg>`;

const b64 = "data:image/svg+xml;base64," + Buffer.from(svgContent).toString('base64');

content = content.replace(/customLogoBase64:\s*'data:image\/svg\+xml;base64,[^']+'/g, 'customLogoBase64: ' + "'" + b64 + "'");
content = content.replace(/const fixedDefaultLogo = 'data:image\/svg\+xml;base64,[^']+';/g, 'const fixedDefaultLogo = ' + "'" + b64 + "'" + ';');

fs.writeFileSync('index.tsx', content);
console.log('Logo replaced');
