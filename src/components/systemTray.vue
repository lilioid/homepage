<script lang="ts" setup>
import { Clock } from "#components";
</script>

<template>
    <div class="border-2 border-solid border-shadow-inverse flex items-center gap-2 m-2 px-2">
        <slot />
        <Clock />
    </div>
</template>

<style scoped></style>
