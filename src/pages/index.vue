<script setup lang="ts">
import { useHead } from "#imports";
import { Viewport } from "#components";

useHead({
    meta: [
        {
            name: "description",
            "data-hid": "description",
            content:
                "I am Finn-Thorben Sell. I am a student at the University of Hamburg pursuing my Master of Science degree in Computer Science.",
        },
    ],
});
</script>

<template>
    <viewport />
</template>
