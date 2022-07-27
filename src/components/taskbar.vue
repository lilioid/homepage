<script lang="ts" setup>
import { SystemTray } from "#components";
</script>

<template>
    <div>
        <div>
            <slot />
        </div>
        <system-tray>
            <slot name="system-tray" />
        </system-tray>
    </div>
</template>

<style scoped></style>
