<script lang="ts" setup>
import { SvgIcon } from "#components";
import { ProgramMetadata, useProgramManager } from "~/composables/programManagement";
import { computed } from "#imports";

const programManager = useProgramManager();

const props = defineProps<{
    program: ProgramMetadata;
}>();

const dynClasses = computed(() => [
    programManager.getProgramVisibility(props.program.programId).value === "closed"
        ? "border-shadow"
        : "border-shadow-inverse",
    props.program.taskbarSize === "normal" ? "max-w-[200px]" : "max-w-[100px]",
]);

async function onClick(): Promise<void> {
    if (programManager.getProgramVisibility(props.program.programId).value === "closed") {
        await programManager.setProgramVisibility(props.program.programId, "opened", true);
    } else {
        if (programManager.getStackPosition(props.program.programId).value === 0) {
            await programManager.setProgramVisibility(props.program.programId, "closed");
        } else {
            await programManager.raiseWindow(props.program.programId);
        }
    }
}
</script>

<template>
    <div
        class="flex items-center grow bg-grey-normal px-1 py-1.5 m-2 select-none border-2 border-solid"
        :class="dynClasses"
        @click.stop="onClick"
    >
        <svg-icon :path="props.program.icon" />
        <span>{{ program.title }}</span>
    </div>
</template>

<style scoped></style>
