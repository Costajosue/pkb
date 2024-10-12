// 1- Crie uma função que calcule o índice de massa corporal (IMC) de uma pessoa, a partir de sua altura, em metros, e peso, em quilogramas, que serão recebidos como parâmetro.
 function calcularIndice(peso, altura){
    let imc = peso / (altura * altura);
 }



 // 2- Crie uma função que calcule o valor do fatorial de um número passado como parâmetro.
 function calcularFatorial(numero){
    if (numero === 0 || numero === 0){
        return 1; // se numero for 0 ou 1 retorne o valor 1, pois o fatorial de " 0 e 1 = 1"
    }

    let fatorial = 1; // definindo a variavel fetorial para começar com 1 
    for (let i = 2; i <= numero; i++) {
    fatorial *= i; // se a a variavel i for menor que numero, fatorial é multiplicado por i.
}
    return fatorial;
 }

let numero = 5;
let resultado = calcularFatorial(numero);
console.log(`O fatorial de ${numero} é ${resultado}`)



// 3- Crie uma função que converte um valor em dólar, passado como parâmetro, e retorna o valor equivalente em reais. Para isso, considere a cotação do dólar igual a R$4,80.
function converterValorEmReal(valorDolar) {
    let cotação = 4.80;
    let ValorReais = valorDolar * cotação;
    return ValorReais.toFixed(2); // toFixed(2) para ajustar o valor em 2 casas decimais.
}
let valorDolar = 40;
let valorReais = converterValorEmReal(valorDolar);
console.log(`${valorDolar} dólares equivalem a R$ ${valorReais}`);



// 4- Crie uma função que mostre na tela a área e o perímetro de uma sala retangular, utilizando altura e largura que serão dadas como parâmetro.
function mostrarAreaNaTela(altura, largura) {
    let areaDoRetangulo = altura * largura;
    let perimetroDoRetangulo =  2 * (altura + largura);
    
    console.log(`Valor da area ${areaDoRetangulo}`)
    console.log(`Valor do perimetro ${perimetroDoRetangulo}`)
}
// retornando 
let altura = 20;
let largula = 40;
let areaEPerimetro = MostrarAreaNaTela(altura, largura);



// 5- Crie uma função que mostre na tela a área e o perímetro de uma sala circular, utilizando seu raio que será fornecido como parâmetro. Considere Pi = 3,14.
function mostrarPerimetroSala(raio) {
    let areaDoCirculo = Math.PI * raio * raio;
    let perimetroCirculo = 2 * Math.PI * raio;

    console.log(`valor da area é ${areaDoCirculo.toFixed(2)}`);
    console.log(`Valor do perimetro é ${perimetroCirculota.toFixed(2)}`);
}

let raio = 4;
mostrarPerimetroSala(raio);


// 6- Crie uma função que mostre na tela a tabuada de um número dado como parâmetro.
function mostrarTabuadaTela(numero2) {
    for (let i = 0; i <= numero2; i++ ) {
        let resultado = numero * i;
        console.log(`${numero} X ${i} = ${resultado}`);

    }
}

let numero2 = 5;
mostrarTabuadaTela(numero2);