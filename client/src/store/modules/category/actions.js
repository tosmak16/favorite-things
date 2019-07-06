import axios from "axios";

import {
  ADD_CATEGORY_START,
  ADD_CATEGORY_SUCCESS,
  ADD_CATEGORY_FAIL,
  CLEAR_SERVER_ERROR,
  GET_CATEGORY_START,
  GET_CATEGORY_SUCCESS,
  GET_CATEGORY_FAIL
} from "./types";

const actions = {
  async addCategory({ commit }, { name, token }) {
    commit(ADD_CATEGORY_START, { name });
    await axios
      .post(
        `${process.env.VUE_APP_API_BASE_URL}categories/`,
        { name },
        {
          headers: { Authorization: `Token ${token}` }
        }
      )
      .then(response => {
        commit(ADD_CATEGORY_SUCCESS, response.status === 201);
      })
      .catch(error => commit(ADD_CATEGORY_FAIL, error.response.data));
  },

  clearServerError({ commit }) {
    commit(CLEAR_SERVER_ERROR, "");
  },

  async getCategories({ commit }, token) {
    commit(GET_CATEGORY_START, true);
    await axios
      .get(`${process.env.VUE_APP_API_BASE_URL}categories/`, {
        headers: { Authorization: `Token ${token}` }
      })
      .then(response => {
        commit(GET_CATEGORY_SUCCESS, response.data);
      })
      .catch(error => commit(GET_CATEGORY_FAIL, error.response.data));
  }
};

export default actions;
