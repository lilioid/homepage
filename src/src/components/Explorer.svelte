<div class="explorer">
	<slot />
</div>

<style lang="scss">
	@use "../styles/utils";
	@use "../styles/colors";

	.explorer {
		background-color: colors.get_color("cyan");
		flex-basis: 90%;
		flex-grow: 1;
		flex-shrink: 1;
	}
</style>
