<template>
  <div>
    <div class="main-container">
      <SelectMenu :category-list="categoryList" />
      <FavoriteTable :on-click="showEditFavoriteModal" />
    </div>

    <SpeedDial
      :on-add-category-icon-click="showAddCategoryModel"
      :on-add-favorite-icon-click="showAddFavoriteModal"
      :on-show-audit-logs-icon-click="showAuditLogsModal"
    />

    <section>
      <b-modal :active.sync="isAuditLogModalActive">
        <AuditLogTable />
      </b-modal>
    </section>

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
import FavoriteTable from "../../components/table/FavoriteTable";
import EditFavoriteForm from "../../components/forms/editFavoriteForm/EditFavoriteForm";
import AuditLogTable from "../../components/table/AuditLogTable";
import SelectMenu from "../../components/selectMenu/SelectMenu";

export default {
  name: "Home",
  data: () => ({
    isCategoryModalActive: false,
    isFavoriteModalActive: false,
    isEditModalActive: false,
    isAuditLogModalActive: false,
    favoriteId: null
  }),

  created() {
    this.getCategories();

    if (!this.isLoggedIn) {
      this.logOut();
    }
  },

  components: {
    SpeedDial,
    AddCategoryForm,
    FavoriteForm,
    FavoriteTable,
    EditFavoriteForm,
    AuditLogTable,
    SelectMenu
  },

  methods: {
    showAddCategoryModel() {
      this.isCategoryModalActive = true;
    },
    showAddFavoriteModal() {
      this.isFavoriteModalActive = true;
    },
    showAuditLogsModal() {
      this.isAuditLogModalActive = true;
    },

    showEditFavoriteModal(selectedFavorite) {
      this.favoriteId = selectedFavorite.id;
      this.isEditModalActive = true;
    },

    getFavorites(page = 1, ordering = "-modified_date") {
      const token = localStorage.getItem("token");
      this.$store.dispatch("getFavorites", {
        token,
        page,
        ordering,
        category: this.selectedCategory
      });
    },

    logOut() {
      localStorage.removeItem("token");
      this.$router.push("/login");
    },

    getCategories() {
      const token = localStorage.getItem("token");
      if (token) {
        this.$store.dispatch("getCategories", token);
      }
    }
  },

  watch: {
    isAddCategorySuccess(newValue, oldValue) {
      if (newValue === true && newValue !== oldValue) {
        this.isCategoryModalActive = false;
        this.getCategories();
      }
    },

    isAddFavoriteSuccess(newValue, oldValue) {
      if (newValue === true && newValue !== oldValue) {
        this.isFavoriteModalActive = false;
        this.getFavorites();
        this.getCategories();
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
    },
    selectedCategory(newValue, oldValue) {
      if (newValue !== oldValue) {
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
      "isDeleteFavoriteSuccess",
      "isLoggedIn",
      "selectedCategory"
    ]),

    token() {
      return localStorage.getItem("token");
    }
  }
};
</script>
