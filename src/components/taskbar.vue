<template>
  <div class="shadow taskbar">
    <div>
      <slot name="default" />
    </div>
    <system-tray>
      <slot name="system-tray" />
    </system-tray>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import SystemTray from '~/components/system-tray.vue'

@Component({
  components: { SystemTray }
})
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

  & > div:first-child {
    display: flex;
    flex-grow: 1;

    // normal programs
    & > * {
      flex-grow: 1;
      margin: 3px 5px;
    }
    // start menu
    & > *:first-child {
      max-width: 96px;
    }
  }
}
</style>
