const fs = require('fs');
let code = fs.readFileSync('index.tsx', 'utf8');

// Replace the manual checks for 'dark' class with Tailwind responsive classes in Bingo board rendering.
code = code.replace(/if \(document\.documentElement\.classList\.contains\('dark'\)\) cell\.classList\.add\('text-slate-200'\); else cell\.classList\.add\('text-slate-800'\);;/g, "cell.classList.add('text-slate-800', 'dark:text-slate-200');");

// Same for the other location where it appears (line 2504 in older iterations, though we might have changed it)
// Let's also do a broader regex just in case
code = code.replace(/if\s*\(document\.documentElement\.classList\.contains\('dark'\)\)\s*cell\.classList\.add\('text-slate-200'\);\s*else\s*cell\.classList\.add\('text-slate-800'\);+/g, "cell.classList.add('text-slate-800', 'dark:text-slate-200');");

// Let's also ensure `updateLastNumbers` uses responsive classes instead of hardcoded 'bg-gray-700 text-slate-100'
code = code.replace(/numberEl\.className = 'bg-gray-700 text-slate-100 font-bold rounded-lg/g, "numberEl.className = 'bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-slate-100 font-bold rounded-lg");

// Also check the clearMasterBoard hardcoding size, which might wipe out the CSS. We should change it to preserve responsive sizes but the original code hardcoded it, let's just make sure it has the right classes.
fs.writeFileSync('index.tsx', code);
