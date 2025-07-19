// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  telemetry: false,
  devtools: {enabled: false},
  modules: [
    "@nuxt/fonts",
  ],
  app: {
    head: {
      link: [
        {rel: "external me", href: "https://chaos.social/@lilly"},
      ],
      htmlAttrs: {
        lang: "en",
      },
    },
  },
  vite: {
    plugins: [tailwindcss(),],
    vue: {
      features: {
        optionsAPI: false,
      }
    }
  },
});
