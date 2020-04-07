import Vue from 'vue';
import VueRouter, {RouteConfig} from 'vue-router';

Vue.use(VueRouter);

const loadView = function (name: string) {
  // @ts-ignore
  return resolve => require(["@/views/" + name + ".vue"], resolve)
};

const routes: Array<RouteConfig> = [
  {
    path: "/",
    component: loadView("Desktop")
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
