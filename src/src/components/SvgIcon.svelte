<script lang="ts">
	export let size = 24;
	export let path: string;
</script>

<svg width={size} height={size} viewBox="0 0 24 24">
	<path d={path} />
</svg>

<style>
	path {
		fill: currentColor;
	}
</style>
