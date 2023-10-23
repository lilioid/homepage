<script setup lang="ts">
const props = defineProps<{
    tabs: string[];
    activeTab: number;
}>();
const emit = defineEmits<{
    (e: "update:activeTab", value: number): void;
}>();

function isTabActive(tab: string): boolean {
    return props.tabs.findIndex((i) => i === tab) == props.activeTab;
}

function switchToTab(tab: string) {
    emit(
        "update:activeTab",
        props.tabs.findIndex((i) => i === tab),
    );
}
</script>

<template>
    <div class="h-full flex flex-col bg-grey-normal">
        <menu role="tablist" class="flex pt-0.5 pl-0.5 pr-0.5 gap-[1px]">
            <li
                v-for="tab in props.tabs"
                role="tab"
                class="py-1 px-1.5 border-t-2 border-l-2 border-r-2 border-solid rounded-tl-sm rounded-tr-sm select-none cursor-pointer"
                :aria-selected="isTabActive(tab)"
                :class="isTabActive(tab) ? 'border-shadow-inverse' : 'border-shadow border-b-2'"
                @click.prevent="switchToTab(tab)"
            >
                {{ tab }}
            </li>
            <div aria-hidden="true" class="grow border-b-2 border-solid border-shadow"></div>
        </menu>
        <div
            role="tabpanel"
            class="bg-white grow ml-0.5 mr-0.5 p-2 border-l-2 border-solid border-shadow-inverse"
        >
            <slot>Add tab content in its slot</slot>
        </div>
    </div>
</template>
