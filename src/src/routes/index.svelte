<script context="module" lang="ts">
	import type { LoadInput, LoadOutput } from "@sveltejs/kit";
	import { browser } from "$app/env";

	let isInitialNavigation = true;

	export function load({ url }: LoadInput): LoadOutput {
		if (!browser || !isInitialNavigation) {
			return {};
		}

		isInitialNavigation = false;
		if (url.searchParams.toString() !== "") {
			return {};
		}

		return {
			status: 303,
			redirect: `${url.href}?cv=opened&cvi=2&contact=opened&contacti=1`,
		};
	}
</script>

<script lang="ts">
	import Viewport from "../components/Viewport.svelte";
	import Bluescreen from "../components/Bluescreen.svelte";
</script>

<svelte:head>
	<title>Finn-Thorben Sell – Student M.Sc Computer Science</title>
	<meta
		name="description"
		data-hid="description"
		content="I am Finn-Thorben Sell. I am a student at the University of Hamburg pursuing my Master of Science degree in Computer Science."
	/>
	<link rel="canonical" href="https://finn-thorben.me/" />
</svelte:head>

<div class="fullscreen">
	<Viewport />
	<Bluescreen />
</div>

<style>
	.fullscreen {
		top: 0;
		left: 0;
		position: absolute;
		height: 100vh;
		width: 100vw;
	}
</style>
