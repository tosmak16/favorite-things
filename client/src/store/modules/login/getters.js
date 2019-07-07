const getters = {
  loginErrorMessage: state => state.errorMessage,
  isLoggedInSuccess: state => state.isSuccess,
  isLoggedIn: state => state.isLoggedIn
};

export default getters;
