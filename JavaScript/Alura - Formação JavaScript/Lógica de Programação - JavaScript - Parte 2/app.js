let numeroSecreto  = gerarNumeroAleatorio(); // Criando uma variavel que ira receber o número secreto gerado na função na linha 26 e executando ela.

// Manipulando texto "<h1></h1>":
// let titulo = document.querySelector('h1'); // Criando uma variavel "titulo" e utilizando o document.querySelector('h1') para selecionar e alterar texto no HTML.
// titulo.innerHTML = 'Jogo do Número secreto';  // inserir um texto 

// Manipulando texto "<p></p>":
// let paragrafo = document.querySelector('p'); // Criando uma variavel "paragrafo" e utilizando o document.querySelector('p') para selecionar e alterar texto no HTML.
// paragrafo.innerHTML = 'Escolha um número entre 1 e 10:'; // inserir um texto 

// Criando uma função que irá manipular os textos "h1" e "p" aplicando as boas praticas e assim resulmindo os codigos que estão acima:
function exibirTextoNaTela(tag, texto){
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

exibirTextoNaTela('h1','Jogo do Número secreto'); // executando a função
exibirTextoNaTela('p', 'Escolha um número entre 1 e 10:'); // executando a função

// Criando função para verificar quando o número for criado:
function verificarChute() {
    let chute = document.querySelector('input').value; // crindo uma variavel que irá selecionar a tag input e o value para pegar so o valor que o usuario for digitar
    console.log(chute == numeroSecreto); // conparar o valor 
}

// Criando função que ira gerar um número aleatorio.
function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 10 + 1); // Utilizando o return para assim que executarmos o fanção ele ira retornar o resultado.
}