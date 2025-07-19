<script setup lang="ts">
interface Friend {
  name: string,
  url: string,
}

const friends: Friend[] = [
  {
    name: "bonsaibeef.de",
    url: "https://bonsaibeef.de/",
  },
  {
    name: "Freddy",
    url: "https://frederico.info/",
  },
  {
    name: "Helena",
    url: "https://helena.place/",
  },
  {
    name: "kritzl",
    url: "https://kritzl.dev/",
  },
  {
    name: "Noah Fust",
    url: "https://noahfuhst.de/",
  },
  {
    name: "olebit",
    url: "https://oleb.it/",
  },
  {
    name: "traumweh",
    url: "https://traumweh.dev/",
  },
  {
    name: "Vic Wrobel",
    url: "https://www.vicwrobel.de/",
  },
  {
    name: "Markus",
    url: "https://weboverflow.de/",
  },
];
</script>

<template>
  <footer>
    <HCommand cmd="ls /friends/">
      <ul class="flex flex-wrap gap-3 items-baseline">
        <li v-for="i of friends" :key="i.name">
          <a :href="i.url" rel="external">{{ i.name }}</a>
        </li>
      </ul>
    </HCommand>
  </footer>
</template>
