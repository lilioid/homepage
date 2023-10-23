<script setup lang="ts">
import { useHead, useProgramManager, cvMetadata, contactMetadata } from "#imports";
import { Viewport } from "#components";

useHead({
    meta: [
        {
            name: "description",
            "data-hid": "description",
            content:
                "I am Finn Sell. I am a student at the University of Hamburg pursuing my Master of Science degree in Computer Science.",
        },
    ],
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
