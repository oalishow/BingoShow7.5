const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

const regex = /let innerHTML = '';[\s\S]*?rightIndex\+\+;/g;

const match = code.match(regex);
if (match) {
    console.log(match[0]);
}
