export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Finn-Thorben Sell - Student B.Sc Computer Science',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'google-site-verification', content: 'Cn3fYPQEgI7fqxkxGsiOLMVl8dgmJOYPf_KuE4UsWa0' },
      { hid: 'description', name: 'description', content: 'I am Finn-Thorben Sell. I am a student at the University of Hamburg pursuing my Bachelor of Science degree in Computer Science.' }
    ],
    link: [
      // { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build'
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
  ],

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    transpile: ['pixelflut-client']
  },

  // What type of application is built (https://nuxtjs.org/docs/2.x/configuration-glossary/configuration-target)
  target: 'static',

  // Disable telemetry reporting
  telemetry: false
}
