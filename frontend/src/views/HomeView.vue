<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <h1>Welcome to MAD2 project</h1>
  <!-- <main>
    <TheWelcome />
  </main> -->

  <p>Don't have an account? <router-link to="/register">Register here</router-link>.</p>
  <p>Already have an account? <router-link to="/login">Login here</router-link>.</p>

  <!-- <TheWelcome /> -->

</template>
