const getters = {
  loginErrorMessage: state => state.errorMessage,
  isLoggedInSuccess: state => state.isSuccess,
  isLoggedIn: state => state.isLoggedIn,
  isLoginLoading: state => state.isLoading
};

export default getters;
