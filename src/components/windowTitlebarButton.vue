<script lang="ts" setup>
import { SvgIcon } from "#components";

const props = defineProps<{
    iconPath: string;
}>();
</script>

<template>
    <SvgIcon class="bg-grey-light shadow-default active:shadow-inverse" :path="props.iconPath" :size="22" />
</template>
