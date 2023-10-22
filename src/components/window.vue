<script lang="ts" setup>
import { WindowTitlebar } from "#components";
import { useProgramManager, computed } from "#imports";
import { ProgramMetadata } from "~/composables/programManagement";
import { useDraggable } from "@vueuse/core";

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

const window = ref();
const titlebar = ref();
const { x: dragX, y: dragY } = useDraggable(window, {
    handle: titlebar,
});
const dynStyle = computed(() => ({
    left: dragX.value == 0 ? props.program.renderDefaults.x : `${dragX.value}px`,
    top: dragY.value == 0 ? props.program.renderDefaults.y : `${dragY.value}px`,
    width: props.program.renderDefaults.width,
    height: props.program.renderDefaults.height,
}));
</script>

<template>
    <div
        v-if="visibility !== 'closed'"
        @mousedown.stop="programManager.raiseWindow(props.program.programId)"
        ref="window"
        class="absolute border-2 border-solid border-shadow"
        :class="dynClasses"
        :style="dynStyle"
    >
        <WindowTitlebar class="h-[2em]" ref="titlebar" :program="program" />

        <!-- Content -->
        <div
            class="border-2 border-solid border-shadow-inverse w-full h-full bg-white p-2 overflow-scroll"
            style="max-height: calc(100% - 2em)"
        >
            <slot>Add content to this window in its slot</slot>
        </div>
    </div>
</template>
