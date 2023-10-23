<script lang="ts" setup>
import { WindowTitlebar } from "#components";
import { useProgramManager, computed } from "#imports";
import type { ProgramMetadata } from "#imports";
import { useDraggable } from "@vueuse/core";

const programManager = useProgramManager();

const props = defineProps<{
    program: ProgramMetadata;
}>();

const visibility = programManager.getProgramVisibility(props.program.programId);
const stackIndex = programManager.getStackPosition(props.program.programId);

const window = ref();
const titlebar = ref();
const { x: dragX, y: dragY } = useDraggable(window, {
    handle: titlebar,
});
const dynStyle = computed(() => {
    if (visibility.value == "opened")
        return {
            left: dragX.value == 0 ? props.program.renderDefaults.x : `${dragX.value}px`,
            top: dragY.value == 0 ? props.program.renderDefaults.y : `${dragY.value}px`,
            width: props.program.renderDefaults.width,
            height: props.program.renderDefaults.height,
            "z-index": 100 - stackIndex.value,
        };
    else if (visibility.value == "maximized")
        return {
            left: 0,
            top: 0,
            width: "100%",
            height: "100%",
            "z-index": 100 - stackIndex.value,
        };
    else if (visibility.value == "minimized")
        return {
            left: dragX.value == 0 ? props.program.renderDefaults.x : `${dragX.value}px`,
            top: dragY.value == 0 ? props.program.renderDefaults.y : `${dragY.value}px`,
            width: props.program.renderDefaults.width,
            height: "2em",
            "z-index": 100 - stackIndex.value,
        };
});
</script>

<template>
    <div
        v-if="visibility !== 'closed'"
        @mousedown.stop="programManager.raiseWindow(props.program.programId)"
        ref="window"
        class="absolute border-2 border-solid border-shadow"
        :style="dynStyle"
    >
        <WindowTitlebar class="h-[2em]" ref="titlebar" :program="program" />

        <!-- Content -->
        <div
            v-show="visibility != 'minimized'"
            class="border-2 border-solid border-shadow-inverse w-full h-full bg-white overflow-scroll"
            style="max-height: calc(100% - 2em)"
        >
            <slot>Add content to this window in its slot</slot>
        </div>
    </div>
</template>
