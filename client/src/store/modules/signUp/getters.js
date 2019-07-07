const getters = {
  signUpErrorMessage: state => state.errorMessage,
  isSignUpSuccess: state => state.isSuccess,
  isSignUpLoading: state => state.isLoading
};

export default getters;
