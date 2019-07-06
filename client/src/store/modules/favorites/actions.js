import axios from "axios";

import {
  ADD_FAVORITE_START,
  ADD_FAVORITE_SUCCESS,
  ADD_FAVORITE_FAIL,
  CLEAR_SERVER_ERROR,
  GET_FAVORITES_START,
  GET_FAVORITES_SUCCESS,
  GET_FAVORITES_FAIL,
  EDIT_FAVORITE_START,
  EDIT_FAVORITE_SUCCESS,
  EDIT_FAVORITE_FAIL,
  DELETE_FAVORITE_START,
  DELETE_FAVORITE_SUCCESS,
  DELETE_FAVORITE_FAIL
} from "./types";

const actions = {
  async addFavorite({ commit }, { favoriteData, token }) {
    commit(ADD_FAVORITE_START, { favoriteData });
    await axios
      .post(`${process.env.VUE_APP_API_BASE_URL}favorites/`, favoriteData, {
        headers: { Authorization: `Token ${token}` }
      })
      .then(response => {
        commit(ADD_FAVORITE_SUCCESS, response.status === 201);
      })
      .catch(error => commit(ADD_FAVORITE_FAIL, error.response.data));
  },

  clearServerError({ commit }) {
    commit(CLEAR_SERVER_ERROR, "");
  },

  async getFavorites({ commit }, { token, page, ordering }) {
    commit(GET_FAVORITES_START, true);
    await axios
      .get(
        `${
          process.env.VUE_APP_API_BASE_URL
        }favorites/?page=${page}&ordering=${ordering}`,
        {
          headers: { Authorization: `Token ${token}` }
        }
      )
      .then(response => {
        commit(GET_FAVORITES_SUCCESS, response.data);
      })
      .catch(error => commit(GET_FAVORITES_FAIL, error.response.data));
  },

  async editFavorite({ commit }, { favoriteData, token, favoriteId }) {
    commit(EDIT_FAVORITE_START, { favoriteData });
    await axios
      .put(
        `${process.env.VUE_APP_API_BASE_URL}favorites/${favoriteId}/`,
        favoriteData,
        {
          headers: { Authorization: `Token ${token}` }
        }
      )
      .then(response => {
        commit(EDIT_FAVORITE_SUCCESS, response.status === 200);
      })
      .catch(error => commit(EDIT_FAVORITE_FAIL, error.response.data));
  },
  async deleteFavorite({ commit }, { token, favoriteId }) {
    commit(DELETE_FAVORITE_START, true);
    await axios
      .delete(`${process.env.VUE_APP_API_BASE_URL}favorites/${favoriteId}/`, {
        headers: { Authorization: `Token ${token}` }
      })
      .then(response => {
        commit(DELETE_FAVORITE_SUCCESS, response.status === 204);
      })
      .catch(error => commit(DELETE_FAVORITE_FAIL, error.response.data));
  }
};

export default actions;
