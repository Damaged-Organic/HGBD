var pathJoin = require("path").join;

module.exports = {
    "js": pathJoin(__dirname, "website/js"),
    "css": pathJoin(__dirname, "website/css"),
    "images": pathJoin(__dirname, "website/images"),
    "vendors": pathJoin(__dirname, "website/js/vendors"),
    "build": pathJoin(__dirname, "../static/website")
}
