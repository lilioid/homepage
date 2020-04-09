<template>
    <router-view/>
</template>

<style lang="scss">
  @use "styles/colors";
  @import "styles/helpers_classes";
  @import "~@mdi/font/css/materialdesignicons.css";

  body {
    margin: 0;
  }

  #app {
    font-family: Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: colors.get_color("black");
  }
</style>
