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

// Bootstrap
var bootstrap_css_path = './node_modules/bootstrap/dist/css';
var bootstrap_js_path = './node_modules/bootstrap/dist/js';

// Font-Awesome
var fa_css_path = './node_modules/font-awesome/css';
var fa_fonts_path = './node_modules/font-awesome/fonts';

// jQuery
var jquery_path = './node_modules/jquery/dist';

// ViperTbot
var css_root_path = './project/static/vipertbot/css';
var js_root_path = './project/static/vipertbot/js';

// Smartadmin
var smart_css_path = './project/static/vipertbot/css/smartadmin';
var smart_js_path = './project/static/vipertbot/js/smartadmin';
var smart_js_plugin_path = './project/static/vipertbot/css/smartadmin/plugin';

// VueJS
var vue_components_path = './project/static/vipertbot/js/components';

// Compiled paths (destinations)
var css_compiled_path = './project/static/compiled/css';
var js_compiled_path = './project/static/compiled/js';
var fonts_compiled_path = './project/static/compiled/fonts';

gulp.task('vendorCSS', function() {
    return gulp.src([
        bootstrap_css_path + '/bootstrap.min.css',
        fa_css_path + '/font-awesome.min.css',
        smart_css_path + '/smartadmin-production-plugins.min.css',
        smart_css_path + '/smartadmin-production.min.css',
        smart_css_path + '/smartadmin-skins.min.css',
        smart_css_path + '/smartadmin-rtl.min.css'
    ])
        .pipe(concat('vendor.css'))
        .pipe(gulp.dest(css_compiled_path))
});

gulp.task('vendorJS', function() {
    return gulp.src([
            jquery_path + '/jquery.min.js',
            bootstrap_js_path + '/bootstrap.min.js',
            smart_js_path + '/app.min.js',
            smart_js_path + '/SmartNotification.min.js',
            smart_js_path + '/jarvis.widget.min.js',
            smart_js_path + '/voicecommand.min.js',
            smart_js_path + '/smart.chat.ui.min.js',
            smart_js_path + '/smart.chat.manager.min.js'
        ])
        .pipe(concat('vendor.js'))
        .pipe(gulp.dest(js_compiled_path));

});

gulp.task('styles', function() {
    return gulp.src([
        css_root_path + '/*.css'
    ])
        .pipe(concat('main.css'))
        .pipe(cleanCSS())
        .pipe(gulp.dest(css_compiled_path))
});

gulp.task('browserify', function() {
    return browserify(js_compiled_path + '/main.js')
        .transform(vueify)
        .bundle()
        .pipe(fs.createWriteStream(js_compiled_path + '/main.js'));
});

gulp.task('fa_fonts', function() {
    return gulp.src([
           fa_fonts_path + '/**/*.{eot,otf,ttf,woff,woff2,eof,svg}'
        ])
        .pipe(gulp.dest(fonts_compiled_path))
});

gulp.task('watch', function() {
    gulp.watch([
        css_root_path + '/*.css'
    ], ['styles']);

    gulp.watch([
        js_root_path + '/main.js',
        vue_components_path + '/*.vue'
    ], ['browserify']);
});

gulp.task('watchify', function() {
    var b = browserify({
      entries: [js_root_path + '/main.js'],
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
          .pipe(fs.createWriteStream(js_compiled_path + '/main.js'));
    }
});

gulp.task('default', ['styles', 'browserify', 'fa_fonts', 'vendorCSS', 'vendorJS']);