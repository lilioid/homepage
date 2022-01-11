<script lang="ts">
	import { beforeUpdate, createEventDispatcher, onDestroy } from "svelte";
	import { browser } from "$app/env";
	import { PixelflutClient } from "pixelflut-client";

	let canvas: HTMLCanvasElement;
	let pixelflutClient: PixelflutClient;
	const dispatch = createEventDispatcher();

	if (browser) {
		beforeUpdate(() => {
			if (canvas && !pixelflutClient) {
				pixelflutClient = new PixelflutClient("wss://finn-thorben.me/pixelflut.sock", canvas, false);
				pixelflutClient.connect().then(() => {
					dispatch("sizeReceived", { width: pixelflutClient.width, height: pixelflutClient.height });
				});
			}
		});

		onDestroy(() => {
			if (pixelflutClient && pixelflutClient.isConnected()) {
				pixelflutClient.disconnect();
			}
		});
	}
</script>

<canvas bind:this={canvas} width="800" height="600" />
