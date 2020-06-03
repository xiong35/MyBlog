import Vue from "vue";
import VueRouter from "vue-router";

const Visiter = () => import("views/Visiter")

const Article = () => import("views/body/article/Article");
const BlogContent = () => import("views/body/article/BlogContent")
const TrapContent = () => import("views/body/article/TrapContent")
const Admin = () => import("views/admin/Admin")

const NotYet = () => import("components/common/NotYet")
const NotFound = () => import("components/common/NotFound")


Vue.use(VueRouter);

const routes = [
  {
    path: "",
    redirect: "/article"
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
        path: "/article",
        component: Article
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
