<template>
  <div v-if="isVisible">
    <div>
      <h1>{{ metadata.title }}</h1>
    </div>
    <slot />
  </div>
</template>

<script lang="ts">
import { Component, Prop } from 'nuxt-property-decorator'
import { WindowMetadata } from '~/utils/windowMetadata'
import { TaskManagerMixin } from '~/utils/mixins'

@Component({})
export default class Window extends TaskManagerMixin {
  @Prop({ required: true }) metadata!: WindowMetadata

  get isVisible (): boolean {
    return this.isActive(this.metadata.programId)
  }
}
</script>
