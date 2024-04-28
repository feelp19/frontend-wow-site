<template>
        <v-stepper v-model="step" :items="items" show-actions>
                <template v-slot:item.1>
                        <br>
                        <v-card class="mx-auto" title="Registro de Usuário">
                                <v-container>
                                        <v-text-field v-model="first" color="primary" label="Primeiro Nome"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="last" color="primary" label="Sobrenome"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="username" color="primary" label="Nome de usuário"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="password" color="primary" label="Senha"
                                                placeholder="Enter your password" variant="underlined"></v-text-field>

                                </v-container>

                                <v-divider></v-divider>

                        </v-card>
                </template>


                <template v-slot:item.2>
                        <br />
                        <h3 class="text-h6">Registro de Email</h3>
                        <v-text-field v-model="email" color="primary" label="Email" variant="underlined"></v-text-field>
                        <v-text-field v-model="email" color="primary" label="Confirmar Email"
                                variant="underlined"></v-text-field>
                        <v-divider></v-divider>
                </template>

                <template v-slot:item.3>
                        <br>
                        <v-card class="mx-auto" title="Confirmar Dados">
                                <v-container>
                                        <v-text-field v-model="first" readonly color="primary" label="Primeiro nome"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="last" readonly color="primary" label="Sobrenome"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="email" readonly color="primary" label="Email"
                                                variant="underlined"></v-text-field>

                                        <v-text-field v-model="username" readonly color="primary" label="Username"
                                        variant="underlined"></v-text-field>

                                        <v-text-field v-model="password" readonly color="primary" label="Password" 
                                        variant="underlined"></v-text-field>

                                        <v-checkbox v-model="terms" color="secondary"
                                                label="Li e aceito os termos"></v-checkbox>
                                </v-container>

                                <v-divider></v-divider>

                                <v-card-actions>
                                        <v-spacer></v-spacer>

                                        <v-btn color="success" v-if="first && last && username && email && password && terms != ''">
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
                step: 1,
                items: [
                        'Nome e Senha',
                        'Email',
                        'Enviar',
                ],
                first: null,
                last: null,
                username: null,
                email: null,
                password: null,
                terms: false,
        }),
}
</script>