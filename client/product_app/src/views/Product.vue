<template>
   
   <div id="app">
      {{data}}
</div>
  </template>
  
  <script>
  import axios from 'axios';
  var conf ={
    headers:{'Access-Control-Allow-Origin' : '*'}
  }

export default {
    name:'app',
  data() {
    return {
      data: [],
    };
  },
  
  mounted () {
    axios.get('http://locahost:8080/products/')
      .then(response => (console.log(response)))
  },


};
</script>