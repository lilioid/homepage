<template>
  <div class="task-bar-button no-select" :class="classes"
       @click="onClick">
    <span class="task-bar-icon mdi" :class="'mdi-' + icon"></span>
    <span class="task-bar-text">
      {{ text }}
    </span>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  import Component from 'vue-class-component';
  import 'vue-class-component/hooks';
  import {Prop} from 'vue-property-decorator';
  import VueTypes from 'vue-types';

  @Component({})
  export default class TaskBarButton extends Vue {
    @Prop(VueTypes.string.isRequired) readonly text!: string;

    @Prop(VueTypes.string.isRequired) readonly icon!: string;

    @Prop(VueTypes.bool.def(false)) readonly disabled!: boolean;

    get isActive(): boolean {
      return !this.disabled && this.$isAppOpen(this.text.toLowerCase());
    }

    get classes(): string[] {
      return [
        this.isActive ? 'shadow-inverse': 'shadow',
        this.disabled ? 'disabled': '',
      ]
    }

    onClick(): void {
      if (!this.disabled) {
        if (this.$isAppOpen(this.text.toLowerCase()) && !this.$isAppOnTop(this.text.toLowerCase())) {
          this.$raiseApp(this.text.toLowerCase());
        } else {
          this.$toggleApp(this.text.toLowerCase());
        }
      }
    }
  }
</script>

<style scoped lang="scss">
  @use "src/styles/shadows";

  .task-bar-button {
    padding: 2px 8px 2px 6px;
    min-height: 32px;
    min-width: 64px;
    display: flex;
    align-items: center;

    &:not(.disabled) {
      cursor: pointer;
    }

    & .task-bar-icon {
      font-size: x-large;
    }

    & .task-bar-text {
      padding-left: 6px;
    }
  }
</style>
