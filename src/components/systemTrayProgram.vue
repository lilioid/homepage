<script lang="ts" setup>
import { ProgramMetadata } from "~/composables/programManagement";
import { SvgIcon } from "#components";

const props = defineProps<{
    metadata: ProgramMetadata;
}>();

function onClick(): void {
    console.error("Could not open program because I have no program manager");
}
</script>

<template>
    <SvgIcon :path="props.metadata.icon" />
</template>

<style scoped></style>
