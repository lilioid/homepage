<script setup lang="ts">
import {articlePathComponents} from "~/utils/blogUtils";

definePageMeta({
  name: "blog",
  path: "/blog/index.html",
});

useSeoMeta({
  title: "Lillys Thoughts",
})

const route = useRoute();
const withDrafts = computed(() => route.query["with_drafts"] != null && route.query["with_drafts"] == "true");
const tagFilter = computed(() => route.query["tag"] != null ? route.query["tag"] : null);
const langFilter = computed(() => route.query["lang"] != null ? route.query["lang"] : null);

const {data: articles} = await useAsyncData("blog-index", async () => {
  let query = queryCollection("blog")
      .select("path", "title", "author", "short_desc", "lang", "tags", "created_at", "edited_at", "num")
      .order("created_at", "DESC");

  if (!withDrafts.value) {
    query = query.where("draft", "<>", true);
  }

  if (langFilter.value) {
    query = query.where("lang", "=", langFilter.value);
  }

  let articles = await query.all();

  // manually filter for tags because nuxt content cannot build a CONTAINS query
  if (tagFilter.value != null && typeof tagFilter.value == "string") {
    articles = articles.filter(i => i.tags.includes(tagFilter.value as string));
  }

  return articles;
}, {
  watch: [withDrafts, tagFilter, langFilter],
});
</script>

<template>
  <HCommand cmd="ls /blog/">
    <HTitledSection title="Blog Index" with="h1">
      <p class="mt-4 mb-2">
        This page contains an overview over all articles written as part my blog. Feel free to browse around and read
        however much you like. It's free.
      </p>

      <p class="my-2">
        Articles are categorized in tags and by language. An overview over all currently used ones can be found in the
        <NuxtLink :to="{ name: 'tag-index' }">tag index</NuxtLink> and <NuxtLink :to="{ name: 'lang-index' }">language index</NuxtLink>.
      </p>

      <ol class="mt-12 max-w-[900px] mx-auto">
        <li v-for="i_article in articles" :key="i_article.title" class="mb-16">
          <h2 class="text-2xl font-extrabold mt-2 mb-1">
            <NuxtLink :to="{ name: 'blog-article', params: { postNum: i_article.num } }">{{ i_article.title }}</NuxtLink>
          </h2>
          <HBlogArticleMetadata :article="i_article" />
          <p class="italic px-4 mt-1">{{ i_article.short_desc }}</p>
        </li>
      </ol>
    </HTitledSection>
  </HCommand>
</template>
