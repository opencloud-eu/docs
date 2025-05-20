// Webpack plugin for raw-loader
export function rawLoaderPlugin() {
    return {
        name: 'custom-webpack-raw-loader',
        configureWebpack() {
            return {
                module: {
                    rules: [
                        {
                            test: /\.ya?ml$/i,
                            resourceQuery: /raw/,
                            use: 'raw-loader',
                        },
                    ],
                },
            };
        },
    };
}