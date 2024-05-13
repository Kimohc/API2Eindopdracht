<template>
  <div id="app">
  <my-header></my-header>
  <my-footer></my-footer>
  </div>
</template>
<script>
import MyHeader from "@/components/Header.vue";
import '/src/app.css';
import MyFooter from "@/components/Footer.vue";
//import axios from "axios";

export default {
  name: 'App',
  components: {
    'my-footer': MyFooter,
    'my-header': MyHeader,
  },
  data() {
    return {

    }
  },
  methods: {



  },
  async created(){

  }
}
</script>