<script lang="ts" setup>
import { Taskbar, Explorer, TaskbarProgram, SystemTrayProgram, Window } from "#components";

import * as programs from "~/components/utils/programs";
</script>

<template>
    <div class="w-screen h-screen flex flex-col">
        <Explorer class="flex-grow">
            <Window :program="programs.startMenuMetadata"></Window>
            <Window :program="programs.cvMetadata">
                <WindowsCv />
            </Window>
            <Window :program="programs.contactMetadata">
                <WindowsContact />
            </Window>
            <Window :program="programs.codingMetadata"></Window>
            <Window :program="programs.rickRollMetadata">
                <WindowsDefender />
            </Window>
            <Window :program="programs.imprintMetadata">
                <WindowsImprint />
            </Window>
        </Explorer>
        <Taskbar>
            <template v-slot:default>
                <TaskbarProgram :program="programs.startMenuMetadata" />
                <TaskbarProgram :program="programs.cvMetadata" />
                <TaskbarProgram :program="programs.contactMetadata" />
                <TaskbarProgram :program="programs.codingMetadata" />
            </template>
            <template v-slot:system-tray>
                <WidgetEyes />
                <SystemTrayProgram :metadata="programs.rickRollMetadata" />
                <SystemTrayProgram :metadata="programs.imprintMetadata" />
                <WidgetClock />
            </template>
        </Taskbar>
    </div>
</template>
