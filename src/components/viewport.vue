<script lang="ts" setup>
import { Taskbar, Explorer, TaskbarProgram, SystemTrayProgram } from "#components";
import * as programs from "~/programs";
import Window from "~/components/window.vue";
</script>

<template>
    <div class="w-screen h-screen flex flex-col">
        <Explorer class="flex-grow">
            <Window :program="programs.startMenuMetadata" />
            <Window :program="programs.cvMetadata" />
            <Window :program="programs.contactMetadata" />
            <Window :program="programs.codingMetadata" />
            <Window :program="programs.rickRollMetadata" />
            <Window :program="programs.imprintMetadata" />
        </Explorer>
        <Taskbar>
            <template v-slot:default>
                <TaskbarProgram :program="programs.startMenuMetadata" />
                <TaskbarProgram :program="programs.cvMetadata" />
                <TaskbarProgram :program="programs.contactMetadata" />
                <TaskbarProgram :program="programs.codingMetadata" />
            </template>
            <template v-slot:system-tray>
                <SystemTrayProgram :metadata="programs.rickRollMetadata" />
                <SystemTrayProgram :metadata="programs.imprintMetadata" />
            </template>
        </Taskbar>
    </div>
</template>

<style scoped></style>
