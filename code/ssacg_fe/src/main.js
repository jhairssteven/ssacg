import { createApp } from 'vue'
// import App from './App.vue'
import App from './AppOld.vue'
// import App from './MainPage.vue'
// import App from './components/ProductListByCat.vue'
import router from './router'

createApp(App).use(router).mount('#app')
