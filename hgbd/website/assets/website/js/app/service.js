"use strict";

import $ from "jquery";
import Loader from "../utils/loader";
import ScrollTop from "../utils/scrollTop";
import tabs from "../vendors/jquery.tabs";

$(() => {

    $(".tabs-container").tabs();

    new Loader();
    new ScrollTop();
});