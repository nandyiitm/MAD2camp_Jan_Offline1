<template>
    <div class="register-view">
        <h1>Register View</h1>

        <p>{{ msg }}</p>

        <form @submit.prevent="register">
            <div>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" v-model="name" />
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" v-model="email" />
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" v-model="password" />
            </div>
            <button type="submit">Register</button>
        </form>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const msg = ref('Please enter infomration to create account.');

const name = ref('');
const email = ref('');
const password = ref('');

async function register() {
    // alert('Register function called with data')
    // alert(`Email: ${email.value}, Password: ${password.value}`);

    try {
        const response = await fetch('http://localhost:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name.value,
                email: email.value,
                password: password.value
            })
        });
        console.log('Response from backend:', response);
        if (response.status === 201) {
            msg.value = 'Register successful!';
            const data = await response.json();

            console.log('Data from backend:', data);

            msg.value += ' Redirecting to login page, please login...';

            setTimeout(() => {
                window.location.href = '/login';
            }, 3000);
            
        } else if (response.status === 401) {
            msg.value = 'Register failed. Incorrect email or password.';
        } else {
            msg.value = 'Register failed. Please check your credentials.';
        }
    } catch (error) {
        console.error('Error fetching data from backend:', error);
        msg.value = 'Failed to fetch message from backend.';
    }
};

</script>