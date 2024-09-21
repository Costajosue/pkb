alert('Boas vindas ao jogo do número secreto'); // Utilizando o <'alert'> para passar uma mensagem ao usuario.
let numeroEscolhido = prompt('Até que número voce deseja se desafiar a acertar! ')
let numeroSecreto = parseInt(Math.random() * numeroEscolhido + 1); // Criando uma variavel, com isso estou utilizando o <'let'> e logo após defino o nome da minha variavel. Utilizo tambem a funão <Mart.random> que vai gerar numeros aleatorios / usando o <parentInt> para pegar somente o numero inteiro, pois quando geramos um numero no range ele pode vir como numero inteiro ou não;
console.log(numeroSecreto); //Exibindo o numero no console.
let chute; // criando uma variavel chute que ira armazenar as respostas do usuario.
let tentativas = 1 // criando variavel de numero de tentativas

// Enquanto chute so usuario não for igual ao numero secreto: 
// <!> = "não for igual" "Diferente"
while (chute != numeroSecreto) {

    chute = prompt(`Escolha um número entre 1 e ${numeroEscolhido}`); // Pedindo ao usuário para digitar número de 1 a 30 utilizando o <'prompt'> e vamos definir o valor a variavel chute;
    // Condição: se numeroSecreto for igual ao chute o programa exibira:
    if (chute == numeroSecreto) {  // Utilizando o <If> para comparar e Utilizando os () para declarar o que queremos comparar
        // Parar codigo
        break
    }
    else { // senão mostre isso:
        if (chute > numeroSecreto) { // Se o chute for maior que o numero secret:
            alert(`O número secreto e menor que ${chute}`); // mensagem que ira exibir.
        }
        else {
            alert(`O número secreto e maior que ${chute}`);// mensagem que ira exibir.
        }
        // tentativas = tantativas + 1;
        tentativas++;
    }
}
let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Isso ai! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);

                              //PODEMOS UTILIZAR A FORMA ABAIXO:
// if(tentativas > 1){
//     alert(`Isso ai! você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas `); // exibindo resultado com o alert, para juntar uma variavel com uma string vamos usar as <´´> e na frente <${<variavel>}>
// }
// else{
//     alert(`Isso ai! você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativa `); // exibindo resultado com o alert, para juntar uma variavel com uma string vamos usar as <´´> e na frente <${<variavel>}>
// }


