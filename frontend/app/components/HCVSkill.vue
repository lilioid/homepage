<script setup lang="ts">
const props = defineProps<{
  name: string,
  level: number,
}>();

const maxSkillLevel = 10;
</script>

<template>
  <label>{{ props.name }}</label>
  <div class="text-lg">
    <span class="inline-block w-11">{{ props.level }}/{{ maxSkillLevel }}</span>
    <span class="font-extrabold font-mono">[</span>
    <span class="inline-block w-[10ch] font-mono text-green1">
      <span v-for="i in Array(props.level).keys()" :key="i">#</span>
    </span>
    <span class="font-extrabold font-mono">]</span>
  </div>
</template>
