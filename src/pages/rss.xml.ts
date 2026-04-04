import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE } from '../data/site';

export async function GET(context: any) {
  const articles = await getCollection('articles');
  const enArticles = articles
    .filter(a => a.data.lang === 'en')
    .sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());

  return rss({
    title: SITE.name,
    description: SITE.description,
    site: context.site,
    items: enArticles.slice(0, 50).map(article => ({
      title: article.data.title,
      pubDate: article.data.publishedAt,
      description: article.data.summary,
      link: `/en/${article.data.category}/${article.id}/`,
      categories: [article.data.category, ...article.data.tags],
    })),
  });
}
