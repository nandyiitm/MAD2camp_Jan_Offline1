<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <!-- <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/test">Test</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </nav>
    </div>
  </header> -->

  <RouterView /> <!-- This is where the matched component will be rendered -->

</template>

<style scoped>

</style>
