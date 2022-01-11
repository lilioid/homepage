<script lang="ts">
	import SvgIcon from "./SvgIcon.svelte";
	import type { ProgramMetadata } from "../ProgramManagement";
	import { ProgramManager, programState, ProgramVisibility } from "../ProgramManagement";

	export let metadata: ProgramMetadata;

	const state = programState(metadata.programId);
	const programManager = new ProgramManager();

	let shadowCssClass;
	$: shadowCssClass = $state.visibility === ProgramVisibility.CLOSED ? "shadow" : "shadow-inverse";

	function onClickProgram(): void {
		if ($state.visibility === ProgramVisibility.CLOSED) {
			programManager.setProgramVisibility(metadata.programId, ProgramVisibility.OPENED);
		} else if (!$state.isOnTop) {
			programManager.raiseWindow(metadata.programId);
		} else {
			programManager.setProgramVisibility(metadata.programId, ProgramVisibility.CLOSED);
		}
	}
</script>

<div class="taskbar-program no-select {shadowCssClass}" role="button" on:click={onClickProgram}>
	<SvgIcon path={metadata.icon} />
	<span>{metadata.title}</span>
</div>

<style lang="scss">
	@use "../styles/utils";
	@use "../styles/colors";

	.taskbar-program {
		max-width: 164px;
		background-color: colors.get_color("grey");
		margin: 3px 5px;
		padding: 2px 4px;
		display: flex;
		align-items: center;
		flex-grow: 1;

		&:first-child {
			max-width: 96px;
		}

		& > :first-child {
			margin-right: 6px;
		}
	}
</style>
