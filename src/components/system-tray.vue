<template>
  <div class="system-tray no-select">
    <slot />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({})
export default class SystemTray extends Vue {
}
</script>

<style lang="scss">
@use "assets/utils";
@use "assets/colors";

.system-tray {
  margin: 4px 6px;
  padding: 4px;
  @include utils.shadow($thickness: 1.5px, $inverse: true);
  display: flex;
  align-items: center;

  & > *:not(:last-child) {
    margin-right: 8px;
  }

  & > *:active:not(.non-interactive) {
    @include utils.shadow($inverse: true);
    border-style: dotted;
  }
}
</style>
