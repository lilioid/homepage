<script lang="ts" setup>
import { ref } from "#imports";
import { useIntervalFn } from "@vueuse/core";

let time = ref("00:00:00");

// this is used instead of `useNow()` to avoid hydration mismatch
// TODO Improve with useNow() somehow
if (process.client) {
    useIntervalFn(() => {
        time.value = new Date().toLocaleTimeString();
    }, 100);
}
</script>

<template>
    {{ time }}
</template>
