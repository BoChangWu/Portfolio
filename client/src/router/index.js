import { createRouter, createWebHistory } from 'vue-router'
import Info from '../views/Info.vue'

const routes = [
  {
    path: '/',
    name: 'Info',
    component: Info
  },
  {
    path: '/works',
    name: 'Works',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "works" */ '../views/Works.vue')
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import(/* webpackChunkName: "contact" */ '../views/Contact.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "contact" */ '../views/About.vue')
  },
  {
    path: '/TryLogin',
    name: 'TryLogin',
    component: () => import(/* webpackChunkName: "ping" */ '../views/TryLogin.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
