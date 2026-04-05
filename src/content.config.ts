import { z, defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles' }),
  schema: z.object({
    title: z.string().max(120),
    summary: z.string().max(1000),
    category: z.enum(['ai-ml', 'startups', 'products', 'policy', 'industry', 'developer-tools', 'hardware']),
    publishedAt: z.coerce.date(),
    featured: z.boolean().default(false),
    trending: z.boolean().default(false),
    sources: z.array(z.object({
      name: z.string(),
      url: z.string(),
    })).default([]),
    relatedSlugs: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    type: z.enum(['news', 'analysis']).default('news'),
    lang: z.enum(['en', 'zh']).default('en'),
  }),
});

export const collections = { articles };
