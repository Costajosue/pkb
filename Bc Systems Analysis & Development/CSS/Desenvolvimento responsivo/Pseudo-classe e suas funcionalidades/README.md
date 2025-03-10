AGRUPAMENTOS

O agrupamento em CSS é uma técnica usada para reduzir a redundância de código e escrever um código limpo, conciso e fácil de seguir (SILVA, 2019). Haverá muitas confusões quando vários seletores CSS tiverem as mesmas declarações. Nesses casos, você pode agrupar todos os seletores e escrever as declarações apenas uma vez. Por exemplo, se você deseja aplicar exatamente o mesmo tamanho de fonte e cor a três títulos diferentes, você pode escrever como mostrado na Tabela 8, no entanto, verá que isso é um desperdício de espaço.

h1 {
    font-size: 10px;
    color: green;
    font-size: 30px;
    }
     
h2 {
    font-size: 10px;
    color: green;
    font-size: 30px;
    }
     
h3 {
    font-size: 10px;
    color: green;
    font-size: 30px;
    } */

Ao agrupar seletores CSS, você aplica os mesmos estilos a vários elementos diferentes sem repetir os estilos em sua folha de estilo. Em vez de ter duas, três ou mais regras CSS que fazem a mesma coisa (definir a cor de algo como vermelho, por exemplo), você usa uma única regra CSS que realiza a mesma coisa. O segredo dessa tática de aumento de eficiência é a vírgula.  
 
 Como você pode ver, podemos direcionar os elementos h1, h2 e h3 com uma única regra, em vez de ter que especificá-la para cada um deles. Você também pode misturar e combinar os seletores de classe e ID, se quiser, como exemplificado.


h1#main, h2.sub, h3, .someClass, #anID {
    color: Maroon;
    } 

Graças ao CSS e sua natureza em cascata, você ainda pode adicionar regras específicas para um ou vários elementos e o navegador as aplicará de acordo com a precedência. Vejamos este exemplo */

h1, h2, h3{
color: Maroon;
text-align: center;
}
h1{
background-color: Silver;
padding:10px;
text-align: left;
}
h2,h3 {
background-color: Gray;
padding: 5px;
} 
Ao agrupar seletores CSS, você aplica os mesmos estilos a vários elementos diferentes sem repetir os estilos em sua folha de estilo. Em vez de ter duas, três ou mais regras CSS que fazem a mesma coisa (definir a cor de algo como vermelho, por exemplo), você usa uma única regra CSS que realiza a mesma coisa. O segredo dessa tática de aumento de eficiência é a vírgula. 
Esse é mais um dos recursos do CSS que permite uma maior reutilização do código – não há razão para especificar as mesmas propriedades para vários elementos/classes se você puder reutilizá-los, não é mesmo?
Como você pode ver, podemos direcionar os elementos h1, h2 e h3 com uma única regra, em vez de ter que especificá-la para cada um deles. Você também pode misturar e combinar os seletores de classe e ID, se quiser, como exemplificado na Tabela 9.

Tabela 9 | Exemplo de combinação de seletores de classe e ID

h1#main, h2.sub, h3, .someClass, #anID {
color: Maroon;
}
Fonte: CSS3-tutorial ([s. d.]).

Agora, o que é realmente legal é que, graças ao CSS e sua natureza em cascata, você ainda pode adicionar regras específicas para um ou vários elementos e o navegador as aplicará de acordo com a precedência. Vejamos este exemplo da Tabela 10.

Tabela 10 | Exemplo de agrupamento com regras específicas para diferentes elementos

<style type=”text/css”>
h1, h2, h3{
color: Maroon;
text-align: center;
}
h1{
background-color: Silver;
padding:10px;
text-align: left;
}
h2,h3 {
background-color: Gray;
padding: 5px;
)
</style>
<h1>Main header</h1>
<h2>Header level 2</h2>
<h3>Header level 3</h3>
}
Fonte: CSS3-tutorial ([s. d.]).

Aplique esse exemplo e veja como o navegador usa as propriedades apropriadas dos seletores. Podemos agrupar as propriedades comuns em um seletor e, em seguida, podemos adicioná-las e até mesmo modificá-las nos seletores mais específicos posteriormente.
Concluímos que o agrupamento de seletores torna muito fácil reutilizar o código CSS enquanto mantém um alto grau de flexibilidade – se uma regra comum for usada em vários lugares, você ainda pode anulá-la escrevendo um seletor mais específico.