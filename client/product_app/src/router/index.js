import { createRouter, createWebHistory } from 'vue-router'
import SignUp from  '../views/SignUp.vue'
import Login from  '../views/Login.vue'
import Product from  '../views/Product.vue'

const routes = [
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'Login',
    component: Login
  },
  {
    path: '/product-list',
    name: 'Product',
    component: Product
  },
 
 
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
