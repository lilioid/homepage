<script setup lang="ts">
import type {BlogCollectionItem} from "@nuxt/content";

const props = defineProps<{
  article: Pick<BlogCollectionItem, "title" | "author" | "tags" | "lang" | "short_desc" | "created_at" | "edited_at">,
}>();

const created_at_date = computed(() => new Date(Date.parse(props.article.created_at)));
const edited_at_date = computed(() => props.article.edited_at != null ? new Date(Date.parse(props.article.edited_at)) : null);
</script>

<template>
  <ul class="flex flex-col items-end text-end">
    <li>
      <span>by </span>
      <span>{{ props.article.author }}</span>
    </li>

    <li>
      <ul class="flex gap-1 justify-end ">
        <li>
          <NuxtLink :to="{ name: 'blog', query: { lang: props.article.lang } }"
                    exact-active-class="lang-exact-active"
             class="text-yellow1 hover:text-black1 hover:bg-yellow1">#{{ props.article.lang }}</NuxtLink>
        </li>
        <li v-for="i_tag in props.article.tags" :key="i_tag">
          <NuxtLink :to="{ name: 'blog', query: { tag: i_tag } }" exact-active-class="tag-exact-active" class="text-yellow1 hover:text-black1 hover:bg-yellow1">#{{
              i_tag
            }}</NuxtLink>
        </li>
      </ul>
    </li>

    <li class="date">
      <span>Written on  </span>
      <time datetime="{{ props.article.created_at }}">{{ created_at_date.toDateString() }}</time>
      <span v-if="props.article.edited_at && edited_at_date">
        <span>, last edit on </span>
        <time datetime="{{ props.article.edited_at }}">{{ edited_at_date.toDateString() }}</time>
      </span>
    </li>
  </ul>
</template>
