const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const replacement1 = `const isDarkTheme = document.documentElement.classList.contains('dark');
            const defaultBg = isDarkTheme ? '#1e293b' : '#f1f5f9';
            const bgColor = roundColor || (appConfig.boardColor !== 'default' ? appConfig.boardColor : defaultBg);`;

code = code.replace(/const bgColor = roundColor \|\| \(appConfig\.boardColor !== 'default' \? appConfig\.boardColor : '#f1f5f9'\);/g, replacement1);

fs.writeFileSync('index.tsx', code);
