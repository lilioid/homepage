<script lang="ts" setup>
import { SvgIcon } from "#components";

const props = defineProps<{
    iconPath: string;
}>();
</script>

<template>
    <SvgIcon
        class="bg-grey-light border-2 border-solid border-shadow active:border-shadow-inverse"
        :path="props.iconPath"
        :size="22"
    />
</template>
