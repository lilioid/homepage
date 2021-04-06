<template>
  <video ref="video" src="~/assets/rick_roll.mp4" loop="loop" />
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component
export default class RickRoll extends Vue {
  private mounted (): void {
    if (process.client) {
      const video = this.$refs.video as HTMLVideoElement
      video.play()
    }
  }
}
</script>

<style scoped>
video {
  display: block;
  width: 100%;
  height: 100%;
}
</style>
