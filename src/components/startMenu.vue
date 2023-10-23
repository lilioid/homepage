<script setup lang="ts">
import { useDogPicture, useProgramManager, startMenuMetadata } from "#imports";

const programManager = useProgramManager();
const { data: dog, status: dogStatus } = useLazyAsyncData(useDogPicture);

const visibility = programManager.getProgramVisibility(startMenuMetadata.programId);
const dynStyles = computed(() => ({
    left: startMenuMetadata.renderDefaults.x,
    top: startMenuMetadata.renderDefaults.y,
    width: startMenuMetadata.renderDefaults.width,
    height: startMenuMetadata.renderDefaults.height,
}));
</script>

<template>
    <div
        v-if="visibility !== 'closed'"
        class="absolute z-[150] bg-grey-normal flex items-stretch border-shadow border-solid border-2"
        :style="dynStyles"
    >
        <span
            class="text-grey-light bg-grey-dark2 text-3xl font-sans font-bold tracking-tight px-1 pb-2"
            style="text-orientation: mixed; writing-mode: sideways-lr"
            >Finndows 98</span
        >
        <div class="grow flex flex-col">
            <div class="grow"></div>
            <img v-if="dogStatus == 'success'" class="object-contain" :src="dog!.url" />
        </div>
    </div>
</template>

<style scoped></style>
