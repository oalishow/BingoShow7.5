const fs = require('fs');

const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
    <defs>
        <linearGradient id="main-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#3b82f6" />
            <stop offset="100%" stop-color="#8b5cf6" />
        </linearGradient>
        <linearGradient id="gloss" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="white" stop-opacity="0.3" />
            <stop offset="100%" stop-color="white" stop-opacity="0" />
        </linearGradient>
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceAlpha" stdDeviation="15" />
            <feOffset dx="0" dy="10" />
            <feComponentTransfer>
                <feFuncA type="linear" slope="0.5" />
            </feComponentTransfer>
            <feMerge>
                <feMergeNode />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
    </defs>

    <!-- Base Circle -->
    <circle cx="256" cy="256" r="230" fill="url(#main-bg)" filter="url(#shadow)" />
    
    <!-- Gloss Effect -->
    <path d="M70 150 Q256 50 442 150 Q256 250 70 150" fill="url(#gloss)" />

    <!-- Main Content -->
    <g transform="translate(256, 256)">
        <!-- Central Ball -->
        <circle r="140" fill="rgba(255,255,255,0.15)" stroke="white" stroke-width="2" />
        
        <!-- Large B -->
        <text y="40" font-family="system-ui, sans-serif" font-weight="900" font-size="200" fill="white" text-anchor="middle" style="text-shadow: 0 10px 30px rgba(0,0,0,0.3)">B</text>
        
        <!-- Bingo Text -->
        <text y="100" font-family="system-ui, sans-serif" font-weight="900" font-size="40" fill="#fbbf24" text-anchor="middle" letter-spacing="10" transform="translate(0, 40)">BINGO</text>
        <text y="150" font-family="system-ui, sans-serif" font-weight="700" font-size="25" fill="white" text-anchor="middle" letter-spacing="15" opacity="0.8" transform="translate(0, 40)">SHOW</text>
    </g>

    <!-- Floating Balls -->
    <circle cx="100" cy="100" r="30" fill="#f43f5e" filter="url(#shadow)" opacity="0.9" />
    <text x="100" y="108" font-family="sans-serif" font-weight="bold" font-size="20" fill="white" text-anchor="middle">7</text>

    <circle cx="412" cy="150" r="25" fill="#10b981" filter="url(#shadow)" opacity="0.9" />
    <text x="412" y="157" font-family="sans-serif" font-weight="bold" font-size="16" fill="white" text-anchor="middle">3</text>

    <circle cx="120" cy="400" r="35" fill="#f59e0b" filter="url(#shadow)" opacity="0.9" />
    <text x="120" y="410" font-family="sans-serif" font-weight="bold" font-size="24" fill="white" text-anchor="middle">V</text>

    <!-- Version Badge -->
    <g transform="translate(430, 410)">
        <rect x="-40" y="-20" width="80" height="40" rx="20" fill="white" />
        <text dy="7" font-family="sans-serif" font-weight="bold" font-size="18" fill="#1e293b" text-anchor="middle">v7.3</text>
    </g>
</svg>`;

const b64 = 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');

let code = fs.readFileSync('index.tsx', 'utf8');
code = code.replace(/customLogoBase64:\s*'data:image\/svg\+xml;base64,[^']+'/, `customLogoBase64: '${b64}'`);

// Re-applying the fix for the default logo placeholder in renderCustomLogo if needed
// Actually let's just make sure the DEFAULT_LOGO_BASE64 part is updated if I used it before
code = code.replace(/const defaultLogo = 'data:image\/svg\+xml;base64,[^']+';/, `const defaultLogo = '${b64}';`);

fs.writeFileSync('index.tsx', code);
