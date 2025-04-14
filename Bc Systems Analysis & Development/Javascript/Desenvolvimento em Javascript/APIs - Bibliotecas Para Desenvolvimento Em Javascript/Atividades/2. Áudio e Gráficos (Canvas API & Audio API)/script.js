// Pegando o canvas e o contexto 2D
var canvas = document.getElementById('figura');
var ctx = canvas.getContext('2d');

// Definindo as coordenadas do centro e o raio
let centroX = canvas.width / 2;
let centroY = canvas.height / 2;
let raio = 150;

ctx.beginPath();
ctx.arc(centroX, centroY, raio, 0, 2 * Math.PI);
ctx.fillStyle = 'red'; // cor do preenchimento
ctx.fill(); 

let som = new Audio("c:\Users\Josue\Desktop\SOUND EFFECT - LOVE MOMENT.mp3");

figura = canvas.addEventListener("click", function (){
    som.play();
})