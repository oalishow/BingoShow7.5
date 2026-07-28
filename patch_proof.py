import re

with open('index.tsx', 'r') as f:
    content = f.read()

old_css = """            <title>Relatório de Resultados - ${appConfig.bingoTitle}</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 4rem; color: #333; line-height: 1.6; }
                h1 { text-align: center; color: #1a365d; margin-bottom: 0.5rem; font-size: 2.5em; text-transform: uppercase; letter-spacing: 1px; }
                .subtitle { text-align: center; color: #64748b; font-size: 1.1em; margin-bottom: 3rem; }
                h2 { color: #2563eb; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 3rem; font-size: 1.8em; }
                table { width: 100%; border-collapse: collapse; margin-top: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
                th, td { border: 1px solid #e2e8f0; padding: 12px 16px; text-align: left; }
                th { background-color: #f8fafc; color: #475569; font-weight: 600; text-transform: uppercase; font-size: 0.9em; letter-spacing: 0.5px; }
                tr:nth-child(even) { background-color: #f8fafc; }
                .numbers { font-size: 0.9em; word-break: break-all; color: #475569; font-family: monospace; }
                .signature-section { margin-top: 6rem; text-align: center; page-break-inside: avoid; }
                .signature-line { width: 400px; border-bottom: 1px solid #333; margin: 0 auto; }
                .signature-name { margin-top: 15px; font-weight: bold; font-size: 1.2em; color: #1e293b; }
                .signature-title { margin-top: 5px; color: #64748b; font-size: 1em; }
                .declaration { margin-top: 4rem; padding: 2rem; background-color: #f1f5f9; border-radius: 8px; border-left: 4px solid #3b82f6; text-align: justify; font-size: 1.1em; }
                @media print {
                    body { margin: 2rem; }
                    .declaration { background-color: transparent; border: 1px solid #cbd5e1; }
                }
            </style>
        </head>
        <body>
            <h1>${appConfig.bingoTitle}</h1>
            <p class="subtitle">Relatório Oficial de Resultados<br>Gerado em: ${new Date().toLocaleString('pt-BR')}</p>"""

new_css = """            <title>Relatório de Resultados - ${appConfig.bingoTitle}</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 4rem; color: #333; line-height: 1.6; }
                .header { text-align: center; margin-bottom: 2rem; }
                .logo { max-width: 150px; max-height: 150px; margin-bottom: 1rem; object-fit: contain; }
                h1 { color: #1a365d; margin-bottom: 0.2rem; font-size: 2.5em; text-transform: uppercase; letter-spacing: 1px; margin-top: 0; }
                .subtitle { color: #64748b; font-size: 1.1em; margin-bottom: 3rem; }
                h2 { color: #2563eb; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 3rem; font-size: 1.8em; }
                table { width: 100%; border-collapse: collapse; margin-top: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
                th, td { border: 1px solid #e2e8f0; padding: 12px 16px; text-align: left; }
                th { background-color: #f8fafc; color: #475569; font-weight: 600; text-transform: uppercase; font-size: 0.9em; letter-spacing: 0.5px; }
                tr:nth-child(even) { background-color: #f8fafc; }
                .numbers { font-size: 0.9em; word-break: break-all; color: #475569; font-family: monospace; }
                .signature-section { margin-top: 6rem; text-align: center; page-break-inside: avoid; }
                .signature-line { width: 400px; border-bottom: 1px solid #333; margin: 0 auto; }
                .signature-name { margin-top: 15px; font-weight: bold; font-size: 1.2em; color: #1e293b; }
                .signature-title { margin-top: 5px; color: #64748b; font-size: 1em; }
                .declaration { margin-top: 4rem; padding: 2rem; background-color: #f1f5f9; border-radius: 8px; border-left: 4px solid #3b82f6; text-align: justify; font-size: 1.1em; }
                @media print {
                    body { margin: 2rem; }
                    .declaration { background-color: transparent; border: 1px solid #cbd5e1; }
                }
            </style>
        </head>
        <body>
            <div class="header">
                ${appConfig.customLogoBase64 ? `<img src="${appConfig.customLogoBase64}" class="logo" alt="Logo do Evento">` : ''}
                <h1>${appConfig.bingoTitle}</h1>
                <p class="subtitle">Relatório Oficial de Resultados<br>Gerado em: ${new Date().toLocaleString('pt-BR')}<br>Sistema: ${appConfig.appName || 'Bingo Show'}</p>
            </div>"""

if old_css in content:
    content = content.replace(old_css, new_css)
    print("Patch successful!")
else:
    print("Could not find the target string!")

with open('index.tsx', 'w') as f:
    f.write(content)
