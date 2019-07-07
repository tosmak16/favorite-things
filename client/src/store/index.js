import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

import signUp from "./modules/signUp";
import login from "./modules/login";
import category from "./modules/category";
import favorite from "./modules/favorites";
import auditLog from "./modules/auditLog";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    signUp,
    login,
    category,
    favorite,
    auditLog
  },
  plugins: [
    createPersistedState({
      paths: ["login"]
    })
  ]
});
