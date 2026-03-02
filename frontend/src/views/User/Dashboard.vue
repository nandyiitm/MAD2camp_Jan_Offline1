<template>
    <h1>User Dashboard</h1>

    <button @click="logout">Logout</button>

    <!-- import all user pages intho this!!! -->

</template>

<script setup>
import { ref, onMounted } from 'vue';

onMounted(() => {
    const token = localStorage.getItem('token');
    const user = JSON.parse(localStorage.getItem('user'));

    if (!token || !user) {
        alert('You are not logged in. Please log in.');
        window.location.href = '/login';
    } else {
        console.log('User data from localStorage:', user);
    }
});

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/login';
}

</script>
