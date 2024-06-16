<template>
  <div class="text-center pa-4">
    <v-btn @click="dialog = true">
      Login
    </v-btn>

    <v-dialog
      v-model="dialog"
    >
      <v-card
        image="@/assets/castle-bg.jpg"
        class="pa-6 bd-radius w-25 h-75 mx-auto"
        title="Login"
      >

        <template v-slot:image>
            <v-img class="img-card" gradient="to top right, rgba(18,18,18,.8), rgba(18,18,18,.8)"></v-img>
        </template> 

        <template v-slot:actions>
          <v-btn
            class="ms-auto mt-2"
            type = "submit"
            text="Login"
            @click="dialog = false"
          ></v-btn>
        </template>

        <v-card-item>

            <v-text-field
                class="ma-3 pa-3 bd-radius"
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                color="success"
                hide-details
                required>
            </v-text-field>

            <v-text-field
                class="ma-3 pa-3 bd-radius"
                v-model="password"
                :rules="password"
                label="Password"
                color="success"
                hide-details
                required>
            </v-text-field>

        </v-card-item>

      </v-card>
    </v-dialog>
  </div>
</template>



<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },
  }
</script>

<style scoped>

.bd-radius{
    border-radius: 25px;
}

.img-card{
    filter: blur(3px);
}

</style>