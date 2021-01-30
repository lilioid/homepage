<template>
  <svg-icon :path="metadata.icon" @click.native="onClick" />
</template>

<script lang="ts">
import { Component, Vue, Prop, mixins } from 'nuxt-property-decorator'
import { WindowMetadata } from '~/utils/windowMetadata'
import { TaskManagerMixin } from '~/utils/mixins'
import SvgIcon from '~/components/svg-icon.vue'

@Component({
  components: { SvgIcon }
})
export default class SystemTrayProgram extends mixins(TaskManagerMixin, Vue) {
  @Prop({ required: true }) metadata!: WindowMetadata

  onClick (): void {
    if (!this.isActive(this.metadata.programId)) {
      this.openProgram(this.metadata.programId)
    } else if (!this.isOnTop(this.metadata.programId)) {
      this.raiseProgram(this.metadata.programId)
    }
  }
}
</script>
