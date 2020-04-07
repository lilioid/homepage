<template>
  <div class="task-bar-button" :class="isActive ? 'shadow-inverse' : 'shadow'" @click="onClick">
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
import { Prop } from 'vue-property-decorator';
import VueTypes from 'vue-types';

@Component({})
export default class TaskBarButton extends Vue {
  @Prop(VueTypes.string.isRequired) readonly text!: string;

  @Prop(VueTypes.string.isRequired) readonly icon!: string;

  get isActive(): boolean {
    const app = this.$route.query.app as string | string[];
    return ((typeof app === 'string' && app.toLowerCase() === this.text.toLowerCase())
      || (app instanceof Array
          && app.map((a) => a.toLowerCase()).includes(this.text.toLowerCase())));
  }

  onClick(): void {
    const query = this.$route.query;
    if (this.isActive && query.app instanceof Array) {
      query.app = query.app.filter((i) => i && i.toLowerCase() !== this.text.toLowerCase());
    } else if (this.isActive) {
      delete query.app;
    } else if (!this.isActive && query.app instanceof Array) {
      query.app.push(this.text.toLowerCase());
    } else {
      query.app = this.text.toLowerCase();
    }

    console.log(query, this.$route.path);
    this.$router.push({ query }).catch((e) => console.error(e));
  }
}
</script>

<style scoped lang="scss">
  @use "src/styles/shadows";

  .task-bar-button {
    padding: 2px 8px 2px 6px;
    cursor: pointer;
    min-height: 32px;
    min-width: 64px;
    display: flex;
    align-items: center;

    & .task-bar-icon {
      font-size: x-large;
    }

    & .task-bar-text {
      padding-left: 6px;
    }
  }
</style>
