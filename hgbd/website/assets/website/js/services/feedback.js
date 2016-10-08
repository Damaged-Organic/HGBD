"use strict";

export function sendFeedback(url, data){

    return $.ajax({
        url: url,
        type: "POST",
        data: data
    });

}