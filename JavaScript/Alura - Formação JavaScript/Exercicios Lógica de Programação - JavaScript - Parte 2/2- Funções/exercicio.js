// 1- Criar uma função que exibe "Olá, mundo!" no console.
function exibirOla() {
    console.log('Olá, Mundo!');
}
exibirOla();

// 2- Criar uma função que recebe um nome como parâmetro e exibe "Olá, [nome]!" no console.
function recebeNome(nome) {
    console.log(`Olá ${nome}!`)
}
recebeNome('Alice');

// 3- Criar uma função que recebe um número como parâmetro e retorna o dobro desse número.
function recebeNumero(numero) {
    return numero * 2;
}
let resultadoNumero = (2);
console.log(resultadoNumero);

// 4- Criar uma função que recebe três números como parâmetros e retorna a média deles.
function RecebeTresNuemeros(numero1, numero2, numero3){
    return (numero1 + numero2 + numero3) / 3;
}
let media = calcularMedia(4, 7, 10);
console.log(media);

// 5- Criar uma função que recebe dois números como parâmetros e retorna o maior deles.
function RecebeDoisNumeros(N1, N2) {
    return N1 > N2 ? N1 : N2;
}
let maiorNuemero = RecebeDoisNumeros(15, 9);
console.log(Maior);

// 6- Criar uma função que recebe um número como parâmetro e retorna o resultado da multiplicação desse número por ele mesmo
function Quadrado(numero) {
    return numero * numero;
}
  
let resultado = quadrado(2);
console.log(resultado); 