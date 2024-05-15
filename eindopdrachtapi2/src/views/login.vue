<template>
<div id="app">
  <div class="alertContainer">
    <my-alert ref="myAlert"  ></my-alert>
  </div>
  <svg v-on:click="$router.push('/')" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M11.9481 14.8285L10.5339 16.2427L6.29126 12L10.5339 7.7574L11.9481 9.17161L10.1197 11H17.6568V13H10.1197L11.9481 14.8285Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M23 19C23 21.2091 21.2091 23 19 23H5C2.79086 23 1 21.2091 1 19V5C1 2.79086 2.79086 1 5 1H19C21.2091 1 23 2.79086 23 5V19ZM19 21H5C3.89543 21 3 20.1046 3 19V5C3 3.89543 3.89543 3 5 3H19C20.1046 3 21 3.89543 21 5V19C21 20.1046 20.1046 21 19 21Z" fill="currentColor" /></svg>
  <div class="container3">
  <div class="login" v-if="registered">
    <div class="border">
    <h1>Login</h1>
  <input  type="text" v-model="username" required placeholder="Username">
  <input type="password" v-model="password" required placeholder="Password">
  <button v-on:click="loginUser">Login</button>
    <button v-on:click="registered = false">Not yet registerd?</button>
    </div>
  </div>
  <div class="register" v-else>
    <div class="border">
    <h1>Register</h1>
    <input v-on:input="checkIfAlert" type="text" v-model="usernameRegister" required placeholder="Username">
    <input v-on:input="checkIfAlert" type="password" v-model="passwordRegister" required placeholder="Password">
    <button v-on:click="registerUser">Register</button>
    <button v-on:click="registered = true">Already registered but clicked on not yet registered?</button>
    </div>
    </div>
</div>
</div>
</template>
<script>
import '/src/app.css';
import axios from "axios";
import MyAlert from "@/components/Alert.vue";

export default {
  name: 'App',
  components: {
    'my-alert': MyAlert,
  },


    data() {
      return {
        registered: true,
        usernameRegister: '',
        passwordRegister: '',
        username: '',
        password: '',
        access_token: '',
        message1: 'Gebruiker geregistreerd',
      }
    },
    methods: {
      async registerUser() {
        try {
          if(this.usernameRegister === '' || this.passwordRegister === ''){
            this.showAlert("Vul alle velden in", false)
            return
          }
          let response = await axios.post(`http://127.0.0.1:8000/users/`, {
            username: this.usernameRegister,
            password: this.passwordRegister,
          })
          this.usernameRegister = ''
          this.passwordRegister = ''
          console.log(response)
          this.showAlert("Successfully registered", true)
          this.registered = true
        }
        catch (error) {
          this.showAlert(error, false)
        }
      },
      async loginUser() {
        try {
          if(this.username === '' || this.password === ''){
            this.showAlert("Vul alle velden in", false)
            return
          }
          let response = await axios.post(`http://127.0.0.1:8000/users/login`, {
            username: this.username,
            password: this.password,
          })
          console.log(this.username)
          console.log(this.password)
          console.log(response)
          this.access_token = response.data.access_token
          console.log(this.access_token)
          this.$store.commit('setLoggedIn', true);
          this.$store.commit('setAccess_Token', this.access_token);
          this.$store.commit('setUser', {
            username: this.username,
            gebruiker_id: response.data.gebruiker_id
          });
          await this.redirectToHome()
          console.log(this.$store.state.loggedIn);
          console.log(this.$store.state.user);
          console.log(this.$store.state.access_token);
        }
          catch (error){
          this.showAlert("Gebruikersnaam of wachtwoord is onjuist", false)
          }
      },
      showAlert(message, isGood) {
        this.$refs.myAlert.showToast()
        this.$refs.myAlert.message = message
        this.$refs.myAlert.isGood = isGood
      },
      checkIfAlert(){
        this.$refs.myAlert.closeToast()
      },
      async redirectToHome() {
        await this.$router.push({
          path: '/home',
          query: { showAlert: true }
        });
      }

    },
    async created() {

    },
    mounted() {

    }
  }
</script>
