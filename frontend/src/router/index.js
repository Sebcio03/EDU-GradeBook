import {createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/Landing/HomeView.vue'
import AuthenticateView from '../views/Landing/AuthenticateView.vue'
import LoginForm from '../components/Landing/Forms/Login.vue'
import RegisterForm from '../components/Landing/Forms/Register.vue'

import OrganizationsListView from '../views/App/OrganizationsListView.vue'
import AuthenticatedView from '../views/App/AuthenticatedView.vue'

import { isAuthenticated } from '../utils/authentication.js'

import NProgress from 'nprogress';


const routes = [
    {path: '/', name:'Home', component: HomeView, meta: { allowUnauthenticated: true }},
    {path: '/', name:'Authentication', component: AuthenticateView, meta: { guardBeforeAuthenticated: true }, children: [
      {path: 'login', name: 'Login', component: LoginForm},
      {path: 'register', name:'Register', component: RegisterForm}
    ]},
    {path: '/', name: 'Authenticated', component: AuthenticatedView, children: [
      {path: '/organizations/', name: "OrganizationsList", component: OrganizationsListView}
    ]}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach(async (to, from, next) => {
  if (to.meta.allowUnauthenticated){
    return next()
  } 

  const isUserAuthenticated = await isAuthenticated()
  const isAuthenticatedView = to.matched.some(e => e.name === 'Authenticated')
  if (to.meta.guardBeforeAuthenticated === true && isUserAuthenticated){
    return next({name: "OrganizationsList"})
  } else if (!isAuthenticatedView && isUserAuthenticated){
    return next('/')
  }
  return next()
})

router.beforeResolve((to, from, next) => {
  if (to.name) {
      NProgress.start()
  }
  next()
})

router.afterEach(() => {
  NProgress.done()
})

export default router;
