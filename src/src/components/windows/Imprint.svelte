<script context="module" lang="ts">
	import type { ProgramMetadata } from "../../ProgramManagement";
	import { mdiGavel } from "@mdi/js";

	export const imprintMetadata: ProgramMetadata = {
		programId: "imprint",
		title: "Imprint",
		canOpen: true,
		icon: mdiGavel,
		renderDefaults: {
			x: "60vw",
			y: "55vh",
			width: "450px",
			height: "300px",
		},
	};
</script>

<h2>Information according to §5 TMG</h2>
<p>
	This is my private - non commercial - website therefore an imprint containing my private address and phone
	number is not necessary as specified in §5 (1) of the german TMG.
</p>
<p>
	If you want to contact me you can choose your preferred network or method by clicking on <i>Contact</i> in the
	grey bar at the bottom.
</p>
