<template>
  <div>
    <viewport class="fullscreen non-mobile" />
    <bluescreen class="fullscreen only-mobile" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import Viewport from '~/components/viewport.vue'

@Component({
  components: { Viewport }
})
export default class Index extends Vue {
}
</script>

<style scoped>
.fullscreen {
  top: 0;
  left: 0;
  position: absolute;
  height: 100vh;
  width: 100vw;
}
</style>
