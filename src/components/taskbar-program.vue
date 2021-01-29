<template>
  <div class="taskbar-program no-select" :class="classes" role="button" @click="onClick">
    <svg-icon :path="metadata.icon" />
    <span>{{ metadata.title }}</span>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue, mixins } from 'nuxt-property-decorator'
import SvgIcon from '~/components/svg-icon.vue'
import { TaskManagerMixin } from '~/utils/mixins'
import { WindowMetadata } from '~/utils/windowMetadata'

@Component({
  components: { SvgIcon }
})
export default class TaskbarProgram extends mixins(TaskManagerMixin, Vue) {
  @Prop({ required: true }) metadata!: WindowMetadata

  onClick (): void {
    if (!this.isActive(this.metadata.programId)) {
      this.openProgram(this.metadata.programId)
    } else if (!this.isOnTop(this.metadata.programId)) {
      this.raiseProgram(this.metadata.programId)
    } else {
      this.closeProgram(this.metadata.programId)
    }
  }

  get classes (): string {
    if (this.isActive(this.metadata.programId)) {
      return 'shadow-inverse'
    } else {
      return 'shadow'
    }
  }
}
</script>

<style scoped lang="scss">
@use "assets/utils";
@use "assets/colors";

.taskbar-program {
  max-width: 164px;
  background-color: colors.get_color("grey");
  padding: 2px 4px;
  display: flex;
  align-items: center;

  & > :first-child {
    margin-right: 6px;
  }
}
</style>
