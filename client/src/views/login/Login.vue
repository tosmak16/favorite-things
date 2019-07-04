<template>
  <div class="container">
    <div class="content-text">
      Do you need a tool that allows you to track your favorite things and you
      don't have an account? You are in the right place.
      <router-link to="/sign-up">Register Now!</router-link>
    </div>

    <div class="auth-wrapper">
      <LoginForm />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import LoginForm from "./loginForm/LoginForm";

export default {
  name: "Login",
  components: {
    LoginForm
  },

  created() {
    const token = localStorage.getItem("token");
    if (token) {
      this.$router.push("/");
    }
  },

  watch: {
    isLoggedInSuccess(newValue, oldValue) {
      if (newValue === true && newValue !== oldValue) {
        this.$router.push("/");
      }
    }
  },

  computed: {
    ...mapGetters(["isLoggedInSuccess"])
  }
};
</script>

<style lang="scss" scoped>
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding-top: 5rem;
  grid-gap: 2rem;

  @media (max-width: 1024px) {
    margin: 0 2rem;
  }

  @media (max-width: 874px) {
    grid-template-columns: auto;
  }

  @media (max-width: 500px) {
    margin-bottom: 2rem;
  }
}
.content-text {
  color: #36495d;
  font-size: 1.5rem;

  @media (min-width: 874px) {
    max-width: 464px;
    padding: 50% 0;
    height: 100%;
  }

  & > a {
    color: #41b883;
  }
}
</style>
