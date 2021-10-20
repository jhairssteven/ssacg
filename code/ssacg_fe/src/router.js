import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import LogIn from './components/LogIn.vue';
import SignUp from './components/SignUp.vue';
import Products from './components/Products/Products.vue';

const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/login',
    name: 'logIn',
    component: LogIn
  },
  {
    path: '/user/admin',
    name: 'signUp',
    component: SignUp
  },
  {
    path: '/u/products/',
    name: 'products',
    component: Products
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
export default router;
