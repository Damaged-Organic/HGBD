"use strict";

import Cookies from "../utils/cookies";

let token = Cookies.get("csrftoken");

export function sendFeedback(url, data){

    return $.ajax({
        url: url,
        type: "POST",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": token
        },
        data: data
    });

}
