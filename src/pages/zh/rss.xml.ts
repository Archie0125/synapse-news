import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE } from '../../data/site';

export async function GET(context: any) {
  const articles = await getCollection('articles');
  const zhArticles = articles
    .filter(a => a.data.lang === 'zh')
    .sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());

  return rss({
    title: `${SITE.name} — AI 新聞`,
    description: '由 AI 驅動的科技新聞，每日自主研究與發佈',
    site: context.site,
    items: zhArticles.slice(0, 50).map(article => ({
      title: article.data.title,
      pubDate: article.data.publishedAt,
      description: article.data.summary,
      link: `/zh/${article.data.category}/${article.id}/`,
      categories: [article.data.category, ...article.data.tags],
    })),
  });
}
