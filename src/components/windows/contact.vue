<template>
  <div>
    <div class="contact-line">
      <svg-icon :path="emailIcon" />
      <a id="mail-link" href="mailto:contact@finn-thorben.me" class="simple-link">
        contact@finn-thorben.me</a>
    </div>

    <p>
      If you are using PGP and deem my website a valid method of identification,
      my public key is available for download from the HKS-Pool and here is its
      fingerprint:
    </p>

    <code>E28C78646FA4F70B30422385A78A03C25A3A3825</code>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import { mdiEmail } from '@mdi/js'
import SvgIcon from '~/components/svg-icon.vue'

@Component({
  components: { SvgIcon }
})
export default class Coding extends Vue {
  emailIcon = mdiEmail
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
