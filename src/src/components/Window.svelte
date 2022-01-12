<script lang="ts">
	import SvgIcon from "./SvgIcon.svelte";
	import { mdiWindowClose, mdiWindowMaximize, mdiWindowMinimize, mdiWindowRestore } from "@mdi/js";
	import type { ProgramMetadata } from "../ProgramManagement";
	import { ProgramVisibility, ProgramManager } from "../ProgramManagement";
	import { programState } from "../ProgramManagement";
	import { derived } from "svelte/store";

	export let metadata: ProgramMetadata;

	const programManager = new ProgramManager();
	const state = programState(metadata.programId);
	let maximizeButtonIcon: string;
	$: maximizeButtonIcon =
		$state.visibility === ProgramVisibility.MAXIMIZED ? mdiWindowRestore : mdiWindowMaximize;

	const style = derived(state, (state) => {
		const zIndex = 999 - state.programIndex;

		if (state.visibility === ProgramVisibility.MAXIMIZED) {
			return `--x: 0px; --y: 0px; --z-index: ${zIndex}; --preferred-width: 999vw; --preferred-height: 999vh;`;
		} else {
			return `--x: ${state.placement.x}; --y: ${state.placement.y}; --z-index: ${zIndex}; --preferred-width: ${state.placement.width}; --preferred-height: ${state.placement.height};`;
		}
	});

	function onWindowMouseDown(): void {
		console.log("called");
		programManager.raiseWindow(metadata.programId);
	}
</script>

{#if $state.visibility !== ProgramVisibility.CLOSED}
	<!-- Window wrapper -->
	<div
		on:mousedown={onWindowMouseDown}
		class="window"
		class:on-top={$state.isOnTop}
		class:maximized={$state.visibility === ProgramVisibility.MAXIMIZED}
		style={$style}
	>
		<!-- Titlebar -->
		<div class="titlebar no-select">
			<div class="titlebar-title">{metadata.title}</div>
			<div class="button-container">
				<div
					class="button"
					on:click|stopPropagation={programManager.toggleProgramMinimization(metadata.programId)}
				>
					<SvgIcon size="22" path={mdiWindowMinimize} />
				</div>
				<div
					class="button"
					on:click|stopPropagation={programManager.toggleProgramMaximization(metadata.programId)}
				>
					<SvgIcon size="22" path={maximizeButtonIcon} />
				</div>
				<div
					class="button"
					on:click|stopPropagation={programManager.setProgramVisibility(
						metadata.programId,
						ProgramVisibility.CLOSED,
					)}
				>
					<SvgIcon size="22" path={mdiWindowClose} />
				</div>
			</div>
		</div>

		<!-- Content -->
		<div class="content-container" class:hidden={$state.visibility === ProgramVisibility.MINIMIZED}>
			<slot>Add content to this window in its slot</slot>
		</div>
	</div>
{/if}

<style lang="scss">
	@use "../styles/utils";
	@use "../styles/colors";

	.window {
		position: absolute;
		left: var(--x);
		top: var(--y);
		z-index: var(--z-index);
		@include utils.shadow();

		--titlebar-height: 32px;
		// the complete explorer screen minus x position
		--window-max-width: calc(100vw - var(--x));
		// the complete explorer screen minus y position minus taskbar height
		--window-max-height: calc(100vh - var(--y) - var(--taskbar-height));
		max-width: var(--window-max-width);
		max-height: var(--window-max-height);

		& .titlebar {
			display: flex;
			justify-content: space-between;
			align-items: center;
			background-color: colors.get_color("grey-dark");
			height: var(--titlebar-height);

			& .titlebar-title {
				margin: 4px;
				font-size: large;
				font-weight: lighter;
			}

			& .button-container {
				margin: 0 4px;
				display: flex;
				gap: 3px;

				& .button {
					background-color: colors.get_color("grey-light");
					@include utils.shadow();
				}

				& .button:active {
					@include utils.shadow($inverse: true);
				}
			}
		}

		& .content-container {
			@include utils.shadow($inverse: true);
			background-color: colors.get_color("white");
			padding: 4px;
			overflow: scroll;

			// the same as the containing window minus border (2*2px)
			max-width: min(calc(var(--window-max-width) - 4px), var(--preferred-width));
			// the same as the containing window minus titlebar height minus border (2*2px)
			max-height: min(calc(var(--window-max-height) - var(--titlebar-height) - 4px), var(--preferred-height));
		}
	}

	.window.on-top .titlebar {
		background-image: colors.get_color("titlebar-gradient");

		& .titlebar-title {
			color: colors.get_color("white");
		}
	}

	.window.maximized {
		width: 100%;
		height: 100%;

		& .content-container {
			width: 100%;
			height: 100%;
		}
	}
</style>
