<template>
  <form class="form">
    <img src="../../../assets/logo.png" width="58" height="58" />

    <h2>Login</h2>
    <div class="field">
      <div class="control">
        <label for="username">Username</label>
        <input
          @focus="onFocus"
          v-model="formaData.username"
          id="username"
          name="username"
          class="input"
          type="text"
          v-validate="'required'"
          placeholder="Enter your username"
        />
        <span class="error-label">{{ errors.first("username") }}</span>
        <span v-if="loginErrorMessage.username" class="error-label">
          {{ loginErrorMessage.username[0] }}
        </span>
      </div>
    </div>

    <div class="field">
      <div class="control">
        <label for="password">Password</label>
        <input
          @focus="onFocus"
          v-model="formaData.password"
          name="password"
          id="password"
          class="input"
          type="password"
          placeholder="Enter your password"
          v-validate="'required'"
        />
        <span class="error-label">{{ errors.first("password") }}</span>
        <span v-if="loginErrorMessage.password" class="error-label">
          {{ loginErrorMessage.password[0] }}
        </span>
      </div>
    </div>

    <span v-if="loginErrorMessage.error" class="error-label login-error">
      {{ loginErrorMessage.error }}
    </span>

    <div class="btn-link-wrapper">
      <div class="sign-in-link-container">
        Don't have an account?&nbsp;
        <router-link to="/sign-up">Click here</router-link>
      </div>
      <button
        type="button"
        @click="validateForm"
        class="button btn-primary signup-button"
      >
        <strong>Login</strong>
      </button>
    </div>
  </form>
</template>

<style lang="scss" scoped>
@import "./loginForm.scss";
</style>

<script>
import { mapGetters } from "vuex";

export default {
  name: "LoginForm",
  computed: {
    ...mapGetters(["loginErrorMessage"])
  },
  data() {
    return {
      formaData: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    async validateForm() {
      const isValid = await this.$validator.validate();
      if (isValid) return this.$store.dispatch("login", this.formaData);
    },

    onFocus() {
      if (this.loginErrorMessage) {
        return this.$store.dispatch("clearServerError");
      }
    }
  }
};
</script>
