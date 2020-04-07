<template>
  <div class="task-bar">
    <task-bar-button text="Home" icon="microsoft-windows-classic" disabled/>
    <slot/>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  import Component from 'vue-class-component';
  import 'vue-class-component/hooks';
  import TaskBarButton from '@/components/TaskBarButton.vue';
  import {Prop} from 'vue-property-decorator';
  import VueTypes from 'vue-types';

  @Component({
    components: {TaskBarButton},
  })
  export default class TaskBar extends Vue {
  }
</script>

<style scoped lang="scss">
  @use "src/styles/colors";

  .task-bar {
    background-color: colors.get_color("grey");
    padding: 3px 8px;
    display: flex;
    flex-flow: row;
    align-content: baseline;
    border-top: 2px solid colors.get_color("shadow-raised");
    height: 40px;

    & > * {
      margin-right: 8px;
    }

    & > *:not(:first-child) {
      min-width: 128px;
    }
  }
</style>
