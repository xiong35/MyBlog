import Vue from "vue";
import App from "./App.vue";
import router from "./routers";
import store from "./store"
import mavonEditor from 'mavon-editor'

import "font-awesome/css/font-awesome.css";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import 'mavon-editor/dist/css/index.css'

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.use(mavonEditor);

Vue.config.productionTip = false;

Vue.directive('title', {
  inserted: function (el, binding) {
    document.title = el.dataset.title
  }
})

new Vue({
  render: h => h(App),
  router,
  store
}).$mount("#app");
