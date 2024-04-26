import VueRouter from 'vue-router';
import Vue from 'vue';
import Home from "@/views/home.vue";

Vue.use(VueRouter);

const routes = [
    { path: '/', component: Home, },


];

// Create router instance
const router = new VueRouter({
    mode: 'history', // This sets the router mode to use HTML5 History API
    routes
});

// Export router instance
export default router;