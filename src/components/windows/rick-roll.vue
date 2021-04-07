<template>
  <div>
    <video ref="video" src="~/assets/rick_roll.mp4" loop="loop" />
    <p>Source: <a href="https://youtu.be/dQw4w9WgXcQ">YouTube: Rick Astley - Never Gonna Give You Up</a></p>
  </div>
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
}
</style>
