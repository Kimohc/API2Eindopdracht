// store.js

import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        loggedIn: false,
        user: {},
        access_token: '',
    },
    mutations: {
        setLoggedIn(state, payload) {
            state.loggedIn = payload;
        },
        setUser(state, payload) {
            state.user = payload;
        },
        setAccess_Token(state, payload){
            state.access_token = payload;
        }
    },

    actions: {
        // You can define actions here to perform asynchronous operations and commit mutations.
        // Actions are optional but useful for more complex scenarios.
        SetLoggedIn(state, payload){
            state.commit('setLoggedIn', payload)
        },
        SetUser(state, payload){
            state.commit('setAccount', payload)
        },
        SetAccess_Token(state, payload){
            state.commit('setAccess_Token', payload)
        }
    },
    getters: {
        // You can define getters here to compute derived state based on the store's state.
        // Getters are optional but useful for transforming or filtering state data.
        getLoggedIn(state){
            return state.loggedIn;
        },
        getUser(state){
            return state.user;
        },
        getAccess_Token(state){
            return state.access_token;
        }
    }
});
