<script lang="ts" setup>
import { useProgramManager } from "#imports";
import { ProgramMetadata } from "~/composables/programManagement";

const programManager = useProgramManager();

const props = defineProps<{
    program: ProgramMetadata;
}>();

const visibility = programManager.getProgramVisibility(props.program.programId);
</script>

<template>
    <div v-if="visibility !== 'closed'">
        <!-- Titlebar -->
        <div>
            <div>{{ program.title }}</div>
        </div>

        <!-- Content -->
        <div>
            <slot>Add content to this window in its slot</slot>
        </div>
    </div>
</template>
