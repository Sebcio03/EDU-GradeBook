import {createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/Landing/HomeView.vue'
import AuthenticateView from '../views/Landing/AuthenticateView.vue'
import LoginForm from '../components/Landing/Forms/Login.vue'
import RegisterForm from '../components/Landing/Forms/Register.vue'

const routes = [
    {path: '/', name:'Home', component: HomeView},
    {path: '/auth/', component: AuthenticateView, children: [
      {path: 'login', name: 'Login', component: LoginForm},
      {path: 'register', name:'Register', component: RegisterForm}
    ]},
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router;
