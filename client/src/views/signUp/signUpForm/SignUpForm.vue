<template>
  <form class="form">
    <img src="../../../assets/logo.png" width="58" height="58" />

    <h2>Create an account</h2>
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
          v-validate="'required|min:3|max:15'"
          placeholder="Enter your username"
        />
        <span class="error-label">{{ errors.first("username") }}</span>
        <span v-if="signUpErrorMessage.username" class="error-label">
          {{ signUpErrorMessage.username[0] }}
        </span>
      </div>
    </div>

    <div class="field">
      <div class="control">
        <label for="email">Email</label>
        <input
          @focus="onFocus"
          v-model="formaData.email"
          id="email"
          name="email"
          class="input"
          type="email"
          v-validate="'required|email'"
          placeholder="Enter a your email"
        />
        <span class="error-label">{{ errors.first("email") }}</span>
        <span v-if="signUpErrorMessage.email" class="error-label">
          {{ signUpErrorMessage.email[0] }}
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
          v-validate="'required|min:6'"
        />
        <span class="error-label">{{ errors.first("password") }}</span>
        <span v-if="signUpErrorMessage.password" class="error-label">
          {{ signUpErrorMessage.password[0] }}
        </span>
      </div>
    </div>

    <div class="btn-link-wrapper">
      <div class="sign-in-link-container">
        Have an account?&nbsp;
        <router-link to="/login">Sign In</router-link>
      </div>
      <button
        type="button"
        @click="validateForm"
        class="button btn-primary signup-button"
      >
        <strong>Sign up</strong>
      </button>
    </div>
  </form>
</template>

<style lang="scss" scoped>
@import "./SignUpForm.scss";
</style>

<script>
import { mapGetters } from "vuex";

export default {
  name: "SignUpForm",
  computed: {
    ...mapGetters(["signUpErrorMessage"])
  },
  data() {
    return {
      formaData: {
        username: "",
        email: "",
        password: ""
      }
    };
  },
  methods: {
    async validateForm() {
      const isValid = await this.$validator.validate();
      if (isValid) return this.$store.dispatch("signUp", this.formaData);
    },

    onFocus() {
      if (this.signUpErrorMessage) {
        return this.$store.dispatch("clearServerError");
      }
    }
  }
};
</script>
