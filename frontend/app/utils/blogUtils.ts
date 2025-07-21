import type {BlogCollectionItem} from "@nuxt/content";

export function articlePathComponents(article: Pick<BlogCollectionItem, "num" | "title">): { num: number, id: string, slug: string } {
    return {
        num: article.num,
        id: article.num.toString().padStart(3, "0"),
        slug: `-${urlsafeTitle(article.title)}`,
    }
}

function urlsafeTitle(title: string): string {
    return title.toLowerCase().replaceAll(/[/ ?_]/g, "-")
}
