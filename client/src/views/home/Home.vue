<template>
  <div>
    <Table :on-click="showEditFavoriteModal" />

    <SpeedDial
      :on-add-category-icon-click="showAddCategoryModel"
      :on-add-favorite-icon-click="showAddFavoriteModal"
    />

    <section>
      <b-modal :active.sync="isCategoryModalActive" has-modal-card>
        <AddCategoryForm />
      </b-modal>
    </section>

    <section>
      <b-modal :active.sync="isFavoriteModalActive" has-modal-card>
        <FavoriteForm :category-list="categoryList" />
      </b-modal>
    </section>

    <section>
      <b-modal :active.sync="isEditModalActive" has-modal-card>
        <EditFavoriteForm
          :category-list="categoryList"
          :favorite-id="favoriteId"
        />
      </b-modal>
    </section>
  </div>
</template>

<style lang="scss" scoped>
@import "./Home.scss";
</style>

<script>
import { mapGetters } from "vuex";
import SpeedDial from "../../components/speedDial/SpeedDial";
import AddCategoryForm from "../../components/forms/addCategoryForm/AddCategoryForm";
import FavoriteForm from "../../components/forms/favoriteForm/FavoriteForm";
import Table from "../../components/table/Table";
import EditFavoriteForm from "../../components/forms/editFavoriteForm/EditFavoriteForm";

export default {
  name: "Home",
  data: () => ({
    isCategoryModalActive: false,
    isFavoriteModalActive: false,
    isEditModalActive: false,
    favoriteId: null
  }),

  created() {
    const token = localStorage.getItem("token");
    if (token && this.categoryList.length === 0) {
      this.$store.dispatch("getCategories", token);
    }
  },

  components: {
    SpeedDial,
    AddCategoryForm,
    FavoriteForm,
    Table,
    EditFavoriteForm
  },

  methods: {
    showAddCategoryModel() {
      this.isCategoryModalActive = true;
    },
    showAddFavoriteModal() {
      this.isFavoriteModalActive = true;
    },

    showEditFavoriteModal(selectedFavorite) {
      this.favoriteId = selectedFavorite.id;
      this.isEditModalActive = true;
    },

    getFavorites(page = 1, ordering = "-modified_date") {
      const token = localStorage.getItem("token");
      this.$store.dispatch("getFavorites", { token, page, ordering });
    }
  },

  watch: {
    isAddCategorySuccess(newValue, oldValue) {
      if (newValue === true && newValue !== oldValue) {
        this.isCategoryModalActive = false;
      }
    },

    isAddFavoriteSuccess(newValue, oldValue) {
      if (newValue === true && newValue !== oldValue) {
        this.getFavorites();

        this.isFavoriteModalActive = false;
      }
    },
    isEditFavoriteSuccess(newValue, oldValue) {
      if (newValue === true && newValue !== oldValue) {
        this.getFavorites();

        this.isEditModalActive = false;
      }
    },

    isDeleteFavoriteSuccess(newValue, oldValue) {
      this.isEditModalActive = false;

      if (newValue === true && newValue !== oldValue) {
        this.getFavorites();
      }
    }
  },

  computed: {
    ...mapGetters([
      "isAddCategorySuccess",
      "categoryList",
      "isAddFavoriteSuccess",
      "favoriteList",
      "isEditFavoriteSuccess",
      "isDeleteFavoriteSuccess"
    ])
  }
};
</script>
