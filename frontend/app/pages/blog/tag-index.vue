<script setup lang="ts">
definePageMeta({
  name: "tag-index",
  path: "/blog/tag-index.html",
});

const route = useRoute();
const withDrafts = computed(() => route.query["with_drafts"] != null && route.query["with_drafts"] == "true")

const {data: articles} = await useAsyncData("blog-tag-index", () => {
  const query = queryCollection("blog")
      .select("tags");

  if (withDrafts.value) {
    return query.all()
  } else {
    return query.where("draft", "<>", true).all()
  }
}, {
  watch: [withDrafts],
});

const tags = computed(() => {
  const allTags = articles.value!.flatMap((i) => i.tags);
  const tagIndex: Record<string, number> = {};

  for (let i of allTags) {
    if (Object.keys(tagIndex).includes(i)) {
      tagIndex[i]! += 1;
    } else {
      tagIndex[i] = 1;
    }
  }

  return tagIndex;
});
</script>

<template>
  <HCommand cmd="find /blog/ -exec cat {} + | jq .tags | uniq">
    <HTitledSection title="Tag Index" with="h1">
      <p class="my-2">
        This page shows an index over all tags used throughout my blog.
        Click on one of the tag to see posts containing it.
      </p>

      <ul class="mt-6 list-disc pl-8">
        <li v-for="i_tag of Object.keys(tags)" :key="i_tag">
          <NuxtLink :to="{ name: 'blog', query: { tag: i_tag } }">#{{ i_tag }}</NuxtLink>
          <span> ({{ tags[i_tag] }} articles)</span>
        </li>
      </ul>
    </HTitledSection>
  </HCommand>
</template>
