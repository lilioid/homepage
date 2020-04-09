<template>
  <div v-if="isOpen" class="window" :class="classes" @click="onWindowClick" :style="{ 'z-index': stackIndex }">
    <div class="titlebar no-select">
      <h1 class="titlebar-title">{{ title }}</h1>
      <div class="titlebar-button-container">
        <span class="titlebar-button mdi mdi-window-minimize" @click.stop="onClose"/>
        <span class="titlebar-button mdi mdi-window-maximize" @click.stop="onMaximize"/>
        <span class="titlebar-button mdi mdi-window-close" @click.stop="onClose"/>
      </div>
    </div>
    <div class="body">
      <slot/>
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  import Component from 'vue-class-component';
  import 'vue-class-component/hooks';
  import {Prop} from 'vue-property-decorator';
  import VueTypes from 'vue-types';

  @Component({})
  export default class Window extends Vue {
    @Prop(VueTypes.string.isRequired) readonly title!: string;

    @Prop(VueTypes.integer.def(0)) readonly stackNumber!: number;

    get isOpen(): boolean {
      return this.$isAppOpen(this.title.toLowerCase())
    }

    get classes(): string[] {
      return [
        this.$isAppMaximized(this.title.toLowerCase()) ? 'maximized' : '',
        this.$isAppOnTop(this.title.toLowerCase()) ? 'on-top' : ''
      ]
    }

    get stackIndex(): number {
      return this.$getAppStackIndex(this.title.toLowerCase())
    }

    onMaximize(): void {
      this.$toggleAppMaximized(this.title.toLowerCase());
    }

    onClose(): void {
      this.$toggleApp(this.title.toLowerCase())
    }

    onWindowClick(): void {
      this.$raiseApp(this.title.toLowerCase())
    }
  }
</script>

<style scoped lang="scss">
  @use "src/styles/colors";
  @use "src/styles/shadows";

  .window {
    position: absolute;
    @include shadows.shadow($thickness: 3px);

    &:not(.maximized) .body {
      max-width: 75vw;
      max-height: 80vh;
    }
    &.maximized {
      top: 0 !important;
      left: 0 !important;
      width: 100vw !important;
      height: calc(100vh - 40px) !important;

      & .body {
        width: 100%;
        height: 100%;
      }
    }

    &.on-top .titlebar {
      background: colors.get_color("topbar-gradient");
      color: colors.get_color("grey");
    }
    &:not(.on-top) .titlebar {
      background-color: colors.get-color("grey-dark");
    }

    .titlebar {
      display: flex;
      justify-content: space-between;
      align-content: baseline;

      .titlebar-title {
        margin: 3px 0 2px 4px;
        font-size: large;
        font-weight: lighter;
      }

      .titlebar-button-container {
        display: flex;
        align-items: center;

        .titlebar-button {
          margin: 0 2px;
          padding-left: 2px;
          width: 18px;
          height: 18px;
          background-color: colors.get_color("grey");
          color: colors.get_color("black");
          @include shadows.shadow();

          &:active {
            @include shadows.shadow($inverse: true);
          }
        }
      }
    }

    .body {
      background-color: colors.get_color("white");
      @include shadows.shadow($inverse: true);
      padding: 6px 4px 4px;
      overflow: auto;
    }
  }
</style>
