"use strict";
import { sendFeedback } from "../services/feedback";

const FORM = $("#feedback-form");
const RESPONSE = $("#response-holder");
const BTN = $("#feedback-btn");

class Feedback{

    constructor(){
        this.isLoading = false;
        this.isResponse = false;

        this._events();
    }
    _events(){
        FORM.on("submit", (e) => { this._handleForm(e); })
            .on("click", "#response-holder", (e) => { this.closeResponse(); });
    }
    _handleForm(e){
        e.preventDefault();

        if(!FORM.valid() || this.isLoading) return;

        this.isLoading = true;
        BTN.addClass("loading");

        if(this.isResponse){
            this.closeResponse();
        }

        let formAction = FORM.attr("action"),
            formData = FORM.serializeArray();

        sendFeedback(formAction, formData)
            .done((response) => {
                response = JSON.parse(response);
                
                RESPONSE.html(`<p>${response.message}</p>`)
                        .addClass("active success");

                FORM[0].reset();
            })
            .fail((error) => {
                error = JSON.parse(error.responseText);

                RESPONSE.html(`<p>${error.message}</p>`)
                        .addClass("active error");
            })
            .always(() => {
                this.isLoading = false;
                this.isResponse = true;
                BTN.removeClass("loading");
            });

        return false;
    }
    closeResponse(){
        this.isResponse = false;

        RESPONSE.removeClass("active success error")
                .empty();

        return false;
    }
}

export default Feedback;
