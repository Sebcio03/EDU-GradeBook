import { createApp } from 'vue'
import App from './App.vue'

import router from './router/index.js'
import store from './store/index.js'
import Toast from "vue-toastification";

import '../node_modules/nprogress/nprogress.css' 
import "vue-toastification/dist/index.css";
import './index.css'

createApp(App)
    .use(router)
    .use(store)
    .use(Toast, {
        transition: "my-custom-fade",
        maxToasts: 20,
        newestOnTop: true,
        position: "top-right",
        timeout: 5000,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        showCloseButtonOnHover: true,
        closeButton: "button",
        icon: true,
        rtl: false
    })
    .mount('#app')