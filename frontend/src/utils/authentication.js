import store from '../store/index.js'
import { notinterceptedInstance } from '../axios/index.js'

function userNotInStorage(){
  return (store.state.user && Object.keys(store.state.user).length === 0)
}

export async function isAuthenticated(){
  if (userNotInStorage()){
    try{
      const r = await notinterceptedInstance.get('/users/me/')
      store.commit('setUserData', r.data)
    } catch {
      store.commit('setUserData', {})
    }
  }
  return !(userNotInStorage())
}