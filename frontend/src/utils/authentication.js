import store from '../store/index.js'
import { notinterceptedInstance } from '../axios/index.js'

export async function isAuthenticated(){
  if (Object.keys(store.state.user).length === 0){
    try{
      const r = await notinterceptedInstance.get('/users/me/')
      store.commit('setUserData', r.data)
    } catch {
      store.commit('setUserData', {})
    }
  }
  return Object.keys(store.state.user).length === 0 ? false : true
}