<script lang="ts" context="module">
	import { assets } from "$app/paths";
	import type { ProgramMetadata } from "../../ProgramManagement";
	import { mdiFireAlert } from "@mdi/js";

	export const rickRollMetadata: ProgramMetadata = {
		programId: "defender",
		title: "Finndows Defender",
		icon: mdiFireAlert,
		canOpen: true,
		renderDefaults: {
			x: "20vw",
			y: "8vh",
			width: "900px",
			height: "700px",
		},
	};
</script>

<video src="{assets}/rick_roll.mp4" loop autoplay />
<p>Source: <a href="https://youtu.be/dQw4w9WgXcQ">YouTube: Rick Astley - Never Gonna Give You Up</a></p>

<style scoped>
	video {
		display: block;
		width: 100%;
	}
</style>
