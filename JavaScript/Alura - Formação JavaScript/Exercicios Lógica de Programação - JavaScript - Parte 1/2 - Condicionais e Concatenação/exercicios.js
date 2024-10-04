// EXERCICOS: ESTRUTURAS CONDICIONAIS E CONCATENAÇÃO
//___________________________________________________________________________________________________________________________________

// 1- Pergunte ao usuário qual é o dia da semana. Se a resposta for "Sábado" ou "Domingo", mostre "Bom fim de semana!". Caso contrário, mostre "Boa semana!".
let diaSemana = prompt('Qual o dia da semana?');
if(diaSemana == 'sabado'){
    alert('Bom fim de semana!');
}
else if (diaSemana == 'Domingo'){
    alert('Bom fim de semana!');
}
else{
    alert('Boa semana!');
}

// 2- Verifique se um número digitado pelo usuário é positivo ou negativo. Mostre um alerta informando.
let numero = prompt('Digite um numero');
if(numero > 0){
    alert('numero positivo!');
}
else{
    alert('O numero e negativo');
}

// 3- Crie um sistema de pontuação para um jogo. Se a pontuação for maior ou igual a 100, mostre "Parabéns, você venceu!". Caso contrário, mostre no console "Tente novamente para ganhar.".
let pontos = prompt('digite sua pontuação;');
if (pontos => 100){
    console.log('Parabens!');
} 
else{
    console.log('Tente novamente para ganhar');
}

// 4- Crie uma mensagem que informa o usuário sobre o saldo da conta, usando uma template string para incluir o valor do saldo.
let saldoConta = 400;
alert(`Seu saldo é de ${saldoConta}`);

// 5- Peça ao usuário para inserir seu nome usando prompt. Em seguida, mostre um alerta de boas-vindas usando esse nome.
let nomeUsuario = prompt('Digite seu nome:');
alert(`Boas-Vindas ${nomeUsuario}`);