<template>
    <div class="login-view">
        <h1>Login View</h1>

        <p>{{ msg }}</p>

        <form @submit.prevent="login">
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" v-model="email" />
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" v-model="password" />
            </div>
            <button type="submit">Login</button>
        </form>

        <p>Don't have an account? <a href="/register">Register here</a>.</p>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const msg = ref('Please enter credentials to log in.');

const email = ref('');
const password = ref('');

async function login() {
    // alert('Login function called with data')
    // alert(`Email: ${email.value}, Password: ${password.value}`);

    try {
        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email.value,
                password: password.value
            })
        });
        console.log('Response from backend:', response);
        if (response.status === 200) {
            msg.value = 'Login successful!';
            const data = await response.json();

            console.log('Data from backend:', data);

            localStorage.setItem('token', data.token);
            localStorage.setItem('user', JSON.stringify(data.user));

            msg.value += ' Redirecting to dashboard...';

            setTimeout(() => {
                if (data.user.role === 'admin') {
                    window.location.href = '/admin/dashboard';
                } else {
                    window.location.href = '/user/dashboard';
                }
            }, 3000);
            
        } else if (response.status === 401) {
            msg.value = 'Login failed. Incorrect email or password.';
        } else {
            msg.value = 'Login failed. Please check your credentials.';
        }
    } catch (error) {
        console.error('Error fetching data from backend:', error);
        msg.value = 'Failed to fetch message from backend.';
    }
};

</script>