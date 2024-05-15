<template>
  <div id="app">
  <my-header :logged_in="logged_in"></my-header>
    <div class="alert-container">
      <my-alert ref="myAlert" :message="message1"></my-alert>
    </div>

    <div class="container4">
      <div class="textitto">
        <h1>Ben je nog opzoek naar een huisdier?</h1>

        <p>Welkom bij onze huisdieren adoptie service! Wij helpen je graag bij het vinden van jouw perfecte huisdier. Of je nu op zoek bent naar een speelse kitten, een trouwe hond, of een kleurrijke vogel, wij hebben een breed scala aan schattige dieren die wachten om jouw nieuwe metgezel te worden. Blader door onze adoptiecentrum en vind jouw nieuwe beste vriend vandaag nog!</p>      </div>
      <div class="imgitto">
        <img src="/HomePage.svg" alt="">
      </div>
      </div>
  <my-footer></my-footer>
  </div>
</template>
<script>
import MyHeader from "@/components/Header.vue";
import '/src/app.css';
import MyFooter from "@/components/Footer.vue";
import MyAlert from "@/components/Alert.vue";
//import axios from "axios";

export default {
  name: 'App',
  components: {
    'my-footer': MyFooter,
    'my-header': MyHeader,
    'my-alert': MyAlert,
  },
  data() {
    return {
    logged_in: false,
      user: {},
      access_token: '',
      message1: 'Ingelogd',
    }
  },
  methods: {


  },
  async created(){
  },
  mounted() {
    this.logged_in = this.$store.getters.getLoggedIn
    this.user = this.$store.getters.getUser
    this.access_token = this.$store.getters.getAccess_Token
    if (this.$route.query.showAlert === 'true') {
      this.$refs.myAlert.showToast();
      this.$refs.myAlert.isGood = true
      this.$router.replace({ path: '/home', query: null });
    }
      console.log(this.access_token)
  }
}
</script>