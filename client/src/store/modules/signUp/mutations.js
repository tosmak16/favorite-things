import {
  SIGNUP_START,
  SIGNUP_SUCCESS,
  SIGNUP_FAIL,
  CLEAR_SERVER_ERROR
} from "./types";

const mutations = {
  [SIGNUP_START](state, formData) {
    state = Object.assign(state, {
      formData,
      isLoading: true,
      errorMessage: ""
    });
  },

  [SIGNUP_SUCCESS](state, isSuccess) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess
    });
  },

  [SIGNUP_FAIL](state, errorMessage) {
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
  }
};

export default mutations;
