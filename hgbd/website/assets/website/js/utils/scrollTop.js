const scrollBtn = $("#scroll-top-btn"); 

class ScrollTop{

    constructor(){
        this._events();
    }
    _events(){
        scrollBtn.on("click", (e) => { this.handleScroll(e) });
    }
    handleScroll(e){
        $("body, html").stop().animate({"scrollTop": 0}, 1000);
        return false;
    }
}

export default ScrollTop;