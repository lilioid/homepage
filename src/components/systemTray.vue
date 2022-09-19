<script lang="ts" setup>
import { Clock } from "#components";
</script>

<template>
    <div class="shadow-inverse flex items-center gap-3 m-2 px-2">
        <slot />
        <Clock />
    </div>
</template>

<style scoped></style>
