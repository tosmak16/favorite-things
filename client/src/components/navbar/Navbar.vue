<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        <img src="../../assets/logo.png" width="58" height="58" />
      </a>

      <a
        role="button"
        class="navbar-burger burger"
        v-bind:class="{ 'is-active': isActive }"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
        @click="toggleNav"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div
      id="navbarBasicExample"
      class="navbar-menu"
      v-bind:class="{ 'is-activee': isActive }"
    >
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link
              v-if="!isLoggedIn"
              to="/sign-up"
              class="button btn-primary"
            >
              <i class="fas fa-user-plus"></i>
            </router-link>
            <router-link
              v-if="!isLoggedIn"
              to="/login"
              class="button is-success is-outlined"
              ><i class="fas fa-sign-in-alt"></i
            ></router-link>
            <button
              v-if="isLoggedIn"
              type="button"
              class="button is-success is-outlined"
              @click="logOut"
            >
              <i class="fas fa-sign-out-alt"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss" scoped>
nav {
  border-bottom: 1px solid #41b883;
}

.is-activee {
  @media (max-width: 1024px) {
    display: grid;
    justify-content: center;
  }
}

.navbar-burger {
  height: 74px;
}

.navbar-item img {
  max-height: 100%;
}

.btn-primary {
  background-color: #41b883;
  color: white;
  border-color: transparent;

  &:hover {
    color: #41b883;
    border-color: transparent;
    background-color: white;
    border: 1.3px solid #41b883;
  }
}
</style>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Navbar",
  data() {
    return {
      isActive: false
    };
  },
  methods: {
    logOut() {
      localStorage.removeItem("token");
      this.$store.dispatch("logout");
      this.$router.push("/login");
    },
    toggleNav() {
      this.isActive = !this.isActive;
    }
  },

  computed: {
    ...mapGetters(["isLoggedIn"])
  }
};
</script>
