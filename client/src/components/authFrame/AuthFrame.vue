<template>
  <div class="container">
    <div class="content-text">
      Do you need a tool that allows you to track your favorite things ? You are
      in the right place. Login Now!
    </div>

    <div class="auth-wrapper">
      <component :is="children"></component>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthFrame",
  props: {
    children: {
      type: [String, Object],
      default: "div"
    }
  }
};
</script>

<style lang="scss" scoped>
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding-top: 10rem;
}
.content-text {
  color: #36495d;
  font-size: 1.5rem;
}
</style>
