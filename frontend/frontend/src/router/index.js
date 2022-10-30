import { createRouter, createWebHistory } from "vue-router";
import CarEvaluation from "../components/CarEvaluation.vue";
import CarHistory from "@/components/CarHistory";

const routes = [
  {
    path: "/",
    name: "CarEvaluation",
    component: CarEvaluation,
  },
  {
    path: "/history",
    name: "CarHistory",
    component: CarHistory,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
