<script context="module" lang="ts">
	import type { ProgramMetadata } from "../ProgramManagement";
	import { mdiMicrosoftWindowsClassic } from "@mdi/js";

	export const startMenuMetadata: ProgramMetadata = {
		programId: "start",
		title: "Start",
		icon: mdiMicrosoftWindowsClassic,
		canOpen: true,
		renderDefaults: {
			x: "",
			y: "",
			width: "",
			height: "",
		},
	};
</script>

<script lang="ts">
	import { ProgramVisibility, programState } from "../ProgramManagement";
	import { randomDogPicture } from "../dog_pictures";
	import { onMount } from "svelte";
	import { browser } from "$app/env";

	const state = programState(startMenuMetadata.programId);

	// prefetch the dog image when the component is mounted
	//  this has the effect of immediately being able to show the image when the start menu is opened because the
	//  image is already cached
	if (browser) {
		onMount(() => {
			randomDogPicture.subscribe((dog) => {
				if (dog) {
					const img = new Image();
					img.src = dog.url;
				}
			});
		});
	}
</script>

{#if $state.visibility !== ProgramVisibility.CLOSED}
	<div class="panel">
		<span class="os-name">Finndows 98</span>
		<div class="dog-container">
			{#if $randomDogPicture}
				<img alt="Random dog" src={$randomDogPicture.url} />
			{/if}
		</div>
	</div>
{/if}

<style lang="scss">
	@use "../styles/utils";
	@use "../styles/colors";

	.panel {
		display: flex;
		position: absolute;
		width: min(24vw, 428px);
		height: min(64vh, 600px);
		bottom: var(--taskbar-height);
		align-items: flex-end;
		gap: 8px;
		z-index: 2000;

		@include utils.shadow();
		background-color: colors.get_color("grey-dark");

		& > * {
			display: inline;
		}

		.os-name {
			color: colors.get_color("grey-light");
			background-color: colors.get_color("grey-dark2");
			height: 100%;
			padding: 4px;
			font-size: large;
			font-weight: bold;
			letter-spacing: 0.6em;
			writing-mode: sideways-lr;
			text-orientation: mixed;
		}

		.dog-container {
			margin-right: 4px;
			flex-grow: 1;

			& > img {
				object-fit: contain;
				background-size: contain;
				max-height: 100%;
				width: 100%;
			}
		}
	}
</style>
