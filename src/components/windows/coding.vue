<script setup lang="ts">
const activeTab = ref(0);
</script>

<template>
    <div class="h-full">
        <Tabs :tabs="['This Website', 'Pixelflut', 'Riddles']" v-model:active-tab="activeTab">
            <WindowsCodingThisWebsite v-if="activeTab == 0" />
            <WindowsCodingPixelflut v-else-if="activeTab == 1" />
            <WindowsCodingRiddles v-else-if="activeTab == 2" />
        </Tabs>
    </div>
</template>
