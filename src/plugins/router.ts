import Vue from 'vue';
import VueRouter, {RouteConfig} from 'vue-router';
import Desktop from '@/views/Desktop.vue';

Vue.use(VueRouter);

const loadView = function (name: string) {
  // @ts-ignore
  return resolve => require(["@/views/" + name + ".vue"], resolve)
};

const routes: Array<RouteConfig> = [
  {path: "/", redirect: {name: "desktop", query: {app: ["contact", "cv"]}}},

  {
    path: "/desktop",
    name: "desktop",
    component: Desktop
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});
export default router;

