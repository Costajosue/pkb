// 1- Altere o conteúdo da tag h1 com document.querySelector e atribua o seguinte texto: Hora do Desafio.
let texto = document.querySelector('h1');
texto.innerHTML = ('Hora do Desafio');


// 2- Crie uma função que exiba no console a mensagem O botão foi clicado sempre que o botão Console for pressionado.
function exibaConsole() {
    console.log('O botão foi clicado');
}
// no HTML 
<button onclick="exibirMensagemNoConsole()" class="button">Console</button>


// 3- Crie uma função que exiba um alerta com a mensagem: Eu amo JS, sempre que o botão Alerta for pressionado.
function exibaAlert() {
    alert('Eu amo JS');
}
// HTML
<button onclick="exibaAlert()" class="button">alert</button>


// 4- Crie uma função que é executada quando o botão prompt é clicado, perguntando o nome de uma cidade do Brasil. Em seguida, exiba um alerta com a mensagem concatenando a resposta com o texto: Estive em {cidade} e lembrei de você.
function verificarPrompt(){
    let cidade = prompt('Nome de uma cidade do Brasil:');
    alert(`Estive em ${cidade} e lembrei de você`);
}
// HTML
<button onclick="verificarPrompt()" class="button">prompt</button>


// 5- Ao clicar no botão soma, peça 2 números inteiros e exiba o resultado da soma em um alerta.
function soma2Numeros() {
    let numero1 = prompt('Digite o primeiro número:');
    let numero2 = prompt('Digite o segundo número:');
    let soma = numero1 + numero2;
    alert(`${numero1} + ${numero2} = ${soma}`)
}
// HTML
<button onclick="verificarPrompt()" class="button">soma</button>