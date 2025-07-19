<script setup lang="ts">
definePageMeta({
  name: "home",
});

useHead({
  title: "Lillys Homepage",
})
</script>

<template>
  <HCommand cmd="cat /index.html">
    <section id="introduction">
      <h2 class="text-2xl font-extrabold mt-2 mb-4">Hello World!</h2>

      <p>
        This is the personal homepage of me, Lilly.
        I'm a professional computer toucher, formerly at the University of Hamburg, now mainly at CCCHH and B1-Systems.
        My expertise and interests are activism, System Administration and Automation, Networking (the computer as well
        as the people kind) and creating fun applications for whatever seems useful.
        Additionally, I like learning things about privacy, security and how computers work from the ground up.
      </p>
    </section>

    <section id="contact">
      <h2 class="text-2xl font-extrabold mt-12 mb-4">Contact</h2>
      <p class="mb-3">I can be reached and found on any of these platforms:</p>
      <ul class="list-disc pl-8">
        <li>Email: <a href="mailto:li@lly.sh" rel="external">li@lly.sh</a></li>
        <li>Matrix: <a href="https://matrix.to/#/@17sell:mafiasi.de" rel="external">@17sell:mafiasi.de</a></li>
        <li>GitHub: <a href="https://github.com/lilioid" rel="external">lilioid</a></li>
        <li>Mastodon: <a href="https://chaos.social/@lilly" rel="external">@lilly@chaos.social</a></li>
        <li>Pixelfed: <a href="https://dogo.pictures/lilly" rel="external">@lilly@dogo.pictures</a></li>
      </ul>
    </section>

    <section id="projects">
      <h2 class="text-2xl font-extrabold mt-12 mb-4">Notable Projects</h2>
      <p class="mb-4">
        I do have a more detailed
        <NuxtLink :to="{ name: 'projects' }">list of projects</NuxtLink>
        available here's a quick list of the most notable ones.
      </p>

      <div class="pl-8">
        <details class="mb-4">
          <summary><i>py_simple_openid_connect</i> - <span>Simple and opinionated OpenID Connect client library</span>
          </summary>
          <ul class="flex justify-around m-4 ml-8">
            <li><a href="https://github.com/fsinfuhh/py_simple_openid_connect/" rel="external">GitHub</a></li>
            <li><a href="https://simple-openid-connect.readthedocs.io/en/stable/" rel="external">Documentation</a></li>
            <li><a href="https://pypi.org/project/simple_openid_connect/" rel="external">PyPi Page</a></li>
          </ul>
          <p class="m-4 mb-8">
            This library implements the <i>Relying Party</i> and <i>Resource Server</i> parts of the OpenID
            Connect specification. It provides integrations into Django and Django-Rest-Framework, supports
            most commonly used OpenID Connect features but is designed to be as easy to use and understand as
            possible.
          </p>
        </details>

        <details class="mb-4">
          <summary><i>Pixelflut</i> - <span>A pixel drawing game for programmers</span></summary>
          <ul class="flex justify-around m-4">
            <li><a href="https://github.com/lilioid/pixelflut" rel="external">GitHub</a></li>
          </ul>
          <p class="m-4">
            Pixelflut is a game for programmers and other technical minded people in which bots are used to
            collaboratively or competitively draw on a shared canvas.
          </p>
          <p class="m-4 mb-8">
            There is also a dedicated <a href="/pixelflut.html">pixelflut site</a> available which has more information
            on how to participate and on which the current canvas content is always live-streamed.
          </p>
        </details>

        <details>
          <summary><i>Mafiasi</i> - <span>Web-Services for university students</span></summary>
          <ul class="flex justify-around m-4">
            <li><a href="https://mafiasi.de" rel="external">Website</a></li>
            <li><a href="https://github.com/fsinfuhh/mafiasi" rel="external">Source Code</a></li>
          </ul>
          <p class="m-4">
            <i>mafiasi.de</i> is a website that offers various web based
            services
            for computer science students of the Universität Hamburg.<br/>
          </p>
        </details>
      </div>
    </section>

  </HCommand>
</template>
