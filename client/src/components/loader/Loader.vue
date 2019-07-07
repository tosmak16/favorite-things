<template>
  <section>
    <b-loading
      :is-full-page="true"
      :active.sync="isLoading"
      :can-cancel="true"
    ></b-loading>
  </section>
</template>

<script>
export default {
  name: "Loader",
  props: {
    isLoading: Boolean
  }
};
</script>
