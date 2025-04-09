//Criando uma janelinha para o usuario digitar a idade: 
// var idade = parseInt(prompt('Informe a sua idade: '));

// //Estruturas condicionais:
// if( idade >= 18){
//     console.log('Voce é maior de idade');
// }else{
//     console.log('Voce é menor de idade')
// }

//Estruturas de repetição:
for (var count = 0; count < 2; count++) {
    let peso = parseFloat(prompt('Informe seu peso:'));

    if (peso <= 40) {
        alert('Você é peso pena');
    } else if (peso >= 41 && peso <= 60) {
        alert('Você é peso mosca');
    } else {
        alert('Você é peso pesado');
    }

    console.log("No valor " + count + " foi informado o peso " + peso + " Kg");
}