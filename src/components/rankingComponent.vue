<template>
    <v-container>
      <v-row>
        <v-col cols="4">
          <v-card class="pa-4">
            <v-card-title>
              Melhores Jogadores do Servidor
            </v-card-title>
            <v-divider></v-divider>
            <v-card-item>
              <v-simple-table fixed-header class="h-100">
                <thead>
                  <tr>
                    <th class="text-left">Nome</th>
                    <th class="text-left">Pontos</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="item in desserts" :key="item.name">
                    <td>{{ item.name }}</td>
                    <td>{{ item.points }}</td>
                  </tr>
                </tbody>
              </v-simple-table>
            </v-card-item>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  

<style scoped>
.pa {
  padding: 16px;
}
.mt-4 {
  margin-top: 16px;
}
.text-left {
  text-align: left;
}
</style>


<script>
  export default {
    data () {
      return {
        desserts: [ //array que contém os jogadores
          {
            name: 'Feelp19 - Irmaoslokko', 
            points: 1999999,
          },
          {
            name: 'ManyGold19 - Irmaoslokko',
            points: 1999999,
          },
        ],
      }
    },
  }
</script>