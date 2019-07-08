const getters = {
  addCategoryErrorMessage: state => state.errorMessage,
  isAddCategorySuccess: state => state.isAddCategorySuccess,
  categoryList: state => state.categoryData,
  selectedCategory: state => state.selectedCategory,
  isCategoryLoading: state => state.isLoading
};

export default getters;
