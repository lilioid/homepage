<template>
  <pixelflut />
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import Pixelflut from '~/components/pixelflut.vue'

@Component({
  components: { Pixelflut }
})
export default class PixelflutPage extends Vue {
}
</script>

<style scoped lang="scss">
.fullscreen {
  top: 0;
  left: 0;
  position: absolute;
  height: 100vh;
  width: 100vw;
}
</style>
