<script lang="ts" setup>
import "@fontsource/cutive-mono";
import "@fontsource/source-serif-pro";
import "@fontsource/source-sans-pro";
import { useHead, provideProgramManager } from "#imports";

useHead({
    titleTemplate: (siteTitle?: string) =>
        siteTitle ? `${siteTitle} - Finn-Thorben Sell` : "Finn-Thorben Sell",
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
