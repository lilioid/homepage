<template>
  <div class="desktop-window">
    <task-bar class="task-bar">
      <task-bar-button icon="account" text="CV"/>
      <task-bar-button icon="email" text="Contact"/>
      <task-bar-button icon="code-braces" text="Coding"/>
      <task-bar-button icon="gavel" text="Imprint"/>
    </task-bar>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import 'vue-class-component/hooks';
import TaskBar from '@/components/TaskBar.vue';
import TaskBarButton from '@/components/TaskBarButton.vue';

@Component({
  components: { TaskBarButton, TaskBar },
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
    }
  }
</style>
