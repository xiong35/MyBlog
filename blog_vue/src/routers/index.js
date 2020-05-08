import Vue from "vue";
import VueRouter from "vue-router";

const Artical = () => import("views/body/artical/Artical");
const Blog = () => import("views/body/artical/BlogContent")
const NotYet = () => import("components/common/NotYet")
const NotFound = () => import("components/common/NotFound")


Vue.use(VueRouter);

const routes = [
  {
    path: "",
    redirect: "/artical"
  },
  {
    path: "/blog/:blogId",
    component: Blog
  }
  ,
  {
    path: "/artical",
    component: Artical
  },
  {
    path: "/profile",
    component: NotYet
  },
  {
    path: "/works",
    component: NotYet
  },
  {
    path: "/resume",
    component: NotYet
  },
  {
    path: "*",
    component: NotFound
  }
];

const router = new VueRouter({
  routes,
  mode: "history"
});

export default router;
