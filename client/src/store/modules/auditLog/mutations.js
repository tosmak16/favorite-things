import {
  GET_AUDIT_LOGS_START,
  GET_AUDIT_LOGS_SUCCESS,
  GET_AUDIT_LOGS_FAIL
} from "./types";

const mutations = {
  [GET_AUDIT_LOGS_START](state, isLoading) {
    state = Object.assign(state, {
      isLoading: isLoading,
      errorMessage: "",
      isGetSuccess: false
    });
  },

  [GET_AUDIT_LOGS_SUCCESS](state, auditLogData) {
    state = Object.assign(state, {
      isLoading: false,
      isGetSuccess: true,
      auditLogData
    });
  },

  [GET_AUDIT_LOGS_FAIL](state, errorMessage) {
    state = Object.assign(state, {
      isLoading: false,
      isGetSuccess: false,
      errorMessage
    });
  }
};

export default mutations;
