<template>
    <v-card variant="tonal">
        <ul v-if="dados">
            <li v-for="dado in dados" :key="dado.id">{{ dados.Company }}</li>
        </ul>
    </v-card>
        <v-col cols="12" md="12">
            <v-card 
            class="pa-4 ma-4"
            variant="outlined">
            
            <v-card-item>
                <v-icon icon="mdi-information"></v-icon>
                <v-card-title class="mt-4"><bold>Noticias do dia</bold></v-card-title>
                    <v-card-subtitle>Noticias Fresquinhas do WoW</v-card-subtitle>
            </v-card-item>
            <v-icon></v-icon>
            <v-card-text class="bg-surface-light pt-4">"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam"
            </v-card-text>
            </v-card>
        </v-col>

</template>

<script>
import Dados from '@/services/dados'

    export default {
        data(){
            return {
                dados: []
            }
        },
        mounted() {
            Dados.listarDados().then((response) => {
                console.log(response.data)
                this.dados = response.data
            })
        },
    }
</script>