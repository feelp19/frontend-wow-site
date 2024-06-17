/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from "vue-router/auto";
import mainComponent from "@/components/mainComponent.vue";
import Cadastro from "@/components/Cadastro.vue"
import Noticias from "@/components/Noticias.vue"
import Sobre from "@/components/Sobre.vue"

const routes = [
  {
    path: "/",
    component: mainComponent,
  },
  {
    path: "/cadastro",
    component: Cadastro
  },
  {
    path:"/noticias",
    component: Noticias
  },
  {
    path:"/sobre",
    component: Sobre
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
