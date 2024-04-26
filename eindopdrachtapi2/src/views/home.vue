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

export default {
  name: 'App',
  components: {
    'my-footer': MyFooter,
    'my-header': MyHeader,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    }
  },
  methods: {
  },
  created(){
  }
}
</script>

<style>

</style>
