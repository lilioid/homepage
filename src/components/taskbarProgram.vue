<script lang="ts" setup>
import { SvgIcon } from "#components";
import { ProgramMetadata } from "~/composables/programManagement";
import { computed } from "#imports";

const props = defineProps<{
    program: ProgramMetadata;
}>();

const shadowClasses = computed(() => "shadow-default");
</script>

<template>
    <div class="flex max-w-[200px] grow bg-grey-normal px-1 py-1.5 m-2" :class="shadowClasses">
        <svg-icon :path="props.program.icon" />
        <span>{{ program.title }}</span>
    </div>
</template>

<style scoped></style>
