import { defineNuxtConfig } from "nuxt/config";

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    telemetry: false,
    typescript: {
        strict: true,
        typeCheck: true,
    },
    modules: ["@nuxtjs/tailwindcss"],
});
