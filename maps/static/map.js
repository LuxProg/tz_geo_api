//import { fromLonLat } from "./ol/proj";



var point = [43.7961415653353, 43.5416839064579];

var point1 = [4379614.15653353, 4354168.39064579];

window.onload = init;

//var point2 = fromLonLat(point); тут траблы
//console.log(point2);

function init(){
    const map = new ol.Map({
        view: new ol.View({
            center: [0,0],
            zoom: 3,
            maxZoom: 10
        }),
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        target: 'js-map'
    })

    map.on('click', function(e){
        console.log(e.coordinate);
    })
}

//const tileLayer = new ol.layer.Tile({source: new ol.source.OSM()});


//document.addEventListener('DOMContentLoaded', init);

//init;

//const map = new ol.Map('js-map')

//var layer = new ol.layer.OSM('OSM mapa')

//map.addLayer(layer);

//map.zoomToMaxExtent();