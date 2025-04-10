# Instruções das atividades:

### Atividade 1 = Manipulando Documentos (DOM API):

Crie um código JavaScript que interaja com um documento HTML e altere
dinamicamente seu conteúdo ao clicar em um botão.
- Exibir um botão na página com o texto "Mudar mensagem";
- Ao clicar no botão, alterar o conteúdo de uma "div" para exibir uma mensagem
personalizada;
- Modificar a cor de fundo da "div" para azul.

Instruções:
1. Crie um arquivo index.html e adicione uma "div" e um "button" no corpo do
documento.
2. No "script", utilize "document.getElementById()" e "addEventListener()" para
modificar o conteúdo e a cor da "div" ao clicar no botão.


### Atividade 2 = Trabalhando com Áudio e Gráficos (Canvas API & Audio API):

Crie um código que utilize o "canvas" para desenhar uma figura simples e reproduza um
som ao clicar na tela.
- Criar um elemento "canvas" e desenhar um círculo vermelho nele;
- Adicionar um evento de clique para tocar um som curto ao interagir com o
"canvas".

Instruções:
1. No index.html, adicione um elemento "canvas" e um "audio" com um arquivo
de som.
2. No "script", utilize "getContext("2d")" para desenhar o círculo e
"addEventListener("click", function() {...})" para tocar o som.

### Atividade 3 = Comunicando com o Servidor (Fetch API):

Desenvolva um script que consuma dados de uma API pública e exiba informações
dinamicamente na página.
- Fazer uma requisição para a API pública JSONPlaceholder;
- Exibir os títulos dos cinco primeiros posts em uma lista HTML "ul".

Instruções:
1. No "index.html", crie uma "ul" vazia onde os títulos serão exibidos.
2. No "script", utilize "fetch()" para obter dados da API
https://jsonplaceholder.typicode.com/posts.
3. Após a resposta da API, use "response.json()" para converter os dados e atualizar
a "ul".
