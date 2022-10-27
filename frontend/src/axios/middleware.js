import axios from './index.js'

import state from '../store/index'
import router from '../router/index.js'

export async function injectCSRF(config){
    const response = await axios.get('users/csrf/')
    const token = response.data['token']
    config.headers['X-CSRFToken'] = token
    return config;
}

export function whenCSRFMethod(config) {
    return ['post', 'put', 'patch', 'delate'].includes(config.method)
}

export async function handleAuthenticationErrors(promise) {    
    if ([401, 403, 500].includes(promise.response?.status)){
        state.commit('setUserData', {})
        router.push('/login')
        return promise
    } 
    return promise
}