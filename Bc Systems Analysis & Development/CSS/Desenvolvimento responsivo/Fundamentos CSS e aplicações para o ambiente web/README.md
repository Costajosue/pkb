# **Fundamentos CSS e aplicações para o ambiente web**

# **Definições e conceitos CSS**

Assim como o HTML, o CSS (em inglês *Cascading Style Sheet*), traduzindo “folha de estilo em cascata”, não é uma linguagem de programação e muito menos uma linguagem de marcação, como muitos acham. CSS é uma linguagem de folha de estilo. É usada para formatar o layout das páginas da web, simplificando, o CSS é usado para estilizar elementos HTML seletivamente. Ele pode ser usado para definir estilos de texto, tamanhos de tabela e outros aspectos de páginas da web que anteriormente só podiam ser definidos no HTML de uma página (SILVA, 2019). Por exemplo, o CSS do código da Tabela 1, seleciona o texto do parágrafo, definindo a cor para vermelho:

Tabela 1 | Exemplo de código de aplicação de CSS para selecionar o texto do parágrafo

```css
p {
   color; red;
}

```

Fonte: MDN Web Docs ([s. d.]).

O CSS está entre as principais linguagens da web aberta e é padronizado em navegadores da web de acordo com as especificações do [W3C](https://www.w3.org/Style/CSS/#specs). Anteriormente, o desenvolvimento de várias partes da especificação CSS era realizado de forma síncrona, o que permitia o controle de versão das recomendações mais recentes.

O CSS auxilia os desenvolvedores de website a desenvolverem uma aparência uniforme em várias páginas de um site. Ao invés de definir o estilo de cada tabela e cada bloco de texto no HTML de uma página, os estilos comumente usados precisam ser definidos apenas uma vez em um documento CSS (GILLENWATER, 2010).

Depois que o estilo é definido no CSS, ele pode ser usado por qualquer página que faça referência ao arquivo CSS. Além disso, o CSS facilita a alteração de estilos em várias páginas ao mesmo tempo. Por exemplo, digamos que você, desenvolvedor da web, deseja aumentar o tamanho do texto padrão de 9pt para 10pt para vinte páginas de um site. Se todas as páginas fizerem referência à mesma folha de estilo, o tamanho do texto só precisará ser alterado nela, uma única vez e todas as páginas mostrarão o texto maior.

Embora o CSS seja ótimo para criar estilos de texto, é útil para formatar outros aspectos do layout de página do website também. Por exemplo, o CSS pode ser usado para definir o preenchimento das células da tabela, o estilo, a espessura e a cor da borda de uma tabela e o preenchimento ao redor de imagens ou outros objetos. Assim, o CSS dá aos desenvolvedores da web um controle mais exato sobre a aparência das páginas da web do que o HTML. É por isso que a maioria das páginas da web hoje em dia incorpora o CSS.

Voltando a abordar o exemplo da Tabela 1, vamos entender melhor como funciona o código CSS do texto do parágrafo, vejamos a Figura 1 a seguir.

Figura 1 | Código CSS do texto do parágrafo

!https://conteudo.colaboraread.com.br/202201/WHITE_LABEL/DESENVOLVIMENTO_RESPONSIVO/LIVRO/U1/assets/img/1-1.png

Fonte: adaptada de MDN Web Docs ([s. d.]).

Toda a estrutura chamamos de conjunto de regras ou, como frequentemente nos referimos, apenas **regra**. As demais partes são definidas a seguir:

- **Seletor:** é o nome do elemento HTML no início do conjunto de regras. Ele define o(s) elemento(s) a ser(em) estilizado(s) (no exemplo da Figura 1, `<p>` elementos). Para estilizar um elemento diferente, basta alterar o seletor.
- **Declaração:** esta é uma regra única como `color: red;`. Ela especifica quais propriedades do elemento você pode estilizar.
- **Propriedades:** essas são maneiras de definir o estilo de um elemento HTML, no exemplo da Figura 1, `color` é uma propriedade dos `<p>` elementos, no CSS, você escolhe quais propriedades deseja afetar na regra.
- **Valor da propriedade:** à direita da propriedade – após os dois pontos – está o valor da propriedade. Isso escolhe uma das muitas aparências possíveis para uma determinada propriedade, por exemplo, existem muitos valores de `color` além de `red`).

