<template>
  <div class="split-container">
    <explorer />
    <taskbar>
      <taskbar-program program-id="start" name="Start" :icon-path="startIcon" />
      <taskbar-program program-id="cv" name="CV" :icon-path="cvIcon" />
      <taskbar-program program-id="contact" name="Contact" :icon-path="contactIcon" />
      <taskbar-program program-id="coding" name="Coding" :icon-path="codingIcon" />
      <taskbar-program program-id="imprint" name="Imprint" :icon-path="imprintIcon" />
    </taskbar>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import { mdiMicrosoftWindowsClassic, mdiAccount, mdiEmail } from '@mdi/js'
import Taskbar from '~/components/taskbar.vue'
import Explorer from '~/components/explorer.vue'

@Component({
  components: { Explorer, Taskbar }
})
export default class Viewport extends Vue {
  startIcon = mdiMicrosoftWindowsClassic
  cvIcon = mdiAccount
  contactIcon = mdiEmail
  codingIcon = mdiEmail
  imprintIcon = mdiEmail
}
</script>

<style scoped lang="scss">
.split-container {
  display: flex;
  flex-direction: column;

  & > *:first-child {
    flex-basis: 90%;
    flex-grow: 99;
  }

  & > *:nth-child(2) {
    flex-basis: 45px;
    flex-grow: 0;
    flex-shrink: 0;
  }
}
</style>
