<template>
  <div class="shadow taskbar">
    <slot />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({})
export default class Taskbar extends Vue {
}
</script>

<style scoped lang="scss">
@use "assets/utils";
@use "assets/colors";

.taskbar {
  background-color: colors.get_color("grey");
  display: flex;
  z-index: 999;

  & > * {
    flex-grow: 1;
    margin: 3px 5px;
  }

  & > *:first-child {
    max-width: 96px;
  }
}
</style>
