import re

with open("index.tsx") as f:
    tsx = f.read()

# in showFloatingNumber
replacement = """        function showFloatingNumber(number: number) {
            const { activeGameNumber, gamesData, appConfig } = appStore.state;
            if (!activeGameNumber) {
                showAlert("Por favor, selecione uma rodada clicando em 'Jogar' para iniciar.");
                return;
            }
            const game = gamesData[activeGameNumber];
            if (!game) {
                console.error(`Erro: Rodada ativa ${activeGameNumber} não encontrada.`);
                return;
            }

            if (game.calledNumbers.includes(number)) {
                showError(`O número ${number} já foi anunciado.`);
                return;
            }

            appStore.state.pendingNumber = number;
            appStore.debouncedFirebaseSync(true);

            const individualSponsor = appConfig.sponsorsByNumber[number];"""

tsx = tsx.replace("""        function showFloatingNumber(number: number) {
            const { activeGameNumber, gamesData, appConfig } = appStore.state;
            if (!activeGameNumber) {
                showAlert("Por favor, selecione uma rodada clicando em 'Jogar' para iniciar.");
                return;
            }
            const game = gamesData[activeGameNumber];
            if (!game) {
                console.error(`Erro: Rodada ativa ${activeGameNumber} não encontrada.`);
                return;
            }

            if (game.calledNumbers.includes(number)) {
                showError(`O número ${number} já foi anunciado.`);
                return;
            }

            const individualSponsor = appConfig.sponsorsByNumber[number];""", replacement)

with open("index.tsx", "w") as f:
    f.write(tsx)
