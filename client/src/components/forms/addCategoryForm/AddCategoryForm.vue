<template>
  <div class="container">
    <img src="../../../assets/logo.png" width="58" height="58" />
    <h2>Add Category</h2>

    <div class="control">
      <label for="category">Category Name</label>
      <input
        @focus="onFocus"
        v-model="category"
        id="category"
        name="category"
        class="input"
        type="text"
        v-validate="'required|min:3'"
        placeholder="Enter category name"
      />
      <span class="error-label">{{ errors.first("category") }}</span>
      <span v-if="addCategoryErrorMessage.name" class="error-label">
        {{ addCategoryErrorMessage.name[0] }}
      </span>
    </div>

    <button type="button" @click="addCategory" class="button btn-primary">
      <strong>Save</strong>
    </button>
  </div>
</template>

<style lang="scss" scoped>
@import "./AddCategoryForm.scss";
.error-label {
  color: orangered;
}
</style>

<script>
import { mapGetters } from "vuex";

export default {
  name: "AddCategoryForm",
  computed: {
    ...mapGetters(["addCategoryErrorMessage"])
  },
  data: () => ({
    category: ""
  }),
  methods: {
    onFocus() {
      if (this.addCategoryErrorMessage) {
        return this.$store.dispatch("clearServerError");
      }
    },

    async addCategory() {
      const token = localStorage.getItem("token");

      const isValid = await this.$validator.validate();
      if (isValid && token)
        return this.$store.dispatch("addCategory", {
          name: this.category,
          token
        });
    }
  }
};
</script>
