import VueRouter from 'vue-router';
import Vue from 'vue';
import Home from "@/views/home.vue";
import Dieren from "@/views/dieren.vue";
import Login from "@/views/login.vue";
Vue.use(VueRouter);

const routes = [
    { path: '/', component: Home,  },
    { path: '/dieren', component: Dieren},
    { path: '/login', component: Login},

];

// Create router instance
const router = new VueRouter({
    mode: 'history', // This sets the router mode to use HTML5 History API
    routes
});

// Export router instance
export default router;