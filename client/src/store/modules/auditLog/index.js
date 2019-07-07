import mutations from "./mutations";
import actions from "./actions";
import getters from "./getters";

const state = {
  auditLogData: {
    count: 0,
    results: []
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
