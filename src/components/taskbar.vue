<template>
  <div>Taskbar</div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({})
export default class Taskbar extends Vue {
}
</script>

<style scoped lang="scss">
@use "assets/utils";
@use "assets/colors";

div {
  background-color: colors.get_color("grey");
}
</style>
