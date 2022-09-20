<script lang="ts" setup>
import { ProgramMetadata, useProgramManager } from "~/composables/programManagement";
import { SvgIcon } from "#components";

const programManager = useProgramManager();

const props = defineProps<{
    metadata: ProgramMetadata;
}>();

async function onClick(): Promise<void> {
    if (programManager.getProgramVisibility(props.metadata.programId).value === "closed") {
        await programManager.setProgramVisibility(props.metadata.programId, "opened", true);
    } else {
        if (programManager.getStackPosition(props.metadata.programId).value === 0) {
            await programManager.setProgramVisibility(props.metadata.programId, "closed");
        } else {
            await programManager.raiseWindow(props.metadata.programId);
        }
    }
}
</script>

<template>
    <SvgIcon class="active:shadow-inverse" :path="props.metadata.icon" @click.stop="onClick" />
</template>

<style scoped></style>
