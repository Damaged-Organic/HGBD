(($, window, document) => {

    const PLUGIN_NAME = "tabs";

    class Tab{

        constructor(el, options){
            this.el = $(el);
            this.labels = this.el.find(".tab-label");
            this.contents = this.el.find(".tab-content");

            this._events();
        }
        _events(){
            this.labels.on("click", (e) => { this._handleClick(e) });
        }
        _handleClick(e){
            let label = $(e.currentTarget),
                index = label.index();

            this.labels.removeClass("active").eq(index).addClass("active");
            this.contents.removeClass("active").eq(index).addClass("active");

            return false;
        }

    }

    $.fn[PLUGIN_NAME] = function(options){
        return this.each((index, el) => new Tab(el, options));
    }

})($, window, document);