let numeroSecreto  = gerarNumeroAleatorio(); // Criando uma variavel que ira receber o número secreto gerado na função na linha 26 e executando ela.
let tentativas = 1 ;
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

function exibirMensagemInicial(){
    exibirTextoNaTela('h1','Jogo do Número secreto'); // executando a função
    exibirTextoNaTela('p', 'Escolha um número entre 1 e 10:'); // executando a função
}

exibirMensagemInicial();

// Criando função para verificar quando o número for criado:
function verificarChute() { // se o usuario acertar 
    let chute = document.querySelector('input').value; // crindo uma variavel que irá selecionar a tag input e o value para pegar so o valor que o usuario for digitar
    if (chute == numeroSecreto) {
        exibirTextoNaTela('h1', 'Acertou!');
        let palavraTentativa = tentativas > 1 ? 'tentativa' : 'tentativas';
        let mensagensTentativas = `você descobriu o número secreto com ${tentativas} ${palavraTentativa}`;
        exibirTextoNaTela('p', mensagensTentativas);
        // Ativando o botão "Novo Jogo" como nosso botão tem um id vamos usar o getElementById para selecionar somente ele pelo id e o removeAttribut para remover o atributo 'disabled' deixando ele ativado.
        document.getElementById('reiniciar').removeAttribute('disabled');
    }
    else { // Se o usuario errar 
        if (chute > numeroSecreto){
            exibirTextoNaTela('p', 'O número secreto é menor');
        }
        else {
            exibirTextoNaTela('p', 'O número secreto é maior');
        }
        tentativas++; // Soma das tentativas 
        limparCampo() // executando a função
    }
}

// Criando função que ira gerar um número aleatorio.
function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 10 + 1); // Utilizando o return para assim que executarmos o fanção ele ira retornar o resultado.
}

// Criando função para limpar o campo onde o usuário digita seu chute
function limparCampo() {
    chute = document.querySelector('input');
    chute.value = ''
}
// Criando funcão para reiniciar o jogo.
function reiniciarJogo() {
    numeroSecreto = gerarNumeroAleatorio();
    limparCampo();
    tentativas = 1 ;
    exibirMensagemInicial();
    document.getElementById('reiniciar').setAttribute('disabled', true);
}