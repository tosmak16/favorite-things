<template>
  <div id="app">
    <Loader
      :is-loading="
        isFavoritesLoading ||
          isCategoryLoading ||
          isAuditLogsLoading ||
          isSignUpLoading ||
          isLoginLoading
      "
    />

    <Navbar />
    <router-view />
  </div>
</template>

<style lang="scss">
@import "~bulma/sass/utilities/_all";
@import "./style.scss";
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>

<script>
import { mapGetters } from "vuex";

import Navbar from "./components/navbar/Navbar";
import Loader from "./components/loader/Loader";

export default {
  name: "App",
  components: {
    Navbar,
    Loader
  },
  computed: {
    ...mapGetters([
      "isFavoritesLoading",
      "isCategoryLoading",
      "isAuditLogsLoading",
      "isSignUpLoading",
      "isLoginLoading"
    ]),

    token() {
      return localStorage.getItem("token");
    }
  }
};
</script>
