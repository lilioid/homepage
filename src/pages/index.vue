<template>
  <viewport />
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import Viewport from '~/components/viewport.vue'

@Component({
  components: { Viewport }
})
export default class Index extends Vue {

}
</script>
