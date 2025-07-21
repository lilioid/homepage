<script setup lang="ts">
import type { BlogCollectionItem } from "@nuxt/content";

const props = defineProps<{
  article: Pick<BlogCollectionItem, "title" | "author" | "tags" | "lang" | "short_desc" | "created_at" | "edited_at">,
}>();

const created_at_date = computed(() => new Date(Date.parse(props.article.created_at)));
const edited_at_date = computed(() => props.article.edited_at != null ? new Date(Date.parse(props.article.edited_at)) : null);
</script>

<template>
  <div class="">
    <ul class="flex flex-col items-end text-end">
      <li>
        <span>by </span>
        <span>{{ props.article.author }}</span>
      </li>

      <li>
        <ul class="flex gap-1 justify-end ">
          <li>
            <a href="/blog/index.html?lang={{ props.article.lang }}" class="text-yellow1 hover:text-black1 hover:bg-yellow1">#{{ props.article.lang }}</a>
          </li>
          <li v-for="i_tag in props.article.tags" :key="i_tag">
            <a :href="`/blog/index.html?tag=${i_tag}`" class="text-yellow1 hover:text-black1 hover:bg-yellow1">#{{ i_tag }}</a>
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

    <p class="italic px-4 mt-1">{{ props.article.short_desc }}</p>
  </div>
</template>
