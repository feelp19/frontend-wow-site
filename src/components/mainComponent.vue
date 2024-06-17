<template>
  <v-card class="mx-auto" color="grey-lighten-3">
    <v-layout>
      <v-app-bar color="teal-darken-4" image="@/assets/img-menu.jpg">
        <template v-slot:image>
          <v-img gradient="to top right, rgba(18,18,18,.8), rgba(18,18,18,.8)"></v-img>
        </template>

        <v-app-bar-title>
          <router-link to="/">
            <v-icon icon="mdi-home"></v-icon>
          </router-link>
        </v-app-bar-title>

        <v-spacer></v-spacer>

        <router-link to="/cadastro">
          <v-btn>Cadastro</v-btn>
        </router-link>

        <router-link to="/noticias">
          <v-btn>Noticias</v-btn>
        </router-link>

        <router-link to="/sobre">
          <v-btn>Sobre</v-btn>
        </router-link>

        <router-link to="#">
          <LoginComponent />
        </router-link>
        
        <v-col cols="6" sm="2">
          <v-text-field
            label="pesquisar"
            prepend-inner-icon="mdi-magnify" variant="underlined"
            persistent-hint single-line>
          </v-text-field>
        </v-col>
      </v-app-bar>

      <v-main>

      </v-main>
    </v-layout>
  </v-card>
</template>

<script>

import LoginComponent from '@/components/loginComponent.vue';

data: () => ({
  search: ''
})
</script>