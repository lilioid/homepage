<script lang="ts" setup>
import { WindowTitlebar } from "#components";
import { useProgramManager, computed } from "#imports";
import { ProgramMetadata } from "~/composables/programManagement";

const programManager = useProgramManager();

const props = defineProps<{
    program: ProgramMetadata;
}>();

const visibility = programManager.getProgramVisibility(props.program.programId);
const stackIndex = programManager.getStackPosition(props.program.programId);
const dynClasses = computed(() => [
    stackIndex.value == 0 ? "on-top" : null,
    visibility.value == "maximized" ? "maximized" : null,
]);
const dynStyle = computed(() => ({
    left: props.program.renderDefaults.x,
    top: props.program.renderDefaults.y,
    width: props.program.renderDefaults.width,
    height: props.program.renderDefaults.height,
}));
</script>

<template>
    <div
        v-if="visibility !== 'closed'"
        @mousedown.stop="programManager.raiseWindow(props.program.programId)"
        class="absolute border-2 border-solid border-shadow"
        :class="dynClasses"
        :style="dynStyle"
    >
        <WindowTitlebar class="h-[2em]" :program="program" />

        <!-- Content -->
        <div
            class="border-2 border-solid border-shadow-inverse w-full h-full bg-white p-2 overflow-scroll"
            style="max-height: calc(100% - 2em)"
        >
            <slot>Add content to this window in its slot</slot>
        </div>
    </div>
</template>

<style scoped>
.on-top {
    @apply z-50;
}

.maximized {
    @apply w-screen h-screen;
}
</style>
