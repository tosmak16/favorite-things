import mutations from "./mutations";
import actions from "./actions";
import getters from "./getters";

const state = {
  formData: {
    username: "",
    password: ""
  },
  isLoading: false,
  errorMessage: "",
  isSuccess: false,
  isLoggedIn: false
};

export default {
  state,
  mutations,
  actions,
  getters
};
