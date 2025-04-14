// iniciando o canvas 
var canvas = document.getElementById('progress') //  pega o elemento <canvas> do HTML que tem o id="progress"
var ctx = canvas.getContext('2d'); //  ctx.fillRect() para desenhar retângulo 
var atualiza = setInterval(animacao, 100); // chama a função animacao() a cada 100 milissegundos (0,1 segundo), repetidamente.

// configurações
var x = 0;
var y = 0;
var altura = 10;
var largura = 0;
var fator = 60;
var resolucao = 1920;

// cor da barra requisitada pela equipe
ctx.fillStyle = "#4169E1"; 

// função animada da barra de progresso
function animacao(){
    ctx.fillRect(x, y, largura = largura+fator, altura);

    // codigo avançado: interrompe a função setInterval() para evitar carregamento excessivo.
    if(largura > resolucao){
        clearInterval(atualiza);
    }
}