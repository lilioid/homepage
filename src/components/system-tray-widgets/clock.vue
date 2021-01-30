<template>
  <div class="non-interactive">
    {{ time }}
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({})
export default class ClockWidget extends Vue {
  time: string = ''

  private intervalId?: any

  created (): void {
    this.intervalId = setInterval(() => {
      this.time = new Date().toLocaleTimeString()
    }, 100)
  }

  beforeDestroy (): void {
    clearInterval(this.intervalId)
  }
}
</script>

<style scoped lang="scss">
* {
  font-family: "Bitstream Vera Sans Mono", "monospace";
}
</style>
