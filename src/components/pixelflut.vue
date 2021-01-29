<template>
  <canvas ref="canvas" width="800" height="600" />
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import { PixelflutClient } from 'pixelflut-client'

@Component({})
export default class Pixelflut extends Vue {
  pixelflutClient!: PixelflutClient

  mounted () {
    this.pixelflutClient = new PixelflutClient('wss://www.finn-thorben.me/pixelflut.sock', this.$refs.canvas as HTMLCanvasElement, false)
    this.pixelflutClient.connect().then(() => {
      this.$emit('pixelflutSizeReceived', {width: this.pixelflutClient.width, height: this.pixelflutClient.height})
    })
  }

  beforeDestroy (): void {
    this.pixelflutClient.disconnect()
  }
}
</script>
