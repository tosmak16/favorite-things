import Vue from "vue";
import Vuex from "vuex";
import signUp from "./modules/signUp";
import login from "./modules/login";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    signUp,
    login
  }
});
