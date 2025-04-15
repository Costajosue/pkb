// Solicita a posição atual do usuário
navigator.geolocation.getCurrentPosition(position => {

    // Coleta latitude e longitude da posição obtida
    const { latitude, longitude } = position.coords;

    // Criando e exibindo o mapa com a biblioteca OpenLayers
    var map = new ol.Map({
        // Define o elemento HTML onde o mapa será renderizado
        target: 'mapa',  // Certifique-se de ter um <div id="mapa"></div> no HTML

        // Define as camadas do mapa
        layers: [
            new ol.layer.Tile({
                // Fonte do mapa: OpenStreetMap (OSM)
                source: new ol.source.OSM()
            })
        ],

        // Define a visualização inicial do mapa
        view: new ol.View({
            // Centraliza o mapa nas coordenadas do usuário
            center: ol.proj.fromLonLat([longitude, latitude]),

            // Nível de zoom (quanto maior o número, mais aproximado)
            zoom: 10  // aumente este número para maior aproximação
        })
    });

});