<script lang="ts" setup>
import { onBeforeUnmount, onMounted, ref } from "#imports";
import { PixelflutClient } from "pixelflut-client";

const canvas = ref<HTMLCanvasElement>();
let pixelflutClient: PixelflutClient;

const emit = defineEmits<{
    (e: "sizeReceived", width: number, height: number): void;
    (e: "connected"): void;
    (e: "disconnected"): void;
}>();

if (!process.server) {
    onMounted(async () => {
        pixelflutClient = new PixelflutClient("wss://finn-thorben.me/pixelflut.sock", canvas.value!, false);
        await pixelflutClient.connect();
        emit("connected");
        emit("sizeReceived", pixelflutClient.width, pixelflutClient.height);
    });

    onBeforeUnmount(async () => {
        if (pixelflutClient && pixelflutClient.isConnected()) {
            pixelflutClient.disconnect();
            emit("disconnected");
        }
    });
}
</script>

<template>
    <canvas ref="canvas" width="800" height="600" />
</template>

<style scoped></style>
