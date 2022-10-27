const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer:{
    proxy: 'http://locahost:8000'
  }
  
}

