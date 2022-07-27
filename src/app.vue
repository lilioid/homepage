<script lang="ts" setup>
import { useHead } from "#imports";

useHead({
    titleTemplate: (siteTitle?: string) =>
        siteTitle ? `${siteTitle} - Finn-Thorben Sell` : "Finn-Thorben Sell",
});
</script>

<template>
    <div>
        <NuxtPage />
    </div>
</template>
