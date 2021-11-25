
module.exports = {
    devServer: {
      proxy: process.env.PROXY_URL,
      disableHostCheck: true
    }
  }