import axios from "axios";

import {
  LOGIN_START,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  CLEAR_SERVER_ERROR
} from "./types";

const actions = {
  async login({ commit }, formData) {
    commit(LOGIN_START, formData);
    await axios
      .post(`${process.env.VUE_APP_API_BASE_URL}login/`, formData)
      .then(response => {
        localStorage.setItem("token", response.data.token);
        localStorage.setItem("owner", response.data.userId);

        commit(LOGIN_SUCCESS, response.status === 200);
      })
      .catch(error => commit(LOGIN_FAIL, error.response.data));
  },

  clearServerError({ commit }) {
    commit(CLEAR_SERVER_ERROR, "");
  }
};

export default actions;
