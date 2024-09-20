alert('Boas vindas ao jogo do número secreto'); // Utilizando o <'alert'> para passar uma mensagem ao usuario.
let numeroSecreto = 5; // Criando uma variavel, com isso estou utilizando o <'let'> e logo após defino o nome da minha variavel
console.log(numeroSecreto); //Exibindo o numero no console.
let chute; // criando uma variavel chute que ira armazenar as respostas do usuario.
let tentativas = 1 // criando variavel de numero de tentativas

// Enquanto chute so usuario não for igual ao numero secreto: 
// <!> = "não for igual" "Diferente"
while (chute != numeroSecreto) {
    chute = prompt('Escolha um número entre 1 e 10'); // Pedindo ao usuário para digitar número de 1 a 30 utilizando o <'prompt'> e vamos definir o valor a variavel chute;
    // Condição: se numeroSecreto for igual ao chute o programa exibira:
    if (chute == numeroSecreto) {  // Utilizando o <If> para comparar e Utilizando os () para declarar o que queremos comparar
        alert(`Isso ai! você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas`); // exibindo resultado com o alert, para juntar uma variavel com uma string vamos usar as <´´> e na frente <${<variavel>}>
    }
    else { // senão mostre isso:
        if (chute > numeroSecreto) { // Se o chute for maior que o numero secret:
            alert(`O número secreto e menor que ${chute}`); // mensagem que ira exibir.
        }
        else {
            alert(`O número secreto e maior que ${chute}`);// mensagem que ira exibir.
        }
        // tebtativas = tantativas + 1;
        tentativas++;
    }
}



