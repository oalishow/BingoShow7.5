const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regex = /const fileToBase64 = \(file: File, maxWidth = 800, maxHeight = 800, quality = 0\.8\): Promise<string> =>[\s\S]*?reader\.onerror = error => reject\(error\);\n            \}\);/g;

const newFunc = `const fileToBase64 = (file: File): Promise<string> =>
            new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = (event) => {
                    resolve(event.target?.result as string);
                };
                reader.onerror = error => reject(error);
            });`;

code = code.replace(regex, newFunc);
fs.writeFileSync('index.tsx', code);
