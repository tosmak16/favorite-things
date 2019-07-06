import mutations from "./mutations";
import actions from "./actions";
import getters from "./getters";

const state = {
  formData: {
    name: ""
  },
  favoriteData: {
    count: 0,
    results: []
  },
  isLoading: false,
  errorMessage: "",
  isSuccess: false,
  isGetSuccess: false,
  isDeleteSuccess: false
};

export default {
  state,
  mutations,
  actions,
  getters
};
