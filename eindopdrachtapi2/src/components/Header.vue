<template>
  <header>
    <nav>
      <div id="logo">
        <svg width="40" height="32" viewBox="0 0 40 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M12.8 32H0V21.9849C0 17.1239 4.0116 13.1839 8.96 13.1839H15.2V0.468341C15.2 0.251458 15.3792 0.0754376 15.6 0.0754376C15.7184 0.0754376 15.8308 0.127301 15.9068 0.216883L17.3616 1.92719C18.402 1.07577 19.74 0.563816 21.2 0.563816H22C23.442 0.563816 24.7656 1.06359 25.8 1.89654L27.2932 0.14066C27.3692 0.0514706 27.4812 0 27.6 0C27.8208 0 28 0.175628 28 0.392904V15.3896H23.36C17.528 15.3896 12.8 20.0337 12.8 25.7623V32Z" fill="#45413E" />
          <path fill-rule="evenodd" clip-rule="evenodd" d="M29.76 17.0569V12.0875C29.76 12.0836 29.76 12.0797 29.76 12.0758V6.79004C29.76 6.57435 29.9392 6.4 30.16 6.4C30.266 6.4 30.3676 6.44095 30.4424 6.51389L31.9576 7.98784C32.7864 7.42501 33.7936 7.09504 34.88 7.09504C35.97 7.09504 36.9808 7.42735 37.8112 7.99369L39.3176 6.52793C39.3924 6.45499 39.494 6.41404 39.6 6.41404C39.8208 6.41404 40 6.58878 40 6.80408V23.2632C40 28.0883 35.9884 32 31.04 32H14.4V25.7938C14.4 20.969 18.4116 17.0569 23.36 17.0569H29.76Z" fill="#45413E" />
        </svg>

        Jakubski's <br> Dieren
      </div>
      <ul class="navigation-menu">
        <li> <router-link :to="{path: `/home`}">Home</router-link></li>
        <li><router-link :to="{path: `/dieren`}">Dieren </router-link></li>
      </ul>
      <div id="utility" v-if="logged_in">
       <router-link :to="{path: `/favorieten`}"> <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.14648 12.2929C8.36544 11.5118 8.36544 10.2455 9.14648 9.46444C9.92753 8.68339 11.1939 8.68339 11.9749 9.46444L12 9.48955L12.0251 9.46449C12.8061 8.68345 14.0725 8.68345 14.8535 9.46449C15.6346 10.2455 15.6346 11.5119 14.8535 12.2929L12.0251 15.1213L12 15.0962L11.9749 15.1213L9.14648 12.2929Z" fill="currentColor" /><path fill-rule="evenodd" clip-rule="evenodd" d="M3 4C3 2.34315 4.34315 1 6 1H18C19.6569 1 21 2.34315 21 4V20C21 21.6569 19.6569 23 18 23H6C4.34315 23 3 21.6569 3 20V4ZM6 3H18C18.5523 3 19 3.44772 19 4V20C19 20.5523 18.5523 21 18 21H6C5.44772 21 5 20.5523 5 20V4C5 3.44772 5.44772 3 6 3Z" fill="currentColor" /></svg> </router-link>
       <router-link :to="{path: '/home'}"> <svg v-on:click="logOut" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.51428 20H4.51428C3.40971 20 2.51428 19.1046 2.51428 18V6C2.51428 4.89543 3.40971 4 4.51428 4H8.51428V6H4.51428V18H8.51428V20Z" fill="currentColor" /><path d="M13.8418 17.385L15.262 15.9768L11.3428 12.0242L20.4857 12.0242C21.038 12.0242 21.4857 11.5765 21.4857 11.0242C21.4857 10.4719 21.038 10.0242 20.4857 10.0242L11.3236 10.0242L15.304 6.0774L13.8958 4.6572L7.5049 10.9941L13.8418 17.385Z" fill="currentColor" /></svg></router-link>
      </div>
      <div id="utility" v-else>
        <router-link :to="{path: '/login'}">
        <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg" class="log-in">
          <path
              d="M15.4857 20H19.4857C20.5903 20 21.4857 19.1046 21.4857 18V6C21.4857 4.89543 20.5903 4 19.4857 4H15.4857V6H19.4857V18H15.4857V20Z"
              fill="currentColor"/>
          <path
              d="M10.1582 17.385L8.73801 15.9768L12.6572 12.0242L3.51428 12.0242C2.96199 12.0242 2.51428 11.5765 2.51428 11.0242C2.51429 10.4719 2.962 10.0242 3.51429 10.0242L12.6765 10.0242L8.69599 6.0774L10.1042 4.6572L16.4951 10.9941L10.1582 17.385Z"
              fill="currentColor"/>
        </svg>
        </router-link>

      </div>
    </nav>
  </header>

</template>

<script>

export default {
  name: 'MyHeader',
  props:{
    logged_in: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      title: 'My Component',
      message: 'This is my custom Vue component!',
    };
  },
  mounted() {

  },
  methods:{
    logOut(){
      this.$store.commit('setLoggedIn', false);
      this.$store.commit('setAccess_Token', '');
      location.reload()
    }
  }

};
</script>
