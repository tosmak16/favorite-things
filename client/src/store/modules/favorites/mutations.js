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

const mutations = {
  [ADD_FAVORITE_START](state, formData) {
    state = Object.assign(state, {
      formData,
      isLoading: true,
      errorMessage: "",
      isSuccess: false
    });
  },

  [ADD_FAVORITE_SUCCESS](state, isSuccess) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess
    });
  },

  [ADD_FAVORITE_FAIL](state, errorMessage) {
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

  [GET_FAVORITES_START](state, isLoading) {
    state = Object.assign(state, {
      isLoading: isLoading,
      errorMessage: "",
      isGetSuccess: false
    });
  },

  [GET_FAVORITES_SUCCESS](state, favoriteData) {
    state = Object.assign(state, {
      isLoading: false,
      isGetSuccess: true,
      favoriteData
    });
  },

  [GET_FAVORITES_FAIL](state, errorMessage) {
    state = Object.assign(state, {
      isLoading: false,
      isGetSuccess: false,
      errorMessage
    });
  },

  [EDIT_FAVORITE_START](state, formData) {
    state = Object.assign(state, {
      formData,
      isLoading: true,
      errorMessage: "",
      isSuccess: false
    });
  },

  [EDIT_FAVORITE_SUCCESS](state, isSuccess) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess
    });
  },

  [EDIT_FAVORITE_FAIL](state, errorMessage) {
    state = Object.assign(state, {
      isLoading: false,
      isSuccess: false,
      errorMessage
    });
  },
  [DELETE_FAVORITE_START](state, isLoading) {
    state = Object.assign(state, {
      isLoading: isLoading,
      errorMessage: "",
      isDeleteSuccess: false
    });
  },

  [DELETE_FAVORITE_SUCCESS](state, isDeleteSuccess) {
    state = Object.assign(state, {
      isLoading: false,
      isDeleteSuccess
    });
  },

  [DELETE_FAVORITE_FAIL](state, errorMessage) {
    state = Object.assign(state, {
      isLoading: false,
      isDeleteSuccess: false,
      errorMessage
    });
  }
};

export default mutations;
