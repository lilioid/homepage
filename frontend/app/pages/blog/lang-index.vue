<script setup lang="ts">
definePageMeta({
  name: "lang-index",
  path: "/blog/lang-index.html",
});

const route = useRoute();
const withDrafts = computed(() => route.query["with_drafts"] != null && route.query["with_drafts"] == "true")

const {data: articles} = await useAsyncData("blog-lang-index", () => {
  const query = queryCollection("blog")
      .select("lang");

  if (withDrafts.value) {
    return query.all()
  } else {
    return query.where("draft", "<>", true).all()
  }
}, {
  watch: [withDrafts],
});

const langs = computed(() => {
  const allLangs = articles.value!.flatMap((i) => i.lang);
  const langIndex: Record<string, number> = {};

  for (let i of allLangs) {
    if (Object.keys(langIndex).includes(i)) {
      langIndex[i]! += 1;
    } else {
      langIndex[i] = 1;
    }
  }

  return langIndex;
});
</script>

<template>
  <HCommand cmd="find /blog/ -exec cat {} + | jq .lang | uniq">
    <HTitledSection title="Language Index" with="h1">
      <p class="my-2">
        This page shows an index over all languages in which articles throughout my blog are written.
        Click on one of the languages to see posts written in it.
      </p>

      <ul class="mt-6 list-disc pl-8">
        <li v-for="i_lang of Object.keys(langs)" :key="i_lang">
          <NuxtLink :to="{ name: 'blog', query: { lang: i_lang } }">#{{ i_lang }}</NuxtLink>
          <span> ({{ langs[i_lang] }} articles)</span>
        </li>
      </ul>
    </HTitledSection>
  </HCommand>
</template>
