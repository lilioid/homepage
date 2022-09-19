<script lang="ts" setup>
import { SvgIcon } from "#components";
import { ProgramMetadata } from "~/composables/programManagement";
import { computed } from "#imports";

const props = defineProps<{
    program: ProgramMetadata;
}>();

const dynClasses = computed(() => [
    "shadow-default",
    props.program.taskbarSize === "normal" ? "max-w-[200px]" : "max-w-[100px]",
]);
</script>

<template>
    <div class="flex items-center grow bg-grey-normal px-1 py-1.5 m-2" :class="dynClasses">
        <svg-icon :path="props.program.icon" />
        <span>{{ program.title }}</span>
    </div>
</template>

<style scoped></style>
