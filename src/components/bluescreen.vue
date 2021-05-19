<template>
  <div class="container">
    <p class="title">Error: DISPLAY: TOO: SMALL</p>
    <p>
      This is the Website of Finn-Thorben Sell.<br>
      I am a software engineer and am currently pursuing my Master of Science in Computer Science.

      <br><br>
      <a class="contact-line" href="mailto:contact@finn-thorben.me">
        <svg-icon :path="emailIcon" />
        <span>contact@finn-thorben.me</span>
      </a>

      <a class="contact-line" href="https://github.com/ftsell">
        <svg-icon :path="githubIcon" />
        <span>ftsell</span>
      </a>
    </p>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import { mdiEmail, mdiGithub } from '@mdi/js'

@Component({})
export default class BlueScreen extends Vue {
  emailIcon = mdiEmail
  githubIcon = mdiGithub
}
</script>

<style scoped lang="scss">
@use "assets/colors";

.container {
  color: colors.get_color("white");
  background-color: colors.get_color("blue_of_death");
  padding: 24px;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  p {
    margin-bottom: 20px;
  }

  a {
    color: colors.get_color("white");
  }

  .title {
    background-color: colors.get_color("grey-dark");
    color: colors.get_color("blue_of_death");
    padding: 4px;
    font-weight: bold;
  }

  .contact-line {
    padding: 6px 0;
    display: flex;
    align-content: baseline;
    & > :first-child {
      margin-right: 6px;
    }
  }
}
</style>
