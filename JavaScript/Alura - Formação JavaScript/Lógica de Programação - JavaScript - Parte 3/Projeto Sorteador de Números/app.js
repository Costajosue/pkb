// Criando uma função sortear que será para o botão / armazenando as info. quantidade, de e ate em uma variavel.
function sortear(){
    let quantidade = parseInt(document.getElementById('quantidade').value); // O value para pegar so o valor e o parseInt para retornar só numero inteiro
    let de = parseInt(document.getElementById('de').value);
    let ate = parseInt(document.getElementById('ate').value);



}  
// Criando uma função para obter um numero aleatorio 
function obterNumeroAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min; // função para gerar numero aleatorio;

}