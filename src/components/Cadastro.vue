<template>
        <v-stepper v-model="step" :items="items" show-actions>
                <template v-slot:item.1>
                        <v-card class="mx-auto" title="Registro de Usuário">
                                <v-container>
                                        <v-text-field v-model="first" color="primary" label="Primeiro Nome"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="last" color="primary" label="Sobrenome"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="last" color="primary" label="Nome de usuário"
                                        variant="underlined"></v-text-field>

                                        <v-text-field v-model="password" color="primary" label="Senha"
                                                placeholder="Enter your password" variant="underlined"></v-text-field>

                                        <v-checkbox v-model="terms" color="secondary"
                                                label="Li e aceito os termos de conduta"></v-checkbox>
                                </v-container>

                                <v-divider></v-divider>

                        </v-card>
                </template>


                <template v-slot:item.2>
                        <br />
                        <h3 class="text-h6">Registro de Email</h3>
                        <v-text-field v-model="email" color="primary" label="Email" variant="underlined"></v-text-field>
                        <v-text-field v-model="email" color="primary" label="Confirmar Email" variant="underlined"></v-text-field>
                </template>

                <template v-slot:item.3>
                        <br>
                                <v-card class="mx-auto" title="Confirmar Dados">
                                        <v-container>
                                                <v-text-field v-model="first" color="primary" label="First name"
                                                        variant="underlined"></v-text-field>

                                                <v-text-field v-model="last" color="primary" label="Last name"
                                                        variant="underlined"></v-text-field>

                                                <v-text-field v-model="email" color="primary" label="Email"
                                                        variant="underlined"></v-text-field>

                                                <v-text-field v-model="password" color="primary" label="Password"
                                                        placeholder="Enter your password"
                                                        variant="underlined"></v-text-field>

                                                <v-checkbox v-model="terms" color="secondary"
                                                        label="I agree to site terms and conditions"></v-checkbox>
                                        </v-container>

                                        <v-divider></v-divider>

                                        <v-card-actions>
                                                <v-spacer></v-spacer>

                                                <v-btn color="success">
                                                        Completar Registro
                                                        <v-icon icon="mdi-chevron-right" end></v-icon>
                                                </v-btn>
                                        </v-card-actions>
                                </v-card>
                </template>
        </v-stepper>
</template>

<script>
export default {
        data: () => ({
                shipping: 0,
                step: 1,
                items: [
                        'Nome e Senha',
                        'Email',
                        'Enviar',
                ],
                first: null,
                last: null,
                email: null,
                password: null,
                terms: false,
        }),

        computed: {
                subtotal() {
                        return this.products.reduce((acc, product) => acc + product.quantity * product.price, 0)
                },
                total() {
                        return this.subtotal + Number(this.shipping ?? 0)
                },
        },
}
</script>