import { getCollection } from 'astro:content';
import { SITE } from '../data/site';
import { CATEGORIES } from '../lib/categories';
import { renderUrlset, xmlResponse, type SitemapEntry } from '../lib/sitemap';

export const prerender = true;

export function getStaticPaths() {
  return CATEGORIES.map((c) => ({ params: { category: c.slug } }));
}

export async function GET({ params }: { params: { category: string } }) {
  const articles = await getCollection('articles');
  const filtered = articles
    .filter((a) => a.data.category === params.category)
    .sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());

  const entries: SitemapEntry[] = filtered.map((a) => ({
    loc: `${SITE.url}/${a.data.lang}/${a.data.category}/${a.id}/`,
    lastmod: a.data.publishedAt.toISOString(),
    changefreq: 'monthly',
    priority: 0.7,
  }));

  return xmlResponse(renderUrlset(entries));
}
