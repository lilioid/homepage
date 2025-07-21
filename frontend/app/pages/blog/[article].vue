<script setup lang="ts">
import type {RouteLocationNormalized} from "#vue-router";

definePageMeta({
  name: "blog-article",
  path: "/blog/:postNum(\\d+):postSlug(-[^/]+)?:fileType(\\.html)?",
  middleware: [
    defineNuxtRouteMiddleware(async (to, _from) => {
      // extract route parameters and find matching article
      const articleNum = Number(to.params.postNum!);
      const article = await queryCollection("blog").where("num", "=", articleNum).first();
      const pathComponents = articlePathComponents(article!);

      // construct canonical article url
      const router = useRouter();
      const canonicalRoute = router.resolve({ name: "blog-article", params: { postNum: pathComponents.id, postSlug: pathComponents.slug, fileType: ".html"} })

      // redirect to canonical url if required
      if (to.fullPath != canonicalRoute.fullPath) {
        return navigateTo(canonicalRoute);
      }
    }),
  ]
});

const route = useRoute();
const { data: article } = await useAsyncData(route.path, () => {
  const articleNum = Number(route.params.postNum!);
  return queryCollection("blog").where("num", "=", articleNum).first()
});
</script>

<template>
  <HCommand :cmd="`cat ${route.path}`">
    <div v-if="article">
      <ProseH1 class="text-3xl font-extrabold my-2">{{ article.title }}</ProseH1>
      <HBlogArticleMetadata :article="article" class="mb-8" />
      <ContentRenderer :value="article" />
    </div>
  </HCommand>
</template>
