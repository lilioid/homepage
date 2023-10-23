<script lang="ts" setup>
import { Pixelflut as PixelflutComponent } from "#components";

useSeoMeta({
    title: "Pixelflut",
    description: "Live-Viewer for pixelflut, a pixel drawing game fro programmmers",
    ogImage: "/pixelflut_example.webp",
    twitterCard: "app",
});
</script>

<template>
    <pixelflut-component />
</template>
