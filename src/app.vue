<script lang="ts" setup>
import "@fontsource/cutive-mono";
import "@fontsource/source-serif-pro";
import "@fontsource/source-sans-pro";
import { useHead, provideProgramManager } from "#imports";

useSeoMeta({
    colorScheme: "only light",
    themeColor: "#007B7BFF",
    referrer: "no-referrer",
    googleSiteVerification: "Cn3fYPQEgI7fqxkxGsiOLMVl8dgmJOYPf_KuE4UsWa0",
});
useHead({
    titleTemplate: (siteTitle?: string) => (siteTitle ? `${siteTitle} - Finn Sell` : "Finn Sell"),
    htmlAttrs: {
        lang: "en",
    },
    link: [
        {
            rel: "icon",
            type: "image/webp",
            href: "/poly_fox.webp",
        },
    ],
});

provideProgramManager();
</script>

<template>
    <div>
        <NuxtPage />
    </div>
</template>

<style>
html {
    font-family: "Bitstream Vera Serif", "Source Sans Pro", "-apple-system", "BlinkMacSystemFont", "Segoe UI",
        "Roboto", "Helvetica Neue", "Arial", "sans-serif";
    font-size: 16px;
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
}

body {
    overflow: hidden;
}
</style>
