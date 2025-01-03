let tempoTrabalho = 0;
let tempoDescanso = 0;
let tempoAtual = 0; // Tempo restante em segundos
let intervalId = null;
let isPaused = true; // Estado inicial pausado

function registrarValores() {
    // Captura os valores dos inputs
    tempoTrabalho = parseInt(document.getElementById('tempoTrabalho').value) || 0;
    tempoDescanso = parseInt(document.getElementById('tempoDescanso').value) || 0;

    // Converte o tempo de trabalho para segundos e define como tempo atual
    tempoAtual = tempoTrabalho * 60;

    // Atualiza o display do timer
    atualizaDisplay(tempoAtual);

    // Habilita o botão de iniciar/pausar
    const pausePlayButton = document.getElementById("pausePlayButton");
    pausePlayButton.textContent = "Play";
    pausePlayButton.disabled = false;
}

function atualizaDisplay(tempo) {
    const minutos = String(Math.floor(tempo / 60)).padStart(2, '0');
    const segundos = String(tempo % 60).padStart(2, '0');
    document.getElementById("displayTempo").textContent = `${minutos}:${segundos}`;
}

function pausePlayTimer() {
    const pausePlayButton = document.getElementById("pausePlayButton");

    if (isPaused) {
        // Retomar ou iniciar o timer
        pausePlayButton.textContent = "Pause";
        isPaused = false;

        // Inicia o intervalo para contagem regressiva
        intervalId = setInterval(() => {
            if (tempoAtual > 0) {
                tempoAtual--;
                atualizaDisplay(tempoAtual);
            } else {
                // Quando o tempo acabar, pausa o timer
                clearInterval(intervalId);
                alert("Tempo finalizado!");
                isPaused = true;
                pausePlayButton.textContent = "Play";
            }
        }, 1000);
    } else {
        // Pausar o timer
        pausePlayButton.textContent = "Play";
        isPaused = true;
        clearInterval(intervalId);
    }
}
