import axios from 'axios';

import { whenCSRFMethod, injectCSRF, handleAuthenticationErrors } from './middleware.js';

const axiosSettings = {
    baseURL: import.meta.env.VITE_API_ENDPOINT || '/api/',
    withCredentials: true,
    headers:{
        'content-type': 'application/json',
    }
}

const instance = axios.create(axiosSettings);
instance.interceptors.request.use(injectCSRF, (error) => Promise.reject(error), {runWhen: whenCSRFMethod});
instance.interceptors.response.use((response) => response, handleAuthenticationErrors);

export const notinterceptedInstance = axios.create(axiosSettings);
export default instance