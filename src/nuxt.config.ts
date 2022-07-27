import {defineNuxtConfig} from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    alias: {
        "@": "/",
    },
    app: {
        head: {
            meta: [
                {name: "google-site-verification", content: "Cn3fYPQEgI7fqxkxGsiOLMVl8dgmJOYPf_KuE4UsWa0"},
            ]
        },
    },
    telemetry: false,
    typescript: {
        strict: true,
        typeCheck: true,
    }
})
