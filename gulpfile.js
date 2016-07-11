var gulp = require('gulp');
var fs = require('fs');
var browserify = require('browserify');
var concat = require('gulp-concat');
var vueify = require('vueify');
var cleanCSS = require('gulp-clean-css');
var merge = require('merge-stream');
var watchify = require('watchify');
var gutil = require('gulp-util');
var source = require('vinyl-source-stream');
var assign = require('lodash.assign');

gulp.task('vendorCSS', function() {
    return gulp.src([
        './node_modules/bootstrap/dist/css/bootstrap.min.css',
        './node_modules/font-awesome/css/font-awesome.min.css'
    ])
        .pipe(concat('vendor.css'))
        .pipe(gulp.dest('./project/static/compiled/css'))
});

gulp.task('vendorJS', function() {
    return gulp.src([
            './node_modules/jquery/dist/jquery.min.js',
            './node_modules/bootstrap/dist/js/bootstrap.min.js'
        ])
        .pipe(concat('vendor.js'))
        .pipe(gulp.dest('./project/static/compiled/js'));

});

gulp.task('styles', function() {
    return gulp.src([
        './project/static/vipertbot/css/*.css'
    ])
        .pipe(concat('main.css'))
        .pipe(cleanCSS())
        .pipe(gulp.dest('./project/static/compiled/css'))
});

gulp.task('browserify', function() {
    return browserify('./project/static/vipertbot/js/main.js')
        .transform(vueify)
        .bundle()
        .pipe(fs.createWriteStream('./project/static/compiled/js/main.js'));
});

gulp.task('fa_fonts', function() {
    return gulp.src([
            './node_modules/font-awesome/fonts/**/*.{eot,otf,ttf,woff,woff2,eof,svg}'
        ])
        .pipe(gulp.dest('./project/static/compiled/fonts'))
});

gulp.task('watch', function() {
    gulp.watch([
        './project/static/vipertbot/css/*.css'
    ], ['styles']);

    gulp.watch([
        './project/static/vipertbot/js/main.js',
        './project/static/vipertbot/js/components/*.vue'
    ], ['browserify']);
});

gulp.task('watchify', function() {
    var b = browserify({
      entries: ['./project/static/vipertbot/js/main.js'],
      cache: {},
      packageCache: {},
      plugin: [watchify]
    });
    b.transform(vueify);

    b.on('update', bundle);
    b.on('log', gutil.log);
    bundle();

    function bundle() {
      b.bundle()
          .on('error', gutil.log.bind(gutil, 'Browserify Error'))
          .pipe(fs.createWriteStream('./project/static/compiled/js/main.js'));
    }
});

gulp.task('default', ['styles', 'browserify', 'fa_fonts', 'vendorCSS', 'vendorJS']);