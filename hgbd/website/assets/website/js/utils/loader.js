const LOAD_TIME = 2000;

let loaderHolder = $("#loader-holder"),
    body = $("body");

class Loader{

    constructor(){
        (document.readyState === "complete") ? this._handleLoad() : this._events();
    }
    _events(){
        $(window).on("load", (e) => { this._handleLoad() });
    }
    _handleLoad(){
        setTimeout(() => {

            loaderHolder.addClass("loaded");
            body.addClass("loaded");

        }, LOAD_TIME);

        return false;
    }
}

export default Loader;