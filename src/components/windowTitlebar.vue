<script lang="ts" setup>
import { WindowTitlebarButton } from "#components";
import { computed, useProgramManager } from "#imports";
import { ProgramMetadata } from "~/composables/programManagement";
import { mdiWindowMinimize, mdiWindowClose, mdiWindowRestore, mdiWindowMaximize } from "@mdi/js";

const props = defineProps<{
    program: ProgramMetadata;
}>();

const programManager = useProgramManager();
const visibility = programManager.getProgramVisibility(props.program.programId);
const stackIndex = programManager.getStackPosition(props.program.programId);

const maximizeButtonIcon = computed(() =>
    visibility.value != "maximized" ? mdiWindowMaximize : mdiWindowRestore,
);
const dynClasses = computed(() => [stackIndex.value == 0 ? "bg-titlebar" : "bg-grey-dark1"]);
const dynTitleColor = computed(() => (stackIndex.value == 0 ? "text-white" : "text-black"));

async function onMinimizeClicked(): Promise<void> {
    await programManager.setProgramVisibility(
        props.program.programId,
        visibility.value == "minimized" ? "opened" : "minimized",
    );
}

async function onMaximizeClicked(): Promise<void> {
    await programManager.setProgramVisibility(
        props.program.programId,
        visibility.value == "maximized" ? "opened" : "maximized",
    );
}

async function onCloseClicked(): Promise<void> {
    await programManager.setProgramVisibility(props.program.programId, "closed");
}
</script>

<template>
    <div class="flex justify-between items-center select-none" :class="dynClasses">
        <!-- Title -->
        <div class="ml-1 text-2xl font-thin font-serif" :class="dynTitleColor">{{ props.program.title }}</div>

        <!-- Button Container -->
        <div class="mx-2 flex gap-1.5">
            <WindowTitlebarButton :iconPath="mdiWindowMinimize" @click.stop="onMinimizeClicked" />
            <WindowTitlebarButton :iconPath="maximizeButtonIcon" @click.stop="onMaximizeClicked" />
            <WindowTitlebarButton :iconPath="mdiWindowClose" @click.stop="onCloseClicked" />
        </div>
    </div>
</template>

<style scoped>
.bg-titlebar {
    background: linear-gradient(to right, #00007b 0%, #0884ce 100%);
}
</style>
