<script setup lang="ts">
const programManager = useProgramManager();

const TABS = ["This Website", "Pixelflut", "Riddles"];

const activeTab = computed(() => {
    return Math.max(
        TABS.findIndex((i) => i === programManager.getExtraData(codingMetadata.programId).value),
        0
    );
});

async function changeTab(to: number) {
    if (to == 0) {
        await programManager.setExtraData(codingMetadata.programId, null);
    } else {
        await programManager.setExtraData(codingMetadata.programId, TABS[to]);
    }
}
</script>

<template>
    <div class="h-full">
        <Tabs :tabs="TABS" :active-tab="activeTab" @update:active-tab="changeTab">
            <WindowsCodingThisWebsite v-if="activeTab == 0" />
            <WindowsCodingPixelflut v-else-if="activeTab == 1" />
            <WindowsCodingRiddles v-else-if="activeTab == 2" />
        </Tabs>
    </div>
</template>
