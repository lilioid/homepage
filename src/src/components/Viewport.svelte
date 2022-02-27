<script lang="ts">
	import Window from "./Window.svelte";
	import Explorer from "./Explorer.svelte";
	import { setContext } from "svelte";
	import { CTX_PROGRAM_METADATAS } from "../ProgramManagement";
	import { cvMetadata } from "./windows/Cv.svelte";
	import CvContent from "./windows/Cv.svelte";
	import { contactMetadata } from "./windows/Contact.svelte";
	import ContactContent from "./windows/Contact.svelte";
	import Taskbar from "./Taskbar.svelte";
	import TaskbarProgram from "./TaskbarProgram.svelte";
	import SystemTrayProgram from "./SystemTrayProgram.svelte";
	import ImprintContent from "./windows/Imprint.svelte";
	import { imprintMetadata } from "./windows/Imprint.svelte";
	import RickRollContent from "./windows/RickRoll.svelte";
	import { rickRollMetadata } from "./windows/RickRoll.svelte";
	import CodingContent from "./windows/Coding.svelte";
	import { codingMetadata } from "./windows/Coding.svelte";
	import StartMenu, { startMenuMetadata } from "./StartMenu.svelte";

	setContext(CTX_PROGRAM_METADATAS, [
		startMenuMetadata,
		cvMetadata,
		contactMetadata,
		imprintMetadata,
		rickRollMetadata,
		codingMetadata,
	]);
</script>

<div class="split-container fill non-mobile">
	<Explorer>
		<Window metadata={cvMetadata}>
			<CvContent />
		</Window>
		<Window metadata={contactMetadata}>
			<ContactContent />
		</Window>
		<Window metadata={imprintMetadata}>
			<ImprintContent />
		</Window>
		<Window metadata={rickRollMetadata}>
			<RickRollContent />
		</Window>
		<Window metadata={codingMetadata}>
			<CodingContent />
		</Window>
		<StartMenu />
	</Explorer>
	<Taskbar>
		<svelte:fragment>
			<TaskbarProgram metadata={startMenuMetadata} />
			<TaskbarProgram metadata={cvMetadata} />
			<TaskbarProgram metadata={contactMetadata} />
			<TaskbarProgram metadata={codingMetadata} />
		</svelte:fragment>
		<svelte:fragment slot="SystemTray">
			<SystemTrayProgram metadata={rickRollMetadata} />
			<SystemTrayProgram metadata={imprintMetadata} />
		</svelte:fragment>
	</Taskbar>
</div>

<style lang="scss">
	@use "../styles/utils";

	.split-container {
		display: flex;
		flex-direction: column;
		--taskbar-height: 48px;
	}
</style>
