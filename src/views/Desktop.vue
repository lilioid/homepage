<template>
  <div class="desktop-window">
    <task-bar class="task-bar">
      <task-bar-button icon="account" text="CV"/>
      <task-bar-button icon="email" text="Contact"/>
      <task-bar-button icon="code-braces" text="Coding"/>
      <task-bar-button icon="gavel" text="Imprint"/>
    </task-bar>

    <window title="CV" style="width: 900px; left: 4vw; top: 7vh;">
      <c-v/>
    </window>
    <window title="Contact" style="width: 600px; left: 60vw; top: 6vh;">
      <contact/>
    </window>
    <window title="Coding" style="left: 25%; top: 8px;">
      <coding/>
    </window>
    <window title="Imprint" style="width: 600px; right: 10px; top: 10px;">
      <imprint/>
    </window>
    <!-- TODO Add Windows-Update -->
  </div>
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

@Component({
  components: {Coding, Imprint, Contact, CV, Window, TaskBarButton, TaskBar },
})
export default class Desktop extends Vue {
}
</script>

<style scoped lang="scss">
  @use "src/styles/colors";

  .desktop-window {
    width: 100vw;
    height: 100vh;
    position: absolute;
    top: 0;
    left: 0;
    overflow: hidden;
    background-color: colors.get_color("cyan");

    .task-bar {
      position: absolute;
      bottom: 0;
      width: 100%;
      z-index: 99;
    }
  }
</style>
