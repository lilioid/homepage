<script>
	import SystemTrayClock from "./SystemTrayClock.svelte";
</script>

<div class="system-tray no-select">
	<slot />
	<SystemTrayClock />
</div>

<style lang="scss">
	@use "../styles/utils";
	@use "../styles/colors";

	.system-tray {
		margin: 4px 6px;
		padding: 4px;
		@include utils.shadow($thickness: 1.5px, $inverse: true);
		display: flex;
		align-items: center;
		gap: 8px;
	}
</style>