Observe as demais partes importantes da sintaxe da Figura 1:

Além do seletor, cada conjunto de regras deve ser colocado entre chaves ({}).

Em cada declaração, você deve usar dois-pontos (:) para separar a propriedade de seu valor ou valores.

Em cada conjunto de regras, você deve usar um ponto e vírgula (;) para separar cada declaração da próxima.

O Módulo CSS não é um conceito revolucionário, mas é uma quantidade certa de algo novo, misturado com o antigo. Ele oferece modularização de estilos, incentiva a nomenclatura cuidadosa, nivela estilos, garante a remoção segura de estilos e edição aprimorada (MISKOVIAK, 2018).

### **Vinculando folhas de estilo a documentos**

As folhas de estilo representam um enorme avanço para os designers de páginas da web, por permitirem expandir sua capacidade de melhorar a aparência de suas páginas. Nos ambientes científicos em que a web foi concebida, as pessoas se preocupavam mais com o conteúdo de seus documentos do que com a apresentação (BARON, 2003).

À medida que pessoas de camadas mais amplas descobriram a web, as limitações do HTML tornaram-se uma fonte de contínua frustração e os autores foram forçados a contornar as limitações estilísticas do HTML.

As folhas de estilo resolvem esses problemas ao mesmo tempo que substituem a gama limitada de mecanismos de apresentação em HTML. Elas facilitam a especificação da quantidade de espaço em branco entre as linhas de texto, a quantidade de linhas recuadas, as cores usadas para o texto e os fundos, o tamanho e o estilo da fonte e uma série de outros detalhes.

As folhas de estilo podem ser vinculadas a um documento sob três modos distintos:

**1. Incorporadas:** método de escrever a folha de estilos no documento HTML empregando o elemento `style`. Podemos escrever as regras de estilo dentro das tags `<style></style>`, como demonstrado no código abaixo, na Tabela 2, um exemplo de Silva (2012). Esse método deve ser escolhido quando o uso seja para o caso de aplicação de estilos específicos a apenas um documento do site.

Tabela 2 | Exemplo do método de estilos incorporados de folhas de estilo

```html
<head>
<style type=”text/css” media=”all”>
body {
margin: 0;
padding: 0;
font-size: 80%;
color: black;
background: white;
    }
</style>
</head>

```

Fonte: Silva (2012).

**2. Inline:** método simples e direto de aplicação de estilos em um elemento da marcação, utiliza o atributo `style` do HTML. Podemos escrever as regras de estilo dentro da *tag* de abertura do elemento a estilizar, conforme demonstrado na Tabela 3.

Tabela 3 | Exemplo de código de aplicação de regras de estilo dentro da tag de abertura do elemento

```html
<p style=”width: 200px; color: White; background: red; font-size: 1.8em;”>
<!—Parágrafo com aplicação de estilos inline -->
</p>

```

Fonte: Silva (2012).

**3. Externas:** é o que não foi escrito no documento HTML, sendo um arquivo de texto que contém as regras de estilo e os comentários CSS. Um arquivo de folha de estilo deve ser gravado com a extensão .css e podendo ser vinculado a um documento HTML de duas formas:

- Folhas de estilo lincadas: vinculamos uma folha de estilo externa a um documento empregando o elemento `link`. Ele deverá estar incluído na seção `head` do documento.
- Folhas de estilo importadas: vinculamos uma folha de estilo externa a um documento usando a diretiva `@import` dentro do elemento `style`.

Assim, existem diversas práticas de vinculação do CSS a um arquivo HTML, porém uma das formas eficientes de vincular uma folha de estilo externa a um documento HTML requer um documento separado com uma extensão .css que contém todas as regras CSS sem *tags* HTML.

Esse procedimento altera muitas páginas HTML, editando um arquivo CSS, economizando tempo – desse modo não há necessidade de alterar cada propriedade CSS em cada página HTML do site. Também permite definir uma folha de estilo como um documento separado e importá-la para suas páginas da web.

