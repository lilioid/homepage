<template>
  <svg
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
  >
    <path :d="path" />
  </svg>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'nuxt-property-decorator'

@Component({})
export default class SvgIcon extends Vue {
  @Prop({ required: true, type: String }) readonly path!: string
  @Prop({ default: 24, type: Number }) readonly size!: number
}
</script>

<style scoped>
path {
  fill: currentColor;
}
</style>
