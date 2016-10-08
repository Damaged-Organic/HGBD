"use strict";

import $ from "jquery";
import Loader from "../utils/loader";
import ScrollTop from "../utils/scrollTop";

$(() => {
    new Loader();
    new ScrollTop();
});

