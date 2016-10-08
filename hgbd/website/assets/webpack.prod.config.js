var webpack = require("webpack"),
    cfg = require("./config"),
    path = require("path"),

    CopyWebpackPlugin = require("copy-webpack-plugin"),

    node_path = path.join(__dirname, "node_modules");

module.exports = {
    entry: {
        home: "./website/js/app/home.js",
        service: "./website/js/app/service.js",
        contacts: "./website/js/app/contacts.js"
    },
    output: {
        path: path.join(__dirname, "../static/website/js"),
        publicPath: "../static/website/js",
        filename: "[name].bundle.min.js"
    },
    resolve: {
        alias: {
            "jquery": cfg.vendors + "/jquery.min",
            "jquery-validation": cfg.vendors + "/jquery.validate",
            "google-maps": cfg.vendors + "/Google.min.js"
        },
        extensions: ["", ".js", ".es6"]
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            }
        ]
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env': {
                'NODE_ENV': JSON.stringify(process.env.NODE_ENV)
            }
        }),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            }
        }),
        new CopyWebpackPlugin([
            { from: node_path + "/jquery/dist/jquery.min.js", to: cfg.vendors },
            { from: node_path + "/jquery-validation/dist/jquery.validate.js", to: cfg.vendors },
            { from: node_path + "/google-maps/lib/Google.min.js", to: cfg.vendors }
        ])
    ],
    cache: false
}
