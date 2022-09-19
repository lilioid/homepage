<script lang="ts" setup>
import { ProgramMetadata, useProgramManager } from "~/composables/programManagement";
import { SvgIcon } from "#components";

const programManager = useProgramManager();

const props = defineProps<{
    metadata: ProgramMetadata;
}>();

async function onClick(): Promise<void> {
    if (programManager.getProgramVisibility(props.metadata.programId) === "closed") {
        await programManager.setProgramVisibility(props.metadata.programId, "opened");
    } else {
        await programManager.setProgramVisibility(props.metadata.programId, "closed");
    }
}
</script>

<template>
    <SvgIcon :path="props.metadata.icon" @click.stop="onClick" />
</template>

<style scoped></style>
