<template>
  <div v-if="isVisible" class="window" :class="classes" :style="style" @mousedown="onWindowMouseDown">
    <div class="titlebar no-select">
      <div class="titlebar-title">
        {{ metadata.title }}
      </div>
      <div class="button-container">
        <svg-icon class="button" :size="22" :path="minimizeButtonIcon" @click.native="onMinimizeButton" />
        <svg-icon class="button" :size="22" :path="fullscreenButtonIcon" @click.native="onMaximizeButton" />
        <svg-icon class="button" :size="22" :path="closeButtonIcon" @click.native="onCloseButton" />
      </div>
    </div>
    <div class="content-container">
      <slot />
    </div>
  </div>
</template>

<script lang="ts">
import {Component, mixins, Prop, Vue} from 'nuxt-property-decorator'
import {mdiWindowClose, mdiWindowMaximize, mdiWindowMinimize} from '@mdi/js'
import {WindowMetadata} from '~/utils/windowMetadata'
import {TaskManagerMixin} from '~/utils/mixins'
import SvgIcon from '~/components/svg-icon.vue'

@Component({
  components: { SvgIcon }
})
export default class Window extends mixins(TaskManagerMixin, Vue) {
  @Prop({ required: true }) readonly metadata!: WindowMetadata
  @Prop({ default: 0, type: String }) readonly x!: number
  @Prop({ default: 0, type: String }) readonly y!: number

  minimizeButtonIcon = mdiWindowMinimize
  closeButtonIcon = mdiWindowClose
  fullscreenButtonIcon = mdiWindowMaximize

  onWindowMouseDown (): void {
    this.raiseProgram(this.metadata.programId)
  }

  onMinimizeButton (): void {
    this.closeProgram(this.metadata.programId)
  }

  onMaximizeButton (): void {
    console.warn('maximizing programs is not yet implemented')
  }

  onCloseButton (): void {
    this.closeProgram(this.metadata.programId)
  }

  get isVisible (): boolean {
    return this.isActive(this.metadata.programId)
  }

  get style (): string {
    return `--x: ${this.x}; --y: ${this.y}; --z-index: ${100 + this.getProgramIndex(this.metadata.programId)};`
  }

  get classes (): string {
    if (this.isOnTop(this.metadata.programId)) {
      return 'on-top'
    }
    return ''
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
    max-width: calc(var(--window-max-width) - 4px);
    // the same as the containing window minus titlebar height minus border (2*2px)
    max-height: calc(var(--window-max-height) - var(--titlebar-height) - 4px);
  }
}

.window.on-top .titlebar {
  background-image: colors.get_color("titlebar-gradient");

  & .titlebar-title {
    color: colors.get_color("white");
  }
}

</style>
