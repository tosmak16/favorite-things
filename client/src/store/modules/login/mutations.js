import {
  LOGIN_START,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  CLEAR_SERVER_ERROR,
  LOG_OUT
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
      isSuccess,
      isLoggedIn: true
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
  },

  [LOG_OUT](state, isLoggedIn) {
    state = Object.assign(state, {
      isLoggedIn,
      isSuccess: false
    });
  }
};

export default mutations;
