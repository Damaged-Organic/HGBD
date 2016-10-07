"use strict";

import "jquery";
import "jquery-validation";

import { isMobile } from "../utils/detectMobileDevice";
import Loader from "../utils/loader";
import Feedback from "../components/feedback";
import Map from "../components/map";

$(() => {
    new Loader();
    new Feedback();

    if(!isMobile()){
        new Map();
    }
    
    $("form").validate();
});