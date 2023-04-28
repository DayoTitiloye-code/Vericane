module.exports = {
    webpack: (config, options) => {
        config.module.rules.push({
            test: /\.svg$/,
            use: ["@svgr/webpack"]
        })
        return config
    },
    sassOptions: {
        includePaths: [__dirname + '/styles']
    },
}