import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UploadView from '../views/UploadView.vue'
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView
  },
  {
    path: "/upload",
    name: "upload",
    component: UploadView
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
