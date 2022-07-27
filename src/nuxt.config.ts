import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    alias: {
        "@": "/",
    },
    app: {
        head: {
            title: "Finn-Thorben Sell"
        }
    },
    telemetry: false,
    typescript: {
        strict: true,
        typeCheck: true,
    }
})
