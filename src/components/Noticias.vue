<template>
    <v-card variant="tonal">
        <ul v-if="dados">
            <li v-for="dado in dados" :key="dado.id">{{ dados.Company }}</li>
        </ul>
    </v-card>
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