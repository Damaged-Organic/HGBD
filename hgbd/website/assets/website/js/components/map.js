"use strict";

import GoogleMapsLoader from "google-maps";

GoogleMapsLoader.KEY = "AIzaSyDWQ8KabiEnj1NhMT93d-LqytUlFZYIZxk";

const MAP_NODE = $("#map")[0];

class Map{

    constructor(mapLoader = GoogleMapsLoader){
        this.map = {};
        this.marker = {};

        mapLoader.load(google => this.createMap(google));
    }
    createMap(google){
        this.map = new google.maps.Map(MAP_NODE, {
            center: { lat: 50.441149, lng: 30.522921 },
            zoom: 14,
            maxZoom: 17,
            minZoom: 4,
            mapTypeControl: false,
            streetViewControl: false,
            scrollwheel: false
        });

        this.createMarker();
    }
    createMarker(){
        this.marker = new google.maps.Marker({
            position: { lat: 50.441149, lng: 30.522921 },
            map: this.map,
            icon: {
                url: "static/website/images/marker.png",
                size: {
                    width: 24,
                    height: 24
                }
            }
        });
    }
}

export default Map;
