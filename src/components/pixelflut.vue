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
    <div>
        <h3 class="text-xl my-2">Instructions</h3>
        <p>
            Pixelflut is intended to be played via bots that connect to a pixelflut server (e.g.
            <code class="font-mono">tcp://ftsell.de:9876</code>) which are then able to set individual pixels
            on the canvas.
        </p>
        <p>
            The server provides a detailed explanation of the protocol as a response to a
            <code class="font-mono">HELP\n</code> command.<br />
            Generally speaking though, commands to the server are separated by line breaks (<code
                class="font-mono"
                >\n</code
            >) with the most common command being <code class="font-mono">PX $X $Y #$COLOR\n</code> to set the
            pixel at coordinates X,Y to a specific RGB color (in hex notation).
        </p>
        <h3 class="text-xl my-2">Live Canvas</h3>
        <p>
            Below is the live canvas of the pixelflut server located on
            <code class="font-mono">ftsell.de:9876</code>
        </p>
        <canvas ref="canvas" width="800" height="600" />
    </div>
</template>
