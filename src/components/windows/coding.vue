<template>
  <div>
    <div class="project">
      <h1>This Webpage</h1>
      <p>
        The first Project which comes to mind is this WebPage itself.<br>
        I built it using the Vue.js and am hosting it on my own server.
      </p>
      <p>
        The page is completely Open-Source and you can find it's source code on my
        <a href="https://github.com/ftsell/homepage" target="_blank">GitHub</a>
      </p>
    </div>
    <div class="spacer" />

    <div class="project">
      <h1>Pixelflut</h1>
      <p>
        <i>Pixelflut</i> is a small game for programmers inspired by reddits
        <a href="https://www.reddit.com/r/place" target="_blank">r/place</a> and
        <a href="https://cccgoe.de/wiki/Pixelflut" target="_blank">CCCGOE's Pixelflut</a>.
      </p>
      <p>
        You can participate by sending a TCP or UDP command to <code>finn-thorben.me:9876</code>
        in the format <code>PX $X $Y $COLOR\n</code>. <br>
        <i>$X</i> is the x coordinate <br>
        <i>$Y</i> is the y coordinate <br>
        <i>$COLOR</i> is the HEX encoded rgb value (no '#' character) <br>
        The canvas is currently {{ pixelflutWidth }}x{{ pixelflutHeight }} pixels wide and high.
      </p>
      <p>
        More information is available by sending <code>HELP\n</code> to the same server.
      </p>
      <pixelflut @pixelflutSizeReceived="onPixelflutSizeReceived" />
    </div>
    <div class="spacer" />

    <div class="project">
      <h1>Lecture2Gether</h1>
      <p>
        During the <i>EU vs Virus</i> Hackathon some friends and I programmed an application for
        viewing online Lectures together. Hence we called it Lecture2Gether.
      </p>
      <p>
        A Live-Demo is available at <a href="https://lecture2gether.eu/" target="_blank">lecture2gether.eu</a>
        and the source code is on <a href="https://github.com/TheNerdful8/Lecture2Gether/">GitHub</a>
        together with some additional information.
      </p>
    </div>
    <div class="spacer" />

    <div class="project">
      <h1>Riddles</h1>
      <p>
        Hidden on this page is the entry to a few programmatic riddles I have prepared.
        They are intended for programmers and other technically adept people but anyone can have a
        go as far as I'm concerned.<br>
        The most important thing is to have fun!
      </p>
      <a v-show="false" href="/verysecretriddles/">Here is the entrance</a>
    </div>
    <div class="spacer" />

    <div class="project">
      <h1>Coding statistics</h1>
      <div class="wakatime-figure-container">
        <figure>
          <embed src="https://wakatime.com/share/@ftsell/0a0ef242-8431-4795-8fe5-30890cd5fb54.svg">
        </figure>
        <figure>
          <embed src="https://wakatime.com/share/@ftsell/e3ce957f-28a8-430c-b32a-1b85bb7b5ca6.svg">
        </figure>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import Pixelflut from '~/components/pixelflut.vue'

@Component({
  components: { Pixelflut }
})
export default class Coding extends Vue {
  pixelflutWidth: number = -1
  pixelflutHeight: number = -1

  private onPixelflutSizeReceived (e: {width: number, height: number}): void {
    this.pixelflutWidth = e.width
    this.pixelflutHeight = e.height
  }
}
</script>

<style lang="scss">
@use "assets/colors";

.project {
  margin: 6px 0;
  padding: 0 4px;

  &:first-child {
    margin-top: 2px;
  }
}

.spacer {
  height: 2px;
  margin: 24px 0;
  background-color: colors.get_color("grey-light");
  border-radius: 20%;
}

.wakatime-figure-container {
  display: flex;
  flex-flow: row wrap;

  & > figure {
    flex-basis: 512px;
    flex-grow: 1;
    flex-shrink: 1;
    max-width: 768px;
  }
}
</style>
