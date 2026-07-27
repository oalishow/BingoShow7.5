import re

with open("index.tsx") as f:
    tsx = f.read()

replacement = """                    const loadedState = JSON.parse(result);
                    
                    if (!loadedState.gamesData || !loadedState.appConfig) {
                         throw new Error("O arquivo selecionado não parece ser um backup válido do Bingo Show.");
                    }

                    const currentEventId = appStore.state.appConfig.eventId;
                    let keepCurrentQr = false;
                    if (currentEventId && loadedState.appConfig.eventId && currentEventId !== loadedState.appConfig.eventId) {
                        keepCurrentQr = confirm("Este backup pertence a um evento/painel diferente.\n\nDeseja MANTER o seu QR Code/Link atual para o público?\n\n[OK] Sim, manter o link atual.\n[Cancelar] Não, restaurar o link do backup.");
                    }

                    appStore.loadStateFromObject(loadedState);
                    
                    if (keepCurrentQr && currentEventId) {
                        appStore.state.appConfig.eventId = currentEventId;
                        appStore.state.appConfig.onlineSyncEnabled = true;
                    }
                    """

tsx = re.sub(
    r"const loadedState = JSON\.parse\(result\);\s*if \(!loadedState\.gamesData \|\| !loadedState\.appConfig\) \{\s*throw new Error\(\"O arquivo selecionado não parece ser um backup válido do Bingo Show\.\"\);\s*\}\s*appStore\.loadStateFromObject\(loadedState\);",
    replacement,
    tsx
)

with open("index.tsx", "w") as f:
    f.write(tsx)
