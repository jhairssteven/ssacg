import { createRouter, createWebHashHistory } from 'vue-router'
// import App from './App.vue'
import App from './AppOld.vue'
import MainPage from './MainPage.vue'
import ProductListByCat from './components/ProductListByCat.vue';
import LogIn from './components/LogIn.vue';
import SignUp from './components/SignUp.vue';
import Products from './components/Products/Products.vue';
import ProductMainPage from './components/ProductMainPage.vue';

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
    path: '/u/products',
    name: 'products',
    component: Products,
    props: true
  },
  {
    path: '/products/category/:category',
    name: 'productListByCat',
    component: ProductListByCat,
    props: true
  },
  {
    path: '/mainpage/',
    name: 'mainPage',
    component: MainPage,
    props: true
  },
  {
    path: '/:category/product/:pid',
    name: 'productMainPage',
    component: ProductMainPage,
    props: true
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})
export default router;
