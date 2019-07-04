import mutations from "./mutations";
import actions from "./actions";
import getters from "./getters";

const state = {
  formData: {
    username: "",
    email: "",
    password: ""
  },
  isLoading: false,
  errorMessage: "",
  isSuccess: false
};

export default {
  state,
  mutations,
  actions,
  getters
};
