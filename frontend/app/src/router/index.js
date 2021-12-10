import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home'
import Login from '../views/Login'
import Funcionario from '../views/Funcionario'
import Orcamento from '../views/Orcamento'
import Business from '../views/Business'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/funcionario',
    name: 'Funcionario',
    component: Funcionario
  },
  {
    path: '/orcamento',
    name: 'Orçamento',
    component: Orcamento
  },
  {
    path: '/bu',
    name: 'bu',
    component: Business,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
