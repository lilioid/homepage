<script context="module" lang="ts">
	import type { ProgramMetadata } from "../../ProgramManagement";
	import { mdiEmail, mdiGithub } from "@mdi/js";
	import SvgIcon from "../SvgIcon.svelte";

	export const contactMetadata: ProgramMetadata = {
		title: "Contact",
		programId: "contact",
		canOpen: true,
		icon: mdiEmail,
		renderDefaults: {
			x: "55vw",
			y: "12vh",
			width: "600px",
			height: "",
		},
	};
</script>

<div>
	<a class="contact-line" href="mailto:contact@finn-thorben.me">
		<SvgIcon path={mdiEmail} />
		<span>contact@finn-thorben.me</span>
	</a>

	<a class="contact-line" href="https://github.com/ftsell">
		<SvgIcon path={mdiGithub} />
		<span>ftsell</span>
	</a>

	<p>
		If you are using PGP and deem my website a valid method of identification, my public key is available for
		download from
		<a href="https://keys.openpgp.org/search?q=E28C78646FA4F70B30422385A78A03C25A3A3825" target="_blank"
			>keys.openpgp.org</a
		>
		or directly from <a rel="external" href="/finn-thorben_sell.gpg">here</a>.<br />
		Its fingerprint is:
	</p>

	<code>E28C78646FA4F70B30422385A78A03C25A3A3825</code>
</div>

<style lang="scss">
	@use "../../styles/colors";
	@use "../../styles/utils";

	.contact-line {
		width: fit-content;
		display: flex;
		align-content: baseline;
		margin-bottom: 12px;

		& > :first-child {
			color: colors.get_color("black");
			margin-right: 6px;
		}
	}

	code {
		display: block;
		padding: 8px;
		font-family: "Bitstream Vera Sans Mono", "monospace";
		margin-top: 16px;
		background-color: colors.get_color("grey-light");
	}
</style>
