<template>
  <button @click="onClick">
    <svg-icon :path="iconPath" />
    <span>{{ name }}</span>
  </button>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'nuxt-property-decorator'
import { Location } from 'vue-router'
import SvgIcon from '~/components/svg-icon.vue'

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
    const route = this.$route
    const newRoute: Location = {
      query: route.query
    }
    newRoute.query[this.programId] = 'hello'

    console.log(`opening program ${this.programId}`, newRoute)
    console.log(this.$router)
    console.log(this.$router.push)
    window.x = this.$router
    window.y = newRoute
    this.$router.push(newRoute).catch((e: Error) => {
      if (e.name === 'NavigationDuplicated') {
        console.warn('Ignoring NavigationDuplicated error')
        return null
      }
      throw e
    })
  }

  closeProgram (): void {

  }

  get isActive (): boolean {
    return this.$route.query[this.programId] !== undefined
  }
}
</script>
