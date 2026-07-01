const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const oldFunc = `        const fileToBase64 = (file: File, maxWidth = 800, maxHeight = 800, quality = 0.8): Promise<string> =>
            new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = (event) => {
                    const img = new Image();
                    img.src = event.target?.result as string;
                    img.onload = () => {
                        let width = img.width;
                        let height = img.height;
                        if (width > maxWidth || height > maxHeight) {
                            const ratio = Math.min(maxWidth / width, maxHeight / height);
                            width *= ratio;
                            height *= ratio;
                        }
                        const canvas = document.createElement('canvas');
                        canvas.width = width;
                        canvas.height = height;
                        const ctx = canvas.getContext('2d');
                        if (!ctx) {
                            resolve(reader.result as string); // fallback
                            return;
                        }
                        ctx.drawImage(img, 0, 0, width, height);
                        
                        // Preserve transparency using WebP (or PNG for older browsers, though WebP is widely supported now)
                        if (file.type === 'image/png') { 
                             // Use PNG for pristine logos if they specifically uploaded a PNG and size is small enough, but webp is safer for compression. 
                             // Actually, let's just use WebP for everything as it supports transparency and compression.
                        }
                        const dataUrl = canvas.toDataURL('image/webp', quality);
                        resolve(dataUrl);
                    };
                    img.onerror = (error) => reject(error);
                };
                reader.onerror = error => reject(error);
            });`;

const newFunc = `        const fileToBase64 = (file: File): Promise<string> =>
            new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = (event) => {
                    resolve(event.target?.result as string);
                };
                reader.onerror = error => reject(error);
            });`;

code = code.replace(oldFunc, newFunc);
fs.writeFileSync('index.tsx', code);
