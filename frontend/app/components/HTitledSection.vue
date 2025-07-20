<script setup lang="ts">
const props = defineProps<{
  title: string,
  with: "h1" | "h2" | "h3" | "h4" | "h5" | "h6",
}>();

const safeTitle = computed(() => encodeURIComponent(props.title.toLowerCase()));
</script>

<template>
  <section :id="safeTitle" class="target:animate-highlight">
    <component :is="props.with">
      <span>{{ props.title }}</span>
      <span class="ml-2"><a :href="`#${safeTitle}`">#</a></span>
    </component>

    <slot />
  </section>
</template>

<style scoped>
@reference "~/assets/css/main.css";

h1 {
  @apply text-4xl font-extrabold;
}

h2 {
  @apply text-2xl font-extrabold;
}

h3 {
  @apply text-xl font-bold;
}

h4 {
  @apply text-lg font-bold;
}

h5 {
  @apply font-bold;
}
</style>
