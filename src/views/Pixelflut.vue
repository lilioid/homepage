<template>
  <canvas width="800" height="600" ref="canvas"></canvas>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import 'vue-class-component/hooks';
import TaskBar from '@/components/TaskBar.vue';
import TaskBarButton from '@/components/TaskBarButton.vue';
import Window from '@/components/Window.vue';
import CV from '@/components/content/CV.vue';
import Contact from '@/components/content/Contact.vue';
import Imprint from '@/components/content/Imprint.vue';
import Coding from '@/components/content/Coding.vue';
import {PixelflutClient} from 'pixelflut-client/index';

@Component({
  components: {Coding, Imprint, Contact, CV, Window, TaskBarButton, TaskBar },
})
export default class Pixelflut extends Vue {
  pixelflutClient!: PixelflutClient;

  mounted() {
    this.pixelflutClient = new PixelflutClient("wss://www.finn-thorben.me/pixelflut.sock",
      this.$refs.canvas as HTMLCanvasElement, true);
  }

  beforeDestroy(): void {
    this.pixelflutClient.disconnect();
  }
}
</script>

<style scoped lang="scss">
canvas {
  width: 99vw;
  height: 99vh;
}
</style>
