import Vue from "vue";
import VueRouter from "vue-router";

const Artical = () => import("views/body/artical/Artical");

Vue.use(VueRouter);

const routes = [
  {
    path: "",
    redirect: "/artical"
  },
  {
    path: "/artical",
    component: Artical
  }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

export default router;
