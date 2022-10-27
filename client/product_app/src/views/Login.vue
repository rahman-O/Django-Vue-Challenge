<template>
    <dev class="log-in">
        <h1>Login</h1>
        <form  @submit.prevent="submitForm">
            <input type="email" name="username" v-model="username">
            <input type="password" name="password" v-model="password">
            <button type="submit">Login Up</button>
        
        </form>
    </dev>

    
</template>

<script>
    import axios from 'axios';
    export default {
        
        name: 'Login',
        data() {
         return {
         username: '',
         password: '',
         }
        },
        methods: {
            submitForm(e) {
               const formData={
                username: this.username,
                password: this.password
               }

            axios
                    .post('api/v1/token/login', formData)
                    .then(response => {
                   
                   // console.log(response)
                    const token =response.data.token
                    this.$store.commit('setToken',token)
                    axios.defaults.headers.common['Authorization'] = "Token " + token
                    localStorage.setItem['token',token]
                   
                    window.location.href = 'http://127.0.0.1:8000/';
                 })
                 .catch(error=>{
                    console.log(error)
                 })

            }
        }
    }

</script>
