<script setup lang="ts">
import { useHead, useProgramManager, cvMetadata, contactMetadata } from "#imports";
import { Viewport } from "#components";

const description =
    "Personal homepage of Finn Sell, a student at University of Hamburg and software developer and administrator.";
useSeoMeta({
    ogTitle: "Finn Sell",
    twitterCard: "summary_large_image",
    description: description,
    ogDescription: description,
    ogImage: "/screenshot.webp",
    ogImageAlt: "A screenshot showing the personal homepage of Finn Sell",
    ogUrl: "https://ftsell.de",
});

const programManager = useProgramManager();
const route = useRoute();
onMounted(async () => {
    if (route.fullPath == "/") {
        await programManager.setProgramVisibility(contactMetadata.programId, "opened");
        await programManager.setProgramVisibility(cvMetadata.programId, "opened", true);
    }
});
</script>

<template>
    <viewport />
</template>
