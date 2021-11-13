<template>
  <div>
    <a class="contact-line" href="mailto:contact@finn-thorben.me">
      <svg-icon :path="emailIcon" />
      <span>contact@finn-thorben.me</span>
    </a>

    <a class="contact-line" href="https://github.com/ftsell">
      <svg-icon :path="githubIcon" />
      <span>ftsell</span>
    </a>

    <p>
      If you are using PGP and deem my website a valid method of identification,
      my public key is available for download from
      <a href="https://keys.openpgp.org/search?q=E28C78646FA4F70B30422385A78A03C25A3A3825" target="_blank">keys.openpgp.org</a>
      or directly from <a href="/finn-thorben_sell.gpg">here</a>.<br>
      Its fingerprint is:
    </p>

    <code>E28C78646FA4F70B30422385A78A03C25A3A3825</code>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import { mdiEmail, mdiGithub } from '@mdi/js'
import SvgIcon from '~/components/svg-icon.vue'

@Component({
  components: { SvgIcon }
})
export default class Contact extends Vue {
  emailIcon = mdiEmail
  githubIcon = mdiGithub
}
</script>

<style scoped lang="scss">
@use "assets/colors";
@use "assets/utils";

.contact-line {
  display: flex;
  align-content: baseline;
  margin-bottom: 12px;

  & > :first-child {
    color: colors.get_color("black");
    margin-right: 6px;
  }
}

code {
  display: block;
  padding: 8px;
  font-family: "Bitstream Vera Sans Mono", "monospace";
  margin-top: 16px;
  background-color: colors.get_color("grey-light");
}
</style>
