<template>
  <div class="split-container">
    <explorer>
      <window :metadata="cvMetadata" x="56px" y="56px">
        <cv />
      </window>
    </explorer>
    <taskbar>
      <taskbar-program :metadata="startMetadata" />
      <taskbar-program :metadata="cvMetadata" />
      <taskbar-program :metadata="contactMetadata" />
      <taskbar-program :metadata="codingMetadata" />
      <taskbar-program :metadata="imprintMetadata" />
    </taskbar>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import { mdiMicrosoftWindowsClassic, mdiAccount, mdiEmail, mdiCodeBraces, mdiGavel } from '@mdi/js'
import Taskbar from '~/components/taskbar.vue'
import Explorer from '~/components/explorer.vue'
import Cv from '~/components/windows/cv.vue'
import { WindowMetadata } from '~/utils/windowMetadata'

@Component({
  components: { Explorer, Taskbar, Cv }
})
export default class Viewport extends Vue {
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
}
</script>

<style scoped lang="scss">
.split-container {
  display: flex;
  flex-direction: column;
  --taskbar-height: 40px;

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
