<template>
  <div class="taskbar-program no-select" :class="classes" role="button" @click="onClick">
    <svg-icon :path="iconPath" />
    <span>{{ name }}</span>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'nuxt-property-decorator'
import { Dictionary } from 'vue-router/types/router'
import _ from 'lodash'
import SvgIcon from '~/components/svg-icon.vue'

type QueryParams = Dictionary<string | (string | null)[] | null | undefined>

@Component({
  components: { SvgIcon }
})
export default class TaskbarProgram extends Vue {
  @Prop({ required: true, type: String }) readonly programId!: string;
  @Prop({ required: true, type: String }) readonly name!: string;
  @Prop({ required: true, type: String }) readonly iconPath!: string;

  onClick (): void {
    if (!this.isActive) {
      this.openProgram()
    } else {
      this.closeProgram()
    }
  }

  openProgram (): void {
    let query: QueryParams = { ...this.$route.query }

    // add 1 to all existing window indexes so that window ordering is still correct
    // @ts-ignore because the type definition for lodash is incorrect here
    query = _.mapValues(query, (value: string) => {
      const numVal = Number(value)
      if (Number.isNaN(numVal)) {
        return value
      } else {
        return String(numVal + 1)
      }
    })

    query[this.programId] = '1'
    this.$router.replace({ query })
  }

  closeProgram (): void {
    const query: QueryParams = { ...this.$route.query }
    delete query[this.programId]
    this.$router.replace({ query })
  }

  get isActive (): boolean {
    return this.$route.query[this.programId] !== undefined
  }

  get classes (): string {
    if (this.isActive) {
      return 'shadow-inverse'
    } else {
      return 'shadow'
    }
  }
}
</script>

<style scoped lang="scss">
@use "assets/utils";
@use "assets/colors";

.taskbar-program {
  max-width: 164px;
  background-color: colors.get_color("grey");
  padding: 2px 4px;
  display: flex;
  align-items: center;

  & > :first-child {
    margin-right: 6px;
  }
}
</style>
