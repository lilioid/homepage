<script setup lang="ts">
const props = defineProps<{
  cmd: string,
}>();

const arg0 = computed(() => props.cmd.split(" ")[0]);
const argv = computed(() => props.cmd.replace(`${arg0.value} `, ""));
</script>

<template>
  <div class="grid grid-cols-[2ch_auto] mb-8">
    <span class="text-blue1 font-bold">&gt;</span>
    <p>
      <span class="text-green1 pr-[1ch]">{{ arg0 }}</span>
      <span class="text-yellow1">{{ argv }}</span>
    </p>
    <div class="col-start-2">
      <slot />
    </div>
  </div>
</template>
