<template>
  <div id="app">
    <my-header :logged_in="logged_in"></my-header>
    <my-modal ref="myModal"></my-modal>
    <div class="alert-container">
      <my-alert ref="myAlert"></my-alert>
      </div>
    <div class="container">
      <div class="categorien" v-show="show">
        <div class="card">
          <img src="/undraw_playful_cat_re_ac9g.svg" alt="">
        <button v-on:click="getRandom(1)">Katten</button>
        </div>
        <div class="card">
          <img src="/undraw_playing_fetch_cm19.svg" alt="">
        <button v-on:click="getRandom(2)">Honden</button>
        </div>
          <div class="card">
            <img src="/undraw_teddy_bear_hns1.svg" alt="">
        <button v-on:click="getRandom(3)">Overige</button>
        </div>
      </div>

      <div class="dier-cards">
    <div v-show="showDieren" class="dier-div" v-for="dier in dieren"  :key="dier.dier_id">
      <img :src="dier.foto[foto]" alt="">
      <h2>Naam: {{dier.naam}}</h2>
      <h3>Geslacht: {{dier.geslacht}}</h3>
      <h3>Ras: {{dier.ras}}</h3>
      <svg v-on:click="showModal(dier.commentaar)" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M17 9H7V7H17V9Z" fill="currentColor" /><path d="M7 13H17V11H7V13Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M2 18V2H22V18H16V22H14C11.7909 22 10 20.2091 10 18H2ZM12 16V18C12 19.1046 12.8954 20 14 20V16H20V4H4V16H12Z" fill="currentColor" /></svg>

    </div>

      <div class="dier-icons" v-show="showDieren">
        <svg v-on:click="saveDier" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M12.0122 5.57169L10.9252 4.48469C8.77734 2.33681 5.29493 2.33681 3.14705 4.48469C0.999162 6.63258 0.999162 10.115 3.14705 12.2629L11.9859 21.1017L11.9877 21.0999L12.014 21.1262L20.8528 12.2874C23.0007 10.1395 23.0007 6.65711 20.8528 4.50923C18.705 2.36134 15.2226 2.36134 13.0747 4.50923L12.0122 5.57169ZM11.9877 18.2715L16.9239 13.3352L18.3747 11.9342L18.3762 11.9356L19.4386 10.8732C20.8055 9.50635 20.8055 7.29028 19.4386 5.92344C18.0718 4.55661 15.8557 4.55661 14.4889 5.92344L12.0133 8.39904L12.006 8.3918L12.005 8.39287L9.51101 5.89891C8.14417 4.53207 5.92809 4.53207 4.56126 5.89891C3.19442 7.26574 3.19442 9.48182 4.56126 10.8487L7.10068 13.3881L7.10248 13.3863L11.9877 18.2715Z" fill="currentColor" /></svg>

        <svg v-on:click="prevFoto" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20.3284 11.0001V13.0001L7.50011 13.0001L10.7426 16.2426L9.32842 17.6568L3.67157 12L9.32842 6.34314L10.7426 7.75735L7.49988 11.0001L20.3284 11.0001Z" fill="currentColor" /></svg>
        <svg v-on:click="nextFoto" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M15.0378 6.34317L13.6269 7.76069L16.8972 11.0157L3.29211 11.0293L3.29413 13.0293L16.8619 13.0157L13.6467 16.2459L15.0643 17.6568L20.7079 11.9868L15.0378 6.34317Z" fill="currentColor" /></svg>

        <svg v-on:click="rejectDier" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.2253 4.81108C5.83477 4.42056 5.20161 4.42056 4.81108 4.81108C4.42056 5.20161 4.42056 5.83477 4.81108 6.2253L10.5858 12L4.81114 17.7747C4.42062 18.1652 4.42062 18.7984 4.81114 19.1889C5.20167 19.5794 5.83483 19.5794 6.22535 19.1889L12 13.4142L17.7747 19.1889C18.1652 19.5794 18.7984 19.5794 19.1889 19.1889C19.5794 18.7984 19.5794 18.1652 19.1889 17.7747L13.4142 12L19.189 6.2253C19.5795 5.83477 19.5795 5.20161 19.189 4.81108C18.7985 4.42056 18.1653 4.42056 17.7748 4.81108L12 10.5858L6.2253 4.81108Z" fill="currentColor" /></svg>
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
import MyModal from "@/components/Modal.vue";
import MyAlert from "@/components/Alert.vue";
export default {
  name: 'App',
  components: {
    'my-footer': MyFooter,
    'my-header': MyHeader,
    'my-modal': MyModal,
    'my-alert': MyAlert,
  },

  data() {
    return {
      dieren: [],
      foto: 1,
      dierOffset: 0,
      length: 0,
      show: true,
      showDieren: false,
      dierValue: 0,
      access_token: '',
      showCommentaar: false,
      user: {},
      logged_in: false,
    }
  },
  methods: {
    showModal(message){
      this.$refs.myModal.toggleModal()
      this.$refs.myModal.message = message
    },
    showAlert(message, isGood) {
      this.$refs.myAlert.showToast()
      this.$refs.myAlert.message = message
      this.$refs.myAlert.isGood = isGood
    },
    async getRandom(value) {
      if (this.logged_in === true) {
        let responseRandom = await axios.get(`http://127.0.0.1:8000/random?soort=${value}`)
        this.dierOffset = responseRandom.data.offset
        this.length = responseRandom.data.length
        console.log(this.dierOffset)
        console.log(this.length)
        await this.getDier(value)
        console.log(this.access_token)
      } else {
        this.showAlert('Je moet ingelogd zijn om dieren te kunnen bekijken', false)
      }
    },
    async getDier(value) {
      try {
        this.show = false
        this.showDieren = true
        this.dierValue = value
        let response = await axios.get(`http://127.0.0.1:8000/dier?limit=1&offset=${this.dierOffset}&soort=${value}`, {
          headers: {
            'Authorization': `Bearer ${this.access_token}`
          }
        })
        console.log(response.status)
        this.dieren = response.data.map(dier => ({
          dier_id: dier.dier_id,
          naam: dier.naam,
          geslacht: dier.geslacht,
          ras: dier.ras,
          commentaar: dier.commentaar,
          foto: dier.foto.split(',')
        }))
        console.log(this.dieren)

      } catch (error) {
        this.showAlert("nieuwe token ophalen", true)
        let responseNieuweAcces_token = await axios.get(`http://127.0.0.1:8000/refresh?username=${this.user.username}`)
        this.access_token = responseNieuweAcces_token.data.access_token
        console.log(responseNieuweAcces_token.data.access_token)
        await this.getDier(this.dierValue)
      }


    },
    nextFoto() {
      if (this.foto >= this.dieren[0].foto.length - 1) {
        alert('Dit is de laatste foto')
      } else {
        console.log(this.dieren[0].foto.length)
        console.log(this.foto)
        this.foto += 1
      }
    },
    prevFoto() {
      if (this.foto < 2) {
        alert('Dit is de eerste foto')
      } else {
        console.log(this.dieren[0].foto.length)
        console.log(this.foto)
        this.foto -= 1
      }
    },
    async saveDier() {
      try {
        let response = await axios.post('http://127.0.0.1:8000/reservering/', {
          gebruiker_id: this.user.gebruiker_id,
          dier_id: this.dieren[0].dier_id
        }, {
          headers: {
            'Authorization': `Bearer ${this.access_token}`
          }
        })

        console.log(response)
        this.dierOffset += 1
        if (this.dierOffset >= this.length) {
          console.log(this.dierOffset)
          console.log(this.length)
          this.dierOffset = 0
          await this.getDier(this.dierValue)
          return
        }
        await this.getDier(this.dierValue)
        this.foto = 1
      } catch (error) {
        this.showAlert("nieuwe token ophalen", true)
        let responseNieuweAcces_token = await axios.get(`http://127.0.0.1:8000/refresh?username=${this.user.username}`)
        this.access_token = responseNieuweAcces_token.data.access_token
        console.log(responseNieuweAcces_token.data.access_token)
        await this.saveDier()
      }
    },
  async rejectDier(){
    this.dierOffset += 1
    if (this.dierOffset >= this.length) {
      console.log(this.dierOffset)
      console.log(this.length)
      this.dierOffset = 0
      await this.getDier(this.dierValue)
      return
    }
    await this.getDier(this.dierValue)
    this.foto = 1
  }
    },
  mounted() {
    this.logged_in = this.$store.getters.getLoggedIn
    this.user = this.$store.getters.getUser
    this.access_token = this.$store.getters.getAccess_Token

  }
}
</script>

<style>

</style>
