import {
  LOGIN_START,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  CLEAR_SERVER_ERROR
} from "./types";

const mutations = {
  [LOGIN_START](state, formData) {
    state = Object.assign(state, {
      formData,
      isLoading: true,
      errorMessage: ""
    });
  },

  [LOGIN_SUCCESS](state, isSuccess) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess
    });
  },

  [LOGIN_FAIL](state, errorMessage) {
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
