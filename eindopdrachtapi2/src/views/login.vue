<template>
<div id="app">
  <h1>Login</h1>
  <div class="login" v-show="registered">
  <input type="text" v-model="username" required placeholder="Username">
  <input type="password" v-model="password" required placeholder="Password">
  <button v-on:click="loginUser">Login</button>
  </div>
  <div class="register" v-show="register">
    <input type="text" v-model="usernameRegister" required placeholder="Username">
    <input type="password" v-model="passwordRegister" required placeholder="Password">
    <button v-on:click="registerUser">Register</button>
  </div>
  <button v-on:click="register = true">Not yet registerd?</button>
</div>
</template>
<script>
import '/src/app.css';
import axios from "axios";

export default {
  name: 'App',
  components: {},
  data() {
    return {
      registered: true,
      register: false,
      usernameRegister: '',
      passwordRegister: '',
      username: '',
      password: '',
      access_token: '',
    }
  },
  methods: {
    async registerUser(){
      let response = await axios.post(`http://127.0.0.1:8000/users/`, {
        username: this.usernameRegister,
        password: this.passwordRegister,
      })
      console.log(response)
    },
    async loginUser(){
      let response = await axios.post(`http://127.0.0.1:8000/users/login`, {
        username: this.username,
        password: this.password,
      })
      console.log(this.username)
      console.log(this.password)
      console.log(response)
    }
  },
  async created() {

  }
}
</script>