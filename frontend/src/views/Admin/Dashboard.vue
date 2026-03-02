<template>
    <div class="dashboard">
        <div class="card">
            <h1 class="title">Admin Dashboard</h1>

            <h2 class="subtitle">Users List</h2>

            <ul class="user-list">
                <li v-for="user in users" :key="user.id" class="user-card">
                    <div class="user-info">
                        <div class="name">{{ user.name }}</div>
                        <div class="email">{{ user.email }}</div>
                    </div>
                    <div class="role" :class="user.role">
                        {{ user.role }}
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
/* YOUR ORIGINAL SCRIPT — UNCHANGED */
import { ref, onMounted } from 'vue';

const users = ref([
    {
        id: 1,
        name: 'John Doe',
        email: 'jhn@gmail.com',
        role: 'user'
    },
    {
        id: 2,
        name: 'Jane Smith',
        email: 'jane@gmail.com',
        role: 'user'
    },
    {
        id: 3,
        name: 'Alice Johnson',
        email: 'alice@gmail.com',
        role: 'admin'
    }
]);

onMounted(() => {
    const token = localStorage.getItem('token');
    const user = JSON.parse(localStorage.getItem('user'));

    if (!token || !user) {
        alert('You are not logged in. Please log in.');
        window.location.href = '/login';
    } else {
        console.log('User data from localStorage:', user);
        if (user.role !== 'admin') {
            alert('You do not have permission to access this page.');
            window.location.href = '/user/dashboard';
        }
    }
});

function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/login';
}
</script>

<style scoped>
.dashboard {
    min-height: 100vh;
    background: linear-gradient(135deg, #1e293b, #a6afc3);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 40px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
    background: #ffffff;
    width: 100%;
    max-width: 700px;
    border-radius: 16px;
    padding: 40px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
}

.title {
    font-size: 32px;
    margin-bottom: 10px;
    color: #1e293b;
}

.subtitle {
    font-size: 20px;
    margin-bottom: 25px;
    color: #64748b;
}

.user-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.user-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 20px;
    margin-bottom: 15px;
    border-radius: 12px;
    background: #f8fafc;
    transition: all 0.2s ease;
}

.user-card:hover {
    transform: translateY(-3px);
    background: #f1f5f9;
}

.user-info .name {
    font-weight: 600;
    color: #0f172a;
}

.user-info .email {
    font-size: 14px;
    color: #64748b;
}

.role {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
}

.role.admin {
    background-color: #dcfce7;
    color: #166534;
}

.role.user {
    background-color: #e0f2fe;
    color: #075985;
}
</style>