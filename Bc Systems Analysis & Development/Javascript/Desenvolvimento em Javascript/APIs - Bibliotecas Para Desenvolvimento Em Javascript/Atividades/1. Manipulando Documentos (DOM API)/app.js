// Criando uma variavel onde armazene o botao e a mansagem.
let botao = document.getElementById("botao");
let mensagem = document.getElementById("mensagem");

// Adicionando a função ao botão.
botao.onclick = function() { 
    mensagem.innerText = "MENSAGEM ALTERADA";
    mensagem.style.fontSize = "30px"; // Aqui é onde o texto fica grande
    mensagem.style.backgroundColor = "Blue"; // Deixando o fundo azul ao clicar 
    mensagem.style.color = "white";  // Fonte branca 
}