<template>
  <div class="split-container">
    <explorer>
      <window :metadata="cvMetadata" x="3vw" y="4vh" width="48vw" height="80vh">
        <cv />
      </window>
      <window :metadata="contactMetadata" x="64vw" y="8vh" width="32vw">
        <contact />
      </window>
      <window :metadata="codingMetadata" x="6vw" y="3vh" width="90vw">
        <coding />
      </window>
      <window :metadata="imprintMetadata" x="calc(100vw - 35vw)" y="20px" width="30vw">
        <imprint />
      </window>
    </explorer>
    <taskbar>
      <template #default>
        <taskbar-program :metadata="startMetadata" />
        <taskbar-program :metadata="cvMetadata" />
        <taskbar-program :metadata="contactMetadata" />
        <taskbar-program :metadata="codingMetadata" />
      </template>
      <template #system-tray>
        <system-tray-program :metadata="imprintMetadata" />
        <clock-widget />
      </template>
    </taskbar>
  </div>
</template>

<script lang="ts">
import { Vue, Component, mixins } from 'nuxt-property-decorator'
import { mdiMicrosoftWindowsClassic, mdiAccount, mdiEmail, mdiCodeBraces, mdiGavel } from '@mdi/js'
import Taskbar from '~/components/taskbar.vue'
import Explorer from '~/components/explorer.vue'
import Cv from '~/components/windows/cv.vue'
import { WindowMetadata } from '~/utils/windowMetadata'
import Contact from '~/components/windows/contact.vue'
import Coding from '~/components/windows/coding.vue'
import { TaskManagerMixin } from '~/utils/mixins'
import SystemTrayProgram from '~/components/system-tray-widgets/system-tray-program.vue'
import ClockWidget from '~/components/system-tray-widgets/clock.vue'
import Imprint from '~/components/windows/imprint.vue'

@Component({
  components: { Explorer, Taskbar, Cv, Contact, Coding, SystemTrayProgram, ClockWidget, Imprint }
})
export default class Viewport extends mixins(TaskManagerMixin, Vue) {
  startMetadata: WindowMetadata = {
    title: 'Start',
    programId: 'start',
    icon: mdiMicrosoftWindowsClassic,
    canOpen: true
  }

  cvMetadata: WindowMetadata = {
    title: 'CV',
    programId: 'cv',
    icon: mdiAccount,
    canOpen: true
  }

  contactMetadata: WindowMetadata = {
    title: 'Contact',
    programId: 'contact',
    icon: mdiEmail,
    canOpen: true
  }

  codingMetadata: WindowMetadata = {
    title: 'Coding',
    programId: 'coding',
    icon: mdiCodeBraces,
    canOpen: true
  }

  imprintMetadata: WindowMetadata = {
    title: 'Imprint',
    programId: 'imprint',
    icon: mdiGavel,
    canOpen: true
  }

  async created (): Promise<void> {
    // do an initial redirect to open cv and contact programs
    // only do so on client-side render because the pre-rendered site and client-side-rendered site might differ
    // which would result in programs being open initially but instantly closing
    if (process.client && Object.keys(this.$route.query).length === 0) {
      await this.openProgram(this.cvMetadata.programId, this.contactMetadata.programId)
    }
  }
}
</script>

<style scoped lang="scss">
.split-container {
  display: flex;
  flex-direction: column;
  --taskbar-height: 48px;

  & > *:first-child {
    flex-basis: 90%;
    flex-grow: 99;
  }

  & > *:nth-child(2) {
    flex-basis: var(--taskbar-height);
    max-height: var(--taskbar-height);
    flex-grow: 0;
    flex-shrink: 0;
  }
}
</style>
