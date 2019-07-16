<template>
  <section>
    <b class="filter"> Filter </b>
    <b-field>
      <b-select size="8" multiple v-model="selectedOptions">
        <option
          @click="filterByCategory"
          v-for="item in categoryList"
          :key="item.id"
          :value="item.id"
          >{{ item.name }}</option
        >
      </b-select>
    </b-field>
    <button @click="clearFilter" type="button" class="button btn-danger">
      <i class="fas fa-times"></i>
    </button>
  </section>
</template>

<style lang="scss" scoped>
@import "./SelectMenu.scss";
</style>

<script>
export default {
  data() {
    return {
      selectedOptions: [null]
    };
  },
  props: {
    categoryList: Array
  },

  methods: {
    filterByCategory() {
      const selectedCategory = this.selectedOptions[
        this.selectedOptions.length - 1
      ];
      return this.$store.dispatch("addSelectedCategory", selectedCategory);
    },

    clearFilter() {
      return this.$store.dispatch("clearSelectedCategory");
    }
  }
};
</script>
