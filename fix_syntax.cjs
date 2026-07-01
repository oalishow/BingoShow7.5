const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

code = code.replace(/cell\.classList\.add\(''bg-gray-200/g, "cell.classList.add('bg-gray-200");
code = code.replace(/cell\.classList\.remove\(''bg-gray-200/g, "cell.classList.remove('bg-gray-200");

fs.writeFileSync('index.tsx', code);
