const getters = {
  addCategoryErrorMessage: state => state.errorMessage,
  isAddCategorySuccess: state => state.isSuccess,
  categoryList: state => state.categoryData
};

export default getters;
