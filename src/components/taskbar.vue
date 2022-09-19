<script lang="ts" setup>
import { SystemTray } from "#components";
</script>

<template>
    <div class="bg-grey-normal z-50 flex gap-1">
        <slot />
        <div class="flex-grow" />
        <system-tray>
            <slot name="system-tray" />
        </system-tray>
    </div>
</template>

<style scoped></style>
