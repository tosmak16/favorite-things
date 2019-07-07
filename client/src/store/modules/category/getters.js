const getters = {
  addCategoryErrorMessage: state => state.errorMessage,
  isAddCategorySuccess: state => state.isSuccess,
  categoryList: state => state.categoryData,
  selectedCategory: state => state.selectedCategory,
  isCategoryLoading: state => state.isLoading
};

export default getters;
