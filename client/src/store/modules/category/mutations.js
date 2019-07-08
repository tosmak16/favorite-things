import {
  ADD_CATEGORY_START,
  ADD_CATEGORY_SUCCESS,
  ADD_CATEGORY_FAIL,
  CLEAR_SERVER_ERROR,
  GET_CATEGORY_START,
  GET_CATEGORY_SUCCESS,
  GET_CATEGORY_FAIL,
  ADD_SELECTED_CATEGORY,
  CLEAR_SELECTED_CATEGORY
} from "./types";

const mutations = {
  [ADD_CATEGORY_START](state, formData) {
    state = Object.assign(state, {
      formData,
      isLoading: true,
      errorMessage: "",
      isSuccess: false,
      isAddCategorySuccess: false
    });
  },

  [ADD_CATEGORY_SUCCESS](state, isSuccess) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess,
      isAddCategorySuccess: true
    });
  },

  [ADD_CATEGORY_FAIL](state, errorMessage) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess: false,
      errorMessage,
      isAddCategorySuccess: false
    });
  },

  [CLEAR_SERVER_ERROR](state, errorMessage) {
    state = Object.assign(state, {
      errorMessage
    });
  },

  [GET_CATEGORY_START](state, isLoading) {
    state = Object.assign(state, {
      isLoading: isLoading,
      errorMessage: "",
      isSuccess: false
    });
  },

  [GET_CATEGORY_SUCCESS](state, categoryData) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess: true,
      categoryData
    });
  },

  [GET_CATEGORY_FAIL](state, errorMessage) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess: false,
      errorMessage
    });
  },

  [ADD_SELECTED_CATEGORY](state, selectedCategory) {
    state = Object.assign(state, {
      selectedCategory
    });
  },

  [CLEAR_SELECTED_CATEGORY](state, selectedCategory) {
    state = Object.assign(state, {
      selectedCategory
    });
  }
};

export default mutations;
