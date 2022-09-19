<script lang="ts" setup>
import { Taskbar, Explorer, TaskbarProgram } from "#components";
import { cvMetadata } from "~/programs";
</script>

<template>
    <div class="w-screen h-screen flex flex-col">
        <explorer class="flex-grow" />
        <taskbar>
            <taskbar-program :program="cvMetadata" />
        </taskbar>
    </div>
</template>

<style scoped></style>
