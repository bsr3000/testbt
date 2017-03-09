var autoprefixer = require('autoprefixer');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var path = require('path');
var webpack = require('webpack');
var resolve = path.resolve.bind(path, __dirname);
var bundleTrackerPlugin = new BundleTracker({filename: 'webpack-bundle.json'});
var commonsChunkPlugin = new webpack.optimize.CommonsChunkPlugin({names: 'vendor'});
var occurenceOrderPlugin = new webpack.optimize.OccurenceOrderPlugin();
//var extractTextPlugin = new ExtractTextPlugin('[name].[contenthash].css');
var extractTextPlugin = new ExtractTextPlugin('[name].css');
var providePlugin = new webpack.ProvidePlugin({
    $: 'jquery',
    '_': 'underscore',
    jQuery: 'jquery',
    'window.jQuery': 'jquery',
});
var config = {
    entry: {
        dashboard: './assets/js/dashboard.js',
        vendor: ['materialize-css', 'jquery', 'jquery.cookie',]
    },
    output: {
        path: resolve('assets/bundles/'),
        publicPath: '/static/bundles/',
        filename: '[name].js',
        //    filename: '[name].[chunkhash].js'
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel'
            },
            {
                test: /\.json$/,
                loader: 'json'
            },
            {
                test: /\.scss$/,
                loader: ExtractTextPlugin.extract(['css?sourceMap', 'postcss', 'sass'])
            },
            {
                test: /\.(eot|jpg|jpeg|otf|png|svg|ttf|woff|woff2)(\?v=[0-9.]+)?$/,
                //loader: 'file?name=[name].[hash].[ext]',
                loader: 'file?name=[name].[ext]',
                include: [resolve('node_modules'), resolve('static/assets/images'), resolve('static/assets/img')]
            }
        ]
    },
    plugins: [bundleTrackerPlugin, commonsChunkPlugin, extractTextPlugin, occurenceOrderPlugin, providePlugin],
    postcss: function () {
        return [autoprefixer];
    },
    resolve: {
        alias: {
            'jquery': resolve('node_modules/jquery/dist/jquery.js'),
        }
    },
    sassLoader: {sourceMap: true}
};
module.exports = config;

