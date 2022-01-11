<script lang="ts">
	import { onMount, onDestroy } from "svelte";
	import { browser } from "$app/env";

	let time = new Date().toLocaleTimeString();

	/* eslint-disable @typescript-eslint/no-explicit-any */
	let intervalId: any;

	if (browser) {
		onMount(() => {
			intervalId = setInterval(() => {
				time = new Date().toLocaleTimeString();
			}, 100);
		});
		onDestroy(() => {
			clearInterval(intervalId);
		});
	}
</script>

<div class="non-interactive">
	{time}
</div>

<style lang="scss">
	* {
		font-family: "Bitstream Vera Sans Mono", "monospace";
	}
</style>