Quando você usa um estilo externo, os elementos de estilo não são incorporados no cabeçalho da página, mas em um documento totalmente separado. Nesse caso, a página é conectada a um arquivo especial denominado **myStyle.css**. Esse arquivo contém todas as regras CSS, como apresentado na Tabela 4.

Tabela 4 | Modelo de folha de estilo com todas as regras CSS

```css
/ *myStyle.css * /
corpo {
cor defundo: # 333300;
cor: #FFFFFF;
}
h1 {
cor: # FFFF33;
alinhamento detexto: centro;
fonte: itálico 200% fantasia;
}
p {
cor defundo: # FFFF33;
cor: # 333300;
alinhamento detexto: direita;
borda: ranhura de 3px # FFFF33;
}

```

Fonte: Harris (2021).

A folha de estilo se assemelha com um estilo de nível de página, exceto por algumas diferenças importantes citadas por Harris (2014):

- **As regras da folha de estilo estão contidas em um arquivo separado**: ****o estilo não faz mais parte da página HTML, mas é um arquivo totalmente separado, armazenado no servidor. Os arquivos CSS geralmente terminam com a extensão **.css**.
- **Não há *tag***: ****elas não são necessárias porque o estilo não está mais embutido no HTML.
- **O código inicia com um comentário**: o par / * * / indica um comentário em CSS. Você pode colocar comentários em CSS no nível da página, arquivos CSS externos normalmente apresentam comentários.
- **O documento de estilo não possui HTML:** os documentos CSS não contêm nada além de CSS. Isso se aproxima do objetivo de separar *estilo* (no documento CSS) e *conteúdo* (no documento HTML).
- **O documento não está vinculado a nenhuma página específica**: a grande vantagem do CSS externo é a reutilização. O documento CSS não faz parte de nenhuma página em particular, mas qualquer página pode usá-lo.

Alguns conselhos de implementação por Nielsen (1997):

- **As páginas devem continuar a funcionar quando as folhas de estilo estão desativadas**: manter uma apresentação decente sem a folha de estilo é obrigatório para oferecer suporte a usuários com navegadores mais antigos, por exemplo, ou mesmo para usuários que precisam desabilitar o recurso de estilo em seus navegadores (seja por causa de *bugs* ou porque seu estilo conflita muito com suas preferências).
- **Não use mais de duas fontes**: normalmente, você pode usar uma fonte para o corpo do texto e outra, mais ousada, para os títulos. É recomendado usar uma longa lista de fontes alternativas na especificação da folha de estilo para uma determinada classe de texto: o navegador do usuário escolherá a primeira fonte disponível na lista e a usará em todas as suas páginas, o que significa que o usuário verá uma única fonte, fazendo com que o site pareça tipograficamente unificado.
- **Não use tamanhos de fonte absolutos**: especifique todo o texto relativo ao tamanho da fonte de base definido pela configuração de preferência do usuário. Por exemplo, um texto grande pode ser definido como "200%", o que significa que seria definido como 24 pontos se o usuário preferisse 12 pontos para o corpo do texto e 20 pontos se o usuário preferisse 10 pontos para o corpo do texto. É um tanto ruim visitar um site em que o texto é muito pequeno para uma leitura confortável, e é muito ruim clicar no botão "tornar o texto maior" e nada acontecer porque os tamanhos da fonte foram definidos como um número absoluto de pontos.

### **Módulos CSS3 e status dos módulos**

Módulos CSS são um meio de obter nomes de classes CSS com escopo local, ou seja, são uma forma de modularizar estilos em partes menores, em vez de enormes folhas de estilo globais. Para um aplicativo simples de uma página, eles podem não ser necessários, mas se você estiver trabalhando em um aplicativo grande com mais de 20 componentes, essa ferramenta pode realmente ajudar a limpar seu CSS.

Os módulos CSS não têm uma especificação oficial nem são um recurso do navegador. Eles são parte de um processo de compilação executado em seu projeto para converter classes e seletores com escopo em arquivos CSS que o navegador pode analisar e entender. A propósito, um Módulo CSS é apenas um **.css** arquivo. Você o chama de “Módulo CSS” se planeja usá-lo com um compilador de Módulos CSS.

