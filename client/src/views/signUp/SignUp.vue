<template>
  <div class="container">
    <div class="content-text">
      Do you need a tool that allows you to track your favorite things? You are
      in the right place.
      <router-link to="/login">Login Now!</router-link>
    </div>

    <div class="auth-wrapper">
      <SignUpForm />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import SignUpForm from "./signUpForm/SignUpForm";

export default {
  name: "signUp",
  components: {
    SignUpForm
  },

  created() {
    const token = localStorage.getItem("token");
    if (token) {
      this.$router.push("/");
    }
  },

  watch: {
    isSignUpSuccess(newValue, oldValue) {
      if (newValue === true && newValue !== oldValue) {
        this.$router.push("/");
      }
    }
  },

  computed: {
    ...mapGetters(["isSignUpSuccess"])
  }
};
</script>

<style lang="scss" scoped>
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
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
