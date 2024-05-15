<template>
<div id="app">
  <my-header :logged_in="logged_in"></my-header>
  <div class="alert-container">
    <my-alert ref="myAlert"></my-alert>
  </div>
    <div class="dieren-container" >
      <h2>Favoriten: </h2>
      <div class="dieren" >
        <div class="dier" v-for="dier in dieren" :key="dier.dier_id">
          <img :src="dier.foto" alt="">
          <h3>{{dier.naam}}</h3>
          <button v-on:click="annuleerReservering(dier.reservering_id)">Annuleer</button>
        </div>
      </div>
  </div>
  <my-footer></my-footer>
</div>
</template>
<script>
import MyHeader from "@/components/Header.vue";
import '/src/app.css';
import MyFooter from "@/components/Footer.vue";
import axios from "axios";
import MyAlert from "@/components/Alert.vue";
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
      reserveringen: [],
      dieren: [],
    }
  },
  methods: {
    showAlert(message, isGood) {
      this.$refs.myAlert.showToast()
      this.$refs.myAlert.message = message
      this.$refs.myAlert.isGood = isGood
    },
    async getFavorieten() {
      try {
        let response = await axios.get(`http://127.0.0.1:8000/reserveringen`, {
          headers: {
            'Authorization': `Bearer ${this.access_token}`
          },
        })
        console.log(response)
        this.reserveringen = response.data
        for (let i = 0; i < this.reserveringen.length; i++) {
          await this.getDierById(this.reserveringen[i].dier_id)
          this.dieren[i].reservering_id = this.reserveringen[i].reservering_id
        }
      } catch (error) {
        this.showAlert("nieuwe token ophalen", true)
        let responseNieuweAcces_token = await axios.get(`http://127.0.0.1:8000/refresh?username=${this.user.username}`)
        this.access_token = responseNieuweAcces_token.data.access_token
        console.log(responseNieuweAcces_token.data.access_token)
        await this.getFavorieten()
      }
    },
    async getDierById(id) {
      let response = await axios.get(`http://127.0.0.1:8000/dier/${id}`)
      console.log(response)
      let dier = {
        dier_id: response.data.dier_id,
        naam: response.data.naam,
        foto: response.data.foto,
        reservering_id: null,
      }
      dier.foto = dier.foto.split(',')
      this.dieren.push(dier)
      console.log(this.dieren)
    },
    async annuleerReservering(reservering_id) {
      try {
        let response = await axios.delete(`http://127.0.0.1:8000/reservering/${reservering_id}`,{
          headers: {
            'Authorization': `Bearer ${this.access_token}`
          },
        })
        console.log(response)
        this.reserveringen = []
        this.dieren = []
        await this.getFavorieten()
      } catch (error) {
        this.showAlert("nieuwe token ophalen", true)
        let responseNieuweAcces_token = await axios.get(`http://127.0.0.1:8000/refresh?username=${this.user.username}`)
        this.access_token = responseNieuweAcces_token.data.access_token
        console.log(responseNieuweAcces_token.data.access_token)
        await this.annuleerReservering(reservering_id)
      }
    }
  },
  async created() {
  },
  mounted() {
    this.logged_in = this.$store.getters.getLoggedIn
    this.user = this.$store.getters.getUser
    this.access_token = this.$store.getters.getAccess_Token
    this.getFavorieten()
  }
}
</script>