import Vue from 'vue';
import App from './App.vue';
import router from './plugins/router';
import TaskManager from '@/plugins/taskManager';
// @ts-ignore
import VueMatomo from 'vue-matomo';

Vue.config.productionTip = false;

Vue.use(TaskManager);

Vue.use(VueMatomo, {
  host: "https://analytics.finn-thorben.me/",
  siteId: 2,
  trackerFileName: "matomo",
  router: router,
  enableLinkTracking: true,
  requireConsent: false,
  trackInitialView: true,
  disableCookies: false,
  enableHeartBeatTimer: false,
  debug: false,
})

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
