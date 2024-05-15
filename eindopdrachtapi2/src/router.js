import VueRouter from 'vue-router';
import Vue from 'vue';
import Home from "@/views/home.vue";
import Dieren from "@/views/dieren.vue";
import Login from "@/views/login.vue";
import Favorieten from "@/views/favorieten.vue";
Vue.use(VueRouter);

const routes = [
    { path: '/', redirect: '/home'},
    { path: '/home', component: Home },
    { path: '/dieren', component: Dieren, },
    { path: '/login', component: Login},
    {path: '/favorieten', component: Favorieten ,}

];

// Create router instance
const router = new VueRouter({
    mode: 'history', // This sets the router mode to use HTML5 History API
    routes
});


// Export router instance
export default router;