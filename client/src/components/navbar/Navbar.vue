<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        <img src="../../assets/logo.png" width="58" height="58" />
      </a>

      <a
        role="button"
        class="navbar-burger burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/sign-up" class="button btn-primary">
              <strong>Sign Up</strong>
            </router-link>
            <router-link to="/login" class="button is-success is-outlined"
              >Login</router-link
            >
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
export default {
  name: "Navbar"
};
</script>
