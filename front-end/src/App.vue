<script setup>
import { RouterLink, RouterView } from 'vue-router'
//import HelloWorld from './components/HelloWorld.vue'

</script>
<template>
  <ul class="nav justify-content-center">
  <li class="nav-item">
    <RouterLink to="/" class="nav-link active" aria-current="page">Active</RouterLink>
  </li>
  <li class="nav-item">
    <RouterLink to="/about" class="nav-link">About</RouterLink>
  </li>
  <li class="nav-item">
    <RouterLink to="/profile" class="nav-link">Profile</RouterLink>
  </li>
  <!--li class="nav-item">
    <RouterLink to="/login" class="nav-link">Log In</RouterLink>
  </li-->
  <li class="nav-item">
    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
  </li>
</ul>
  <RouterView />

    <p class="text-left">Left</p>
    <p class="text-center">Center</p>
    <p class="text-right">Right</p>
</template>

<style scoped>
.nav {
  background-color: #e3f2fd;
}
.nav-item {
  color: rgb(185, 149, 29);
}
</style>

