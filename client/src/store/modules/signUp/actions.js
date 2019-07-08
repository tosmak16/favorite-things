import axios from "axios";

import {
  SIGNUP_START,
  SIGNUP_SUCCESS,
  SIGNUP_FAIL,
  CLEAR_SERVER_ERROR
} from "./types";

import { LOGIN_SUCCESS } from "../login/types";

const actions = {
  async signUp({ commit }, formData) {
    commit(SIGNUP_START, formData);
    await axios
      .post(`${process.env.VUE_APP_API_BASE_URL}users/`, formData)
      .then(response => {
        localStorage.setItem("token", response.data.token);
        localStorage.setItem("owner", response.data.userId);

        commit(SIGNUP_SUCCESS, response.status === 200);
        commit(LOGIN_SUCCESS, response.status === 200);
      })
      .catch(error => commit(SIGNUP_FAIL, error.response.data));
  },

  clearServerError({ commit }) {
    commit(CLEAR_SERVER_ERROR, "");
  }
};

export default actions;
