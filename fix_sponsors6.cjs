const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

code = code.replace(
    'let finalConfettiInterval: any;',
    'let finalConfettiInterval: any;\n        let finalSponsorsInterval: any;'
);

code = code.replace(
    'let finalSponsorsInterval: any;',
    '' // remove the inner declaration, wait! The first replace already adds it... let's just do a specific replace for the inner one
);

fs.writeFileSync('index.tsx', code);