Qualquer arquivo .css válido pode ser um módulo CSS. A diferença é que as definições de estilo nesse arquivo têm como escopo componentes específicos em vez de globalmente. A propriedade `composes` é usada em arquivos de módulo CSS para combinar definições de estilo local. O exemplo a seguir cria um módulo CSS que aplica a definição de estilo `.heading` onde quer que `.titleHighlighted` seja usado, conforme a Tabela 5.

Tabela 5 | Exemplo de criação de um módulo CSS para combinar definições de estilo local

```css
/** ./styles.css */
.heading {
color: yellow;
background-color: blue;
margin: 0 0 1rem;
}

.titleHighlighted {
composes: heading;
padding: 1rem 2rem;
text-align: center;
}

```

Fonte: Adobe Developer (2021).

A sintaxe para importar um módulo CSS, Tabela 6, é a mesma para importar um módulo JavaScript.

Tabela 6 | Exemplo de importação de módulo CSS

```css
ImportmyStylesfrom ‘./styles.css’;
```

Fonte: Adobe Developer (2021).

Os módulos CSS precisam ser canalizados em uma etapa de construção, o que significa que eles não funcionam por si próprios. Veja isso como um *plugin* para webpack **por exemplo. Basicamente, funciona assim: quando você importa um arquivo CSS dentro de um módulo JavaScript (como, mas não necessariamente, um componente [React](https://facebook.github.io/react/) ), os módulos CSS definirão nomes de classe de mapeamento de objeto do arquivo para nomes de classe com escopo/*namespace* que podem ser usados como *strings* em JavaScript.

Como no exemplo da Tabela 7, onde está um arquivo CSS muito simples, a classe `.base` não precisa ser exclusiva no projeto, pois não é o nome real da classe que será renderizado. É apenas uma espécie de apelido dentro da folha de estilo a ser usado no módulo JavaScript.

Tabela 7 | Exemplo de aplicação de módulo CSS

```css
.base {
color: deeppink;
max-width: 42em;
margin: 0 auto;
}

```

Fonte: Giraudel (2015).

E aqui está como você o usaria em um componente JavaScript fictício, conforme descrito na Tabela 8.

Tabela 8 | Exemplo de aplicação do uso em um componente JavaScript fictício

```html
Import styles from ‘./styles.css’;

element.innerHTML = ‘<div class=”${styles.base}”>
CSS Modules are fun.
</div>’

```

Fonte: Giraudel (2015).

Eventualmente, isso irá gerar algo assim (ao usá-lo por meio do webpack com a configuração padrão), Tabela 9.

Tabela 9 | Utilização por meio de webpack com a configuração padrão

```html
<div class=”_20WEds96_Ee1ra54-24ePy”>CSS Modules are fun.</div>

._20WEdf96_Ee1ra54-24ePy {
color: deepink;
max-width: 42em;
margin: 0 auto;
}

```

Fonte: Giraudel (2015).

A maneira como os nomes das classes são gerados, pode ser configurada para torná-los mais curtos ou para seguir um padrão específico. Isso realmente não importa no final (embora nomes de classes mais curtos significam folhas de estilo mais curtas) porque o ponto é que eles são gerados dinamicamente, são únicos e mapeados para os estilos corretos.

Os módulos apresentados na Figura 2 são necessários para começar com os módulos CSS, como dito anteriormente.

Figura 2 | Módulos para CSS

!https://conteudo.colaboraread.com.br/202201/WHITE_LABEL/DESENVOLVIMENTO_RESPONSIVO/LIVRO/U1/assets/img/1-2.png

Fonte: Webpack-demo (2015).

Para fazer os módulos CSS funcionarem com o webpack, você só precisa incluir os módulos mencionados acima e adicionar o seguinte carregador ao seu `webpack.config.jsarquivo`, como na Tabela 10.

Tabela 10 | Exemplo de código para adição do carregador para webpack

```html
...
{
test: /\.css$/,
loader: ‘style!css-loader?modules&importLoaders=1&localIdentName=[name]_[local]_[hash:base64:5]’
}
...

```

Fonte: Webpack-demo (2015).