function pesquisar() {
    // Obtém a seção HTML onde os resultados serão exibidos
    let section = document.getElementById("resultados-pesquisa");

    let campoPesquisa = document.getElementById("campo-pesquisa").value

    //Se o usuario não digitar nada no campo de pesquisa:
    if (campoPesquisa == "") {
        section.innerHTML = "<p>Ops... não encontramos nenhum jogo<p/>"
        return // utilizando o return para quebrar o codigo caso o usuario não digite nada em pesquisar 
        
    }
    
    campoPesquisa = campoPesquisa.toLowerCase()
    
    // Inicializa uma string vazia para armazenar os resultados
    let resultados = "";
    let titulo = "";
    let descrição = "";

    // Itera sobre cada dado da lista de dados
    for (let dado of dados) {
        titulo = dado.titulo.toLocaleLowerCase()
        descrição = dado.descrição.toLocaleLowerCase()
        if (titulo.includes(campoPesquisa) || descrição.includes(campoPesquisa)){
            // Cria um novo elemento HTML para cada resultado
            resultados += `
            <div class="item-resultado">
                <h2>
                    <a href="#" target="_blank">${dado.titulo}</a>
                </h2>
                <p class="descricao-meta">${dado.descrição}</p>
                <a href=${dado.link} target="_blank">Mais informações</a>
            </div>
        `;
        }

    }
    if(!resultados){
        resultados = "<p>Ops... não encontramos nenhum jogo<p/>"
    }

    // Atribui os resultados gerados à seção HTML
    section.innerHTML = resultados;
}