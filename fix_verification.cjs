const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

code = code.replace(/if \(document\.documentElement\.classList\.contains\('dark'\)\) numberEl\.classList\.toggle\('text-slate-200'\); else numberEl\.classList\.toggle\('text-slate-800'\);;/g, "numberEl.classList.toggle('text-slate-800'); numberEl.classList.toggle('dark:text-slate-200');");

fs.writeFileSync('index.tsx', code);
