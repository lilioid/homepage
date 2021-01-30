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
    </explorer>
    <taskbar>
      <taskbar-program :metadata="startMetadata" />
      <taskbar-program :metadata="cvMetadata" />
      <taskbar-program :metadata="contactMetadata" />
      <taskbar-program :metadata="codingMetadata" />
      <!--taskbar-program :metadata="imprintMetadata" /-->
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

@Component({
  components: { Explorer, Taskbar, Cv, Contact, Coding }
})
export default class Viewport extends mixins(TaskManagerMixin, Vue) {
  startMetadata: WindowMetadata = {
    title: 'Start',
    programId: 'start',
    icon: mdiMicrosoftWindowsClassic
  }

  cvMetadata: WindowMetadata = {
    title: 'CV',
    programId: 'cv',
    icon: mdiAccount
  }

  contactMetadata: WindowMetadata = {
    title: 'Contact',
    programId: 'contact',
    icon: mdiEmail
  }

  codingMetadata: WindowMetadata = {
    title: 'Coding',
    programId: 'coding',
    icon: mdiCodeBraces
  }

  imprintMetadata: WindowMetadata = {
    title: 'Imprint',
    programId: 'imprint',
    icon: mdiGavel
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
    flex-grow: 0;
    flex-shrink: 0;
  }
}
</style>
