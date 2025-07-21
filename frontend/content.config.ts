import { defineContentConfig, defineCollection, z } from '@nuxt/content'

export default defineContentConfig({
    collections: {
        blog: defineCollection({
            type: 'page',
            source: 'blog/*.md',
            schema: z.object({
                title: z.string(),
                author: z.string(),
                short_desc: z.string(),
                lang: z.enum(["en", "de"]),
                tags: z.array(z.string()),
                created_at: z.date(),
                edited_at: z.optional(z.date()),
                draft: z.boolean(),
            }),
        })
    }
})
