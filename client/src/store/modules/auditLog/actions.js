import axios from "axios";

import {
  GET_AUDIT_LOGS_START,
  GET_AUDIT_LOGS_SUCCESS,
  GET_AUDIT_LOGS_FAIL
} from "./types";

const actions = {
  async getAuditLogs({ commit }, { token, page, ordering }) {
    commit(GET_AUDIT_LOGS_START, true);
    await axios
      .get(
        `${
          process.env.VUE_APP_API_BASE_URL
        }audit_logs/?page=${page}&ordering=${ordering}`,
        {
          headers: { Authorization: `Token ${token}` }
        }
      )
      .then(response => {
        commit(GET_AUDIT_LOGS_SUCCESS, response.data);
      })
      .catch(error => commit(GET_AUDIT_LOGS_FAIL, error.response.data));
  }
};

export default actions;
