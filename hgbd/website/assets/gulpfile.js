var gulp = require("gulp"),
    cfg = require("./config"),

    exec = require("child_process").exec,
    rdSync = require("fs").readdirSync,
    extname = require("path").extname,

    imagemin = require("gulp-imagemin"),
    pngquant = require("imagemin-pngquant");

gulp.task("css", () => {

    var fileList = rdSync(cfg.css),
        fileName = "";

    fileList.map((file) => {
        if(extname(file) !== ".less") return;

        fileName = /\w+(?=\.less$)/gi.exec(file)[0];
        exec('lessc --clean-css '+ cfg.css +'/'+ file + ' --autoprefix="last 2 versions" '+ cfg.build +'/css/'+ fileName +'.bundle.min.css');
    });
});

gulp.task("images", () => {

    gulp.src(cfg.images +"/**/*.*")
        .pipe(imagemin([
            pngquant()
        ]))
        .pipe(gulp.dest(cfg.build +"/images/"));

});

gulp.task("inlines", () => {

    gulp.src(cfg.js + "/inlines/*.js")
        .pipe(gulp.dest(cfg.build + "/inlines/"));
})

gulp.task("watcher", () => {
    gulp.watch(cfg.css +"/**/*.less", ["css"]);
    gulp.watch(cfg.images +"/**/*.*", ["images"]);
});

gulp.task("default", ["css", "images", "inlines"]);
