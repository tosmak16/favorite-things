<template>
  <section>
    <b> Filter </b>
    <b-field>
      <b-select multiple size="8" v-model="selectedOptions">
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
section {
  display: grid;
  justify-content: start;
  grid-gap: 10px;
  grid-template-rows: repeat(3, min-content);
}

button {
  width: 89.5px;
}
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
