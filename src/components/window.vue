<template>
  <div v-if="isActive(metadata.programId)" class="window" :class="classes" :style="style" @mousedown="onWindowMouseDown">
    <div class="titlebar no-select">
      <div class="titlebar-title">
        {{ metadata.title }}
      </div>
      <div class="button-container">
        <svg-icon class="button" :size="22" :path="minimizeButtonIcon" @click.native="onMinimizeButton" />
        <svg-icon class="button" :size="22" :path="maximizeButtonIcon" @click.native="onMaximizeButton" />
        <svg-icon class="button" :size="22" :path="closeButtonIcon" @click.native="onCloseButton" />
      </div>
    </div>
    <div v-show="!isProgramMinimized(metadata.programId)" class="content-container">
      <slot />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, mixins, Prop, Vue } from 'nuxt-property-decorator'
import { mdiWindowClose, mdiWindowMaximize, mdiWindowMinimize, mdiWindowRestore } from '@mdi/js'
import { WindowMetadata } from '~/utils/windowMetadata'
import { TaskManagerMixin } from '~/utils/mixins'
import SvgIcon from '~/components/svg-icon.vue'

@Component({
  components: { SvgIcon }
})
export default class Window extends mixins(TaskManagerMixin, Vue) {
  @Prop({ required: true }) readonly metadata!: WindowMetadata
  @Prop({ default: '0px', type: String }) readonly x!: string
  @Prop({ default: '0px', type: String }) readonly y!: string
  @Prop({ default: '999vw', type: String }) readonly width!: string
  @Prop({ default: '999vh', type: String }) readonly height!: string

  minimizeButtonIcon = mdiWindowMinimize
  closeButtonIcon = mdiWindowClose

  onWindowMouseDown (): void {
    this.raiseProgram(this.metadata.programId)
  }

  onMinimizeButton (): void {
    if (this.isProgramMinimized(this.metadata.programId)) {
      this.unminimizeProgram(this.metadata.programId)
    } else {
      this.minimizeProgram(this.metadata.programId)
    }
  }

  onMaximizeButton (): void {
    if (this.isProgramMaximized(this.metadata.programId)) {
      this.unmaximizeProgram(this.metadata.programId)
    } else {
      this.maximizeProgram(this.metadata.programId)
    }
  }

  onCloseButton (): void {
    this.closeProgram(this.metadata.programId)
  }

  get style (): string {
    const zIndex = 999 - this.getProgramIndex(this.metadata.programId)

    if (this.isProgramMaximized(this.metadata.programId)) {
      return `--x: 0px; --y: 0px; --z-index: ${zIndex}; --preferred-width: 999vw; --preferred-height: 999vh;`
    } else {
      return `--x: ${this.x}; --y: ${this.y}; --z-index: ${zIndex}; --preferred-width: ${this.width}; --preferred-height: ${this.height};`
    }
  }

  get classes (): string {
    const result = []
    if (this.isOnTop(this.metadata.programId)) {
      result.push('on-top')
    }
    if (this.isProgramMaximized(this.metadata.programId)) {
      result.push('maximized')
    }
    return result.join(' ')
  }

  get maximizeButtonIcon (): string {
    if (this.isProgramMaximized(this.metadata.programId)) {
      return mdiWindowRestore
    } else {
      return mdiWindowMaximize
    }
  }
}
</script>

<style scoped lang="scss">
@use "assets/utils";
@use "assets/colors";

.window {
  position: absolute;
  left: var(--x);
  top: var(--y);
  z-index: var(--z-index);
  @include utils.shadow();

  --titlebar-height: 32px;
  // the complete explorer screen minus x position
  --window-max-width: calc(100vw - var(--x));
  // the complete explorer screen minus y position minus taskbar height
  --window-max-height: calc(100vh - var(--y) - var(--taskbar-height));
  max-width: var(--window-max-width);
  max-height: var(--window-max-height);

  & .titlebar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: colors.get_color("grey-dark");
    height: var(--titlebar-height);

    & .titlebar-title {
      margin: 4px;
      font-size: large;
      font-weight: lighter;
    }

    & .button-container {
      margin: 0 4px;
      display: flex;

      & .button {
        background-color: colors.get_color("grey-light");
        @include utils.shadow();
        margin-right: 3px;
      }
      & .button:last-child {
        margin-right: 0;
      }
      & .button:active {
        @include utils.shadow($inverse: true)
      }
    }
  }

  & .content-container {
    @include utils.shadow($inverse: true);
    background-color: colors.get_color("white");
    padding: 4px;
    overflow: scroll;

    // the same as the containing window minus border (2*2px)
    max-width: min(calc(var(--window-max-width) - 4px), var(--preferred-width));
    // the same as the containing window minus titlebar height minus border (2*2px)
    max-height: min(calc(var(--window-max-height) - var(--titlebar-height) - 4px), var(--preferred-height));
  }
}

.window.on-top .titlebar {
  background-image: colors.get_color("titlebar-gradient");

  & .titlebar-title {
    color: colors.get_color("white");
  }
}

.window.maximized {
  width: 100%;
  height: 100%;

  & .content-container {
    width: 100%;
    height: 100%;
  }
}
</style>
