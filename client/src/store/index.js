import Vue from "vue";
import Vuex from "vuex";
import signUp from "./modules/signUp";
import login from "./modules/login";
import category from "./modules/category";
import favorite from "./modules/favorites";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    signUp,
    login,
    category,
    favorite
  }
});
