import { http } from '@/services/api'

export default {
    listarDados: () => {
        return http.get(`restaurantes`)
    }
}