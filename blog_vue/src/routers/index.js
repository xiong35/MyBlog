import Vue from "vue";
import VueRouter from "vue-router";

const Visiter = () => import("views/Visiter")

const Artical = () => import("views/body/artical/Artical");
const BlogContent = () => import("views/body/artical/BlogContent")
const TrapContent = () => import("views/body/artical/TrapContent")
const Admin = () => import("views/admin/Admin")

const NotYet = () => import("components/common/NotYet")
const NotFound = () => import("components/common/NotFound")


Vue.use(VueRouter);

const routes = [
  {
    path: "",
    redirect: "/artical"
  },
  {
    path: '/admin',
    component: Admin
  },
  {
    path: '*',
    component: Visiter,
    children: [
      {
        path: "/blog/:blogId",
        component: BlogContent
      },
      {
        path: "/trap/:trapId",
        component: TrapContent
      },
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
    ]
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
  base: '/blog/static'
});

router.afterEach((to, from) => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
})

export default router;
