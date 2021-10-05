import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// base url 
import axios from "axios";
axios.defaults.baseURL = 'http://127.0.0.1:8000'
// const app = createApp(App)
Vue.config.globalProperties.axios = axios;
// app.use(store).use(router).mount('#app')



Vue.config.productionTip = false

// for bootstrap 5
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// welcome page
import SequentialEntrance from 'vue-sequential-entrance'
import 'vue-sequential-entrance/vue-sequential-entrance.css'
Vue.use(SequentialEntrance);
