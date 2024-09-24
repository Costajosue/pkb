
// Fazer exercicios:
// https://cursos.alura.com.br/course/logica-programacao-mergulhe-programacao-javascript/task/137091

// Respostas:
// https://github.com/alura-cursos/logica-js/tree/desafios

// 1- Crie um programa que utilize o console.log para exibir uma mensagem de boas-vindas:
console.log('Boas-vindas');

// 2- Crie uma variável chamada "nome" e atribua a ela o seu nome. Em seguida, utilize o console.log para exibir a mensagem "Olá, [seu nome]!" no console do navegador.
let nome = Josué;
console.log(`Olá, ${nome}!`);

// 3- Crie uma variável chamada "nome" e atribua a ela o seu nome. Em seguida, utilize o alert para exibir a mensagem "Olá, [seu nome]!" .
let nome2 = Josué;
alert(`Olá, ${nome2}!`);

// 4- Utilize o prompt e faça a seguinte pergunta: Qual a linguagem de programação que você mais gosta?. Em seguida, armazene a resposta em uma variável e mostre no console do navegador.
let pergunta = prompt('Qual a linguagem de programação que você mais gosta?');
console.log(pergunta);

// 5- Crie uma variável chamada "valor1" e outra chamada "valor2", atribuindo a elas valores numéricos de sua escolha. Em seguida, realize a soma desses dois valores e armazene o resultado em uma terceira variável chamada "resultado". Utilize o console.log para mostrar a mensagem "A soma de [valor1] e [valor2] é igual a [resultado]." no console.
let valor1 = 1;
let valor2 = 3;
let resultadoSoma = valor1 + valor2;
console.log(`A soma de ${valor1} e ${valor2} é igual a ${resultadoSoma}.`)

// 6- Crie uma variável chamada "valor1" e outra chamada "valor2", atribuindo a elas valores numéricos de sua escolha. Em seguida, realize a subtração desses dois valores e armazene o resultado em uma terceira variável chamada "resultado". Utilize o console.log para mostrar a mensagem "A diferença entre [valor1] e [valor2] é igual a [resultado]." no console.
let valores1 = 5;
let valores2 = 3;
let resultadoSoma2 = valores1 - valores2;
console.log(`A diferença entre ${valores1} e ${valores2} é igual a ${resultadoSoma2}.`)

// 7- Peça ao usuário para inserir sua idade com prompt. Com base na idade inserida, utilize um if para verificar se a pessoa é maior ou menor de idade, exibindo uma mensagem apropriada no console.
let idade = prompt('Insira sua idade: ');
if (idade >= 18 ){
    console.log('Voce é maior de idade');
}
else {
    console.log('Voce e menor de idade');
}

// 8- Crie uma variável "numero" e peça um valor com prompt verifique se é positivo, negativo ou zero. Use if-else para imprimir a respectiva mensagem.
let numero = prompt('Digite um valor: ');

if (numero > 0){
    console.log('Esse numero é positivo!')
}
else if (numero < 0){
    alert('Esse numero é negativo!')}
else{
    alert('o numero é zero')
}

// 9- Use um loop while para imprimir os números de 1 a 10 no console.
contador = 1;
while(contador <= 10){
    console.log(contador);
    contador++;
}

// 10-Crie uma variável "nota" e atribua um valor numérico a ela. Use if-else para determinar se a nota é maior ou igual a 7 e exiba "Aprovado" ou "Reprovado" no console.
let nota = 9;
if(nota >= 7){
    console.log('APROVADO')
}
else{
    console.log('REPROVADO')
}

// 11- Use o Math.random para gerar qualquer número aleatório e exiba esse número no console.
let numeros = math.random();
console.log(numeros);

// 12-Use o Math.random para gerar um número inteiro entre 1 e 10 e exiba esse número no console.
let numeros3 = parseInt(math.random() * 10 + 1);
console.log(numeros);

// 13- Use o Math.random para gerar um número inteiro entre 1 e 1000 e exiba esse número no console.
// 12-Use o Math.random para gerar um número inteiro entre 1 e 10 e exiba esse número no console.
let numeros4 = parseInt(math.random() * 1000 + 1);
console.log(numeros);
