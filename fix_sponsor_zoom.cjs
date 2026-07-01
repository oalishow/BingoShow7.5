const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const oldZoomFunc = `            const applyZoom = (scale: number) => {
                displayWrapper.style.zoom = \`\${scale}%\`;
                if (zoomValue) zoomValue.textContent = \`\${scale}%\`;
                appStore.state.appConfig.sponsorDisplayZoom = scale;
            };`;

const newZoomFunc = `            const applyZoom = (scale: number) => {
                displayWrapper.style.transform = \`scale(\${scale / 100})\`;
                displayWrapper.style.transformOrigin = 'center';
                if (zoomValue) zoomValue.textContent = \`\${scale}%\`;
                appStore.state.appConfig.sponsorDisplayZoom = scale;
            };`;

const oldNumZoomFunc = `            const applyNumZoom = (scale: number) => {
                numberDisplay.style.zoom = \`\${scale}%\`;
                if (numZoomValue) numZoomValue.textContent = \`\${scale}%\`;
                appStore.state.appConfig.sponsorNumberZoom = scale;
            };`;

const newNumZoomFunc = `            const applyNumZoom = (scale: number) => {
                numberDisplay.style.transform = \`scale(\${scale / 100})\`;
                numberDisplay.style.transformOrigin = 'top left';
                if (numZoomValue) numZoomValue.textContent = \`\${scale}%\`;
                appStore.state.appConfig.sponsorNumberZoom = scale;
            };`;

code = code.replace(oldZoomFunc, newZoomFunc);
code = code.replace(oldNumZoomFunc, newNumZoomFunc);
fs.writeFileSync('index.tsx', code);
