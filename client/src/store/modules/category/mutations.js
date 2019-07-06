import {
  ADD_CATEGORY_START,
  ADD_CATEGORY_SUCCESS,
  ADD_CATEGORY_FAIL,
  CLEAR_SERVER_ERROR,
  GET_CATEGORY_START,
  GET_CATEGORY_SUCCESS,
  GET_CATEGORY_FAIL
} from "./types";

const mutations = {
  [ADD_CATEGORY_START](state, formData) {
    state = Object.assign(state, {
      formData,
      isLoading: true,
      errorMessage: "",
      isSuccess: false
    });
  },

  [ADD_CATEGORY_SUCCESS](state, isSuccess) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess
    });
  },

  [ADD_CATEGORY_FAIL](state, errorMessage) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess: false,
      errorMessage
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
  }
};

export default mutations;
