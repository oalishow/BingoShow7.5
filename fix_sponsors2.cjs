const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regex = /nameInput\.addEventListener\('change', \(e\) => \{[\s\S]*?row\.appendChild\(removeImageBtn\);/g;

const replaceStr = `nameInput.addEventListener('input', (e) => {
            if (!appStore.state.appConfig.sponsorsByNumber[i]) appStore.state.appConfig.sponsorsByNumber[i] = { name: '', image: '' };
            appStore.state.appConfig.sponsorsByNumber[i].name = (e.target as HTMLInputElement).value;
            appStore.debouncedSave();
        });

        const imageContainer = document.createElement('div');
        imageContainer.className = 'flex items-center gap-2';

        const imageInput = document.createElement('input');
        imageInput.type = 'file';
        imageInput.accept = 'image/*';
        imageInput.className = 'text-xs text-slate-600 dark:text-slate-400 file:mr-2 file:py-1 file:px-2 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-sky-50 file:text-sky-700 hover:file:bg-sky-100 w-full';
        
        const imagePreview = document.createElement('img');
        imagePreview.className = 'w-8 h-8 object-contain rounded bg-white';
        if (sponsor.image) {
            imagePreview.src = sponsor.image;
            imagePreview.style.display = 'block';
        } else {
            imagePreview.style.display = 'none';
        }

        imageInput.addEventListener('change', async (e) => {
            const file = (e.target as HTMLInputElement).files?.[0];
            if (file) {
                const base64 = await fileToBase64(file);
                if (!appStore.state.appConfig.sponsorsByNumber[i]) appStore.state.appConfig.sponsorsByNumber[i] = { name: '', image: '' };
                appStore.state.appConfig.sponsorsByNumber[i].image = base64;
                imagePreview.src = base64;
                imagePreview.style.display = 'block';
                appStore.debouncedSave();
                renderMasterBoard();
            }
        });

        imageContainer.appendChild(imagePreview);
        imageContainer.appendChild(imageInput);

        const removeImageBtn = document.createElement('button');
        removeImageBtn.innerHTML = '🗑️';
        removeImageBtn.title = 'Remover imagem do patrocinador';
        removeImageBtn.className = 'text-slate-600 dark:text-slate-400 hover:text-red-500 rounded p-1 text-sm transition-colors';
        removeImageBtn.addEventListener('click', () => {
            if (appStore.state.appConfig.sponsorsByNumber[i]) {
                appStore.state.appConfig.sponsorsByNumber[i].image = '';
                deleteSponsorImage(i.toString());
                imageInput.value = '';
                imagePreview.src = '';
                imagePreview.style.display = 'none';
                appStore.debouncedSave();
                renderMasterBoard();
            }
        });

        row.appendChild(numberLabel);
        row.appendChild(nameInput);
        row.appendChild(imageContainer);
        row.appendChild(removeImageBtn);`;

if (regex.test(code)) {
    code = code.replace(regex, replaceStr);
    fs.writeFileSync('index.tsx', code);
    console.log("REPLACED nameInput event and image logic!");
} else {
    console.log("REGEX FAILED for fix_sponsors2");
}
