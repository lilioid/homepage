<script lang="ts">
	import SvgIcon from "./SvgIcon.svelte";
	import type { ProgramMetadata } from "../ProgramManagement";
	import { ProgramManager, programState, ProgramVisibility } from "../ProgramManagement";

	export let metadata: ProgramMetadata;

	const state = programState(metadata.programId);
	const programManager = new ProgramManager();

	function onClick(): void {
		if ($state.visibility === ProgramVisibility.CLOSED) {
			programManager.setProgramVisibility(metadata.programId, ProgramVisibility.OPENED);
		} else if (!$state.isOnTop) {
			programManager.raiseWindow(metadata.programId);
		}
	}
</script>

<div class="system-tray-program" on:click={onClick}>
	<SvgIcon path={metadata.icon} />
</div>

<style lang="scss">
	@use "../styles/utils";
	@use "../styles/colors";

	.system-tray-program {
		border: 2px colors.get_color("grey") solid;
	}
	.system-tray-program:active:not(.non-interactive) {
		@include utils.shadow($inverse: true);
		border-style: dotted;
	}
</style>
