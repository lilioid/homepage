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
