<template>
  <div>
    <explorer />
    <taskbar />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import Taskbar from '~/components/taskbar.vue'
import Explorer from '~/components/explorer.vue'

@Component({
  components: { Explorer, Taskbar }
})
export default class Viewport extends Vue {}
</script>
