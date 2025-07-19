<template>
  <header>
    <nav>
      <HCommand cmd="ls /nav/">
        <ul class="flex gap-3 items-baseline">
          <li>
            <NuxtLink :to="{ name: 'home' }">Home</NuxtLink>
          </li>
          <li>
            <NuxtLink :to="{ name: 'cv' }">CV</NuxtLink>
          </li>
          <li>
            <NuxtLink :to="{ name: 'projects' }">Projects</NuxtLink>
          </li>
          <li>
            <NuxtLink :to="{ name: 'blog' }">Thoughts</NuxtLink>
          </li>
          <li class="flex-1 text-end">
            <NuxtLink :to="{ name: 'legal' }">Legal</NuxtLink>
          </li>
        </ul>
      </HCommand>
    </nav>
  </header>
</template>
