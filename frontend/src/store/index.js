import { createStore } from 'vuex'
import { useToast } from "vue-toastification";

import axios from '../axios/index.js'

const toast = useToast();

const store = createStore({
    state: {
      user: {}
    },
    mutations: {
      notify (state, content, toast_type) {
        toast(content, {type: toast_type})
      },
      setUserData (state, data) {
        state.user = data
      }
    },
    actions: {
      getUserData({ commit }) {
        axios.get('/users/me/')
          .then((res) => commit('setUserData', res.data))
          .catch(() => commit('setUserData', {}))
      }
    }
})
  
export default store