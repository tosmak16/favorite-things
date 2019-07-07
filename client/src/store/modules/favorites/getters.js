const getters = {
  addFavoriteErrorMessage: state => state.errorMessage,
  isAddFavoriteSuccess: state => state.isSuccess,
  favoriteList: state => state.favoriteData,
  getFavoritesById: state => id => {
    return state.favoriteData.results.find(item => item.id === id);
  },
  isEditFavoriteSuccess: state => state.isSuccess,
  editFavoriteErrorMessage: state => state.errorMessage,
  isDeleteFavoriteSuccess: state => state.isDeleteSuccess,
  isFavoritesLoading: state => state.isLoading
};

export default getters;
