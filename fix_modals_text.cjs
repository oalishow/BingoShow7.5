const fs = require('fs');
let content = fs.readFileSync('index.tsx', 'utf8');

let modalChunkStart = content.indexOf('function getModalTemplates() {');
let modalChunkEnd = content.indexOf('function applyBoardZoom', modalChunkStart); // Function right after?
if (modalChunkEnd === -1) {
    modalChunkEnd = content.indexOf('function openModal(', modalChunkStart); 
}
if (modalChunkEnd === -1) {
    modalChunkEnd = content.indexOf('function generateShortUUID', modalChunkStart);
}
if (modalChunkEnd === -1) {
    modalChunkEnd = content.indexOf('function renderUIFromState', modalChunkStart);
}
if (modalChunkEnd === -1) {
    modalChunkEnd = content.length; // Just in case
}

if (modalChunkStart !== -1 && modalChunkEnd !== -1) {
    let chunk = content.substring(modalChunkStart, modalChunkEnd);
    
    // Better regex for white text replacing
    chunk = chunk.replace(/<h2([^>]*)text-white([^>]*)>/g, '<h2$1text-gray-900 dark:text-white$2>');
    chunk = chunk.replace(/<h3([^>]*)text-white([^>]*)>/g, '<h3$1text-gray-900 dark:text-white$2>');
    chunk = chunk.replace(/<h4([^>]*)text-white([^>]*)>/g, '<h4$1text-gray-900 dark:text-white$2>');
    chunk = chunk.replace(/<p([^>]*)text-white([^>]*)>/g, '<p$1text-gray-900 dark:text-white$2>');
    chunk = chunk.replace(/<div([^>]*)text-white([^>]*)>/g, '<div$1text-gray-900 dark:text-white$2>');
    
    // Other texts
    chunk = chunk.replace(/text-slate-300/g, 'text-slate-700 dark:text-slate-300');
    chunk = chunk.replace(/text-slate-400/g, 'text-slate-600 dark:text-slate-400');
    
    // Backgrounds
    chunk = chunk.replace(/bg-gray-700/g, 'bg-gray-200 dark:bg-gray-700');
    chunk = chunk.replace(/bg-gray-900/g, 'bg-gray-100 dark:bg-gray-900');
    chunk = chunk.replace(/border-gray-600/g, 'border-gray-300 dark:border-gray-600');
    
    content = content.substring(0, modalChunkStart) + chunk + content.substring(modalChunkEnd);
    fs.writeFileSync('index.tsx', content);
    console.log('Fixed modals');
}
