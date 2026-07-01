const sharp = require('sharp');
const fs = require('fs');

async function generateIcons() {
  const iconSvg = fs.readFileSync('./public/icon.svg');
  const maskedSvg = fs.readFileSync('./public/masked-icon.svg');

  await sharp(iconSvg)
    .resize(192, 192)
    .toFile('./public/pwa-192x192.png');

  await sharp(iconSvg)
    .resize(512, 512)
    .toFile('./public/pwa-512x512.png');

  await sharp(maskedSvg)
    .resize(512, 512)
    .toFile('./public/pwa-512x512-maskable.png');

  console.log('PNG icons generated successfully.');
}

generateIcons().catch(console.error);
