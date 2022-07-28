<script lang="ts" setup>
const props = withDefaults(
    defineProps<{
        size?: number;
        path: string;
    }>(),
    {
        size: 24,
    }
);
</script>

<template>
    <svg :width="props.size" :height="props.size" viewBox="0 0 24 24">
        <path class="fill-current" :d="props.path" />
    </svg>
</template>

<style scoped></style>
