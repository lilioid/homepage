<template>
  <div>
    Explorer
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'

@Component({})
export default class Explorer extends Vue {}
</script>

<style scoped lang="scss">
@use "assets/utils";
@use "assets/colors";

div {
  background-color: colors.get_color("cyan");
}
</style>
