import { createRouter, createWebHistory } from "vue-router";
import CarEvaluation from "../components/CarEvaluation.vue";

const routes = [
  {
    path: "/",
    name: "CarEvaluation",
    component: CarEvaluation,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
