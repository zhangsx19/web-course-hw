import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SuccessView from '../views/SuccessView.vue'
import ChartView from '../views/ChartView.vue'
import store from '../store/index'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/success',
    name: 'success',
    component: SuccessView
  },
  {
    path: '/chart',
    name: 'chart',
    component: ChartView
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
router.beforeEach((to) => {
  if (to.path == "/success" && store.state.user.is_login == false) {
    console.log("re to /");
    return { path: '/' }
  }
  if (to.path == "/" && store.state.user.is_login == true) {
    console.log("re to /success");
    return { path: '/success' }
  }
  return true
})
export default router
