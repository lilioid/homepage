<template>
  <div>
    <div class="contact-line">
      <i class="mdi mdi-email"/>
      <a id="mail-link" href="mailto:contact@finn-thorben.me" class="simple-link">
        contact@finn-thorben.me</a>
    </div>

    <p>If you are using PGP and deem my website a valid method of identification,
      my public key is available for download from the HKS-Pool and here is its
      fingerprint:
    </p>
    <code>E28C78646FA4F70B30422385A78A03C25A3A3825</code>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue';
  import Component from 'vue-class-component';
  import 'vue-class-component/hooks';
  import {Prop} from 'vue-property-decorator';
  import VueTypes from 'vue-types';

  @Component({})
  export default class Contact extends Vue {
  }
</script>

<style scoped lang="scss">
  @use "src/styles/colors";

  .contact-line {
    display: flex;
    align-content: baseline;

    & > * {
      margin-right: 6px;
    }
  }

  code {
    display: block;
    padding: 8px;
    font-family: monospace;
    background-color: colors.get_color("grey-light");
  }
</style>
