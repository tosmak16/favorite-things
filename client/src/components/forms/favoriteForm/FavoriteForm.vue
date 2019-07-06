<template>
  <div class="container">
    <img src="../../../assets/logo.png" width="58" height="58" />

    <h2>Add that thing you love so much</h2>

    <div class="control">
      <label for="title">Title</label>
      <input
        @focus="onFocus"
        v-model="formData.title"
        id="title"
        name="title"
        class="input"
        type="text"
        v-validate="'required|min:3'"
        placeholder="Enter title"
      />
      <span class="error-label">{{ errors.first("title") }}</span>
      <span v-if="addFavoriteErrorMessage.non_field_errors" class="error-label">
        The title already exist.
      </span>
    </div>

    <div class="control">
      <label for="description">Description</label>
      <b-input
        placeholder="Enter something interesting.."
        maxlength="200"
        type="textarea"
        id="description"
        name="description"
        v-model="formData.description"
        v-validate="'min:10'"
      ></b-input>
      <span class="error-label">{{ errors.first("description") }}</span>
    </div>

    <div class="control">
      <label for="category">Category</label>
      <b-select
        name="category"
        id="category"
        expanded
        placeholder="Select category"
        v-model="formData.category"
        v-validate="'required'"
        class="is-success"
      >
        <option
          v-for="option in categoryList"
          :value="option.id"
          :key="option.id"
        >
          {{ option.name }}
        </option>
      </b-select>
      <span class="error-label">{{ errors.first("category") }}</span>
    </div>

    <div class="control">
      <label for="ranking">Ranking</label>
      <b-select
        name="ranking"
        id="ranking"
        expanded
        placeholder="Select rank number"
        v-model="formData.ranking"
        v-validate="'required'"
      >
        <option v-for="option in rankingList" :value="option" :key="option">
          {{ option }}
        </option>
      </b-select>
      <span class="error-label">{{ errors.first("ranking") }}</span>
    </div>

    <MetaDetaField :on-add-meta="handleAddMeta" />

    <Tags closable :tag-list="formData.metadata" :remove-tag="removeTag" />

    <button type="button" @click="addFavorite" class="button btn-primary">
      <strong>Save</strong>
    </button>
  </div>
</template>

<style lang="scss" scoped>
@import "./FavoriteForm.scss";
.error-label {
  color: orangered;
}
</style>

<script>
import { mapGetters } from "vuex";
import MetaDetaField from "../metaDeta/MetaData";
import Tags from "../../tags/Tags";

export default {
  name: "FavoriteForm",
  props: {
    categoryList: Array
  },
  components: {
    MetaDetaField,
    Tags
  },
  computed: {
    ...mapGetters(["addFavoriteErrorMessage"]),

    rankingList() {
      const selectedCategory = this.formData.category;
      if (selectedCategory.length === 0) {
        return [1];
      }
      const { favorites__count } = this.categoryList.find(
        item => item.id === selectedCategory
      );
      return Array.from(
        { length: favorites__count || 1 },
        (value, index) => index + 1
      );
    }
  },
  data: () => ({
    formData: {
      title: "",
      category: "",
      description: null,
      ranking: "",
      metadata: [],
      owner: ""
    }
  }),
  methods: {
    async addFavorite() {
      const token = localStorage.getItem("token");

      const isValid = await this.$validator.validate();
      if (isValid === false || !token) return;

      const owner = localStorage.getItem("owner");
      const description = this.formData.description
        ? this.formData.description
        : null;
      const favoriteData = { ...this.formData, owner, description };
      return this.$store.dispatch("addFavorite", {
        favoriteData,
        token
      });
    },
    onFocus() {
      if (this.addFavoriteErrorMessage) {
        return this.$store.dispatch("clearServerError");
      }
    },
    handleAddMeta(metaData) {
      this.formData.metadata.push(metaData);
    },

    removeTag(tagIndex) {
      const metaData = this.formData.metadata;
      this.formData.metadata = metaData.filter(
        (value, index) => tagIndex != index
      );
    }
  }
};
</script>
