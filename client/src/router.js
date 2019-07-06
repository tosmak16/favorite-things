import Vue from "vue";
import Router from "vue-router";

import Home from "./views/home/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("./views/login/Login.vue")
    },
    {
      path: "/sign-up",
      name: "SignUp",
      component: () => import("./views/signUp/SignUp.vue")
    }
  ]
});
