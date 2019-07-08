import mutations from "./mutations";
import actions from "./actions";
import getters from "./getters";

const state = {
  formData: {
    name: ""
  },
  categoryData: [],
  isLoading: false,
  errorMessage: "",
  isSuccess: false,
  selectedCategory: null,
  isAddCategorySuccess: false
};

export default {
  state,
  mutations,
  actions,
  getters
};
