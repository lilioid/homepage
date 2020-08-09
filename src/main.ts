import Vue from 'vue';
import App from './App.vue';
import router from './plugins/router';
import TaskManager from '@/plugins/taskManager';

Vue.config.productionTip = false;

Vue.use(TaskManager);

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
