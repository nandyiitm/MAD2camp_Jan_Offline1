import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // home page of frontend app
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/TestView.vue'),
    },
    // Below routes are for authentication
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
    },
    // Below routes are for user
    {
      path: '/user/dashboard',
      name: 'user-dashboard',
      component: () => import('../views/User/Dashboard.vue'),
    },
    // Below routes are for admin
    {
      path: '/admin/dashboard',
      name: 'admin-dashboard',
      component: () => import('../views/Admin/Dashboard.vue'),
    }
  ],
})

export default router
