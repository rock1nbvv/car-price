<script>
import MyHeader from "./components/Header.vue";

export default {
  components: {
    MyHeader,
  },
};
</script>

<template>
  <MyHeader />
  <router-view />
</template>

<style>
nav a.router-link-exact-active {
  color: #42b983;
}
</style>
