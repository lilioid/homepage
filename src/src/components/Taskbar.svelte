<script lang="ts">
	import SystemTray from "./SystemTray.svelte";
</script>

<div class="shadow taskbar fill">
	<div>
		<slot />
	</div>
	<SystemTray>
		<slot name="SystemTray" />
	</SystemTray>
</div>

<style lang="scss">
	@use "../styles/utils";
	@use "../styles/colors";

	.taskbar {
		background-color: colors.get_color("grey");
		display: flex;
		z-index: 999;
		flex-basis: var(--taskbar-height);
		max-height: var(--taskbar-height);

		& > *:first-child {
			display: flex;
			flex-grow: 1;
			gap: 4px;
		}
	}
</style>
