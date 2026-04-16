import { getCollection } from 'astro:content';
import { SITE } from '../data/site';
import { CATEGORIES } from '../lib/categories';
import { renderSitemapIndex, xmlResponse } from '../lib/sitemap';

export const prerender = true;

export async function GET() {
  const articles = await getCollection('articles');

  const lastmodByCategory: Record<string, string> = {};
  let globalLastmod: string | undefined;
  for (const a of articles) {
    const iso = a.data.publishedAt.toISOString();
    const cat = a.data.category;
    if (!lastmodByCategory[cat] || iso > lastmodByCategory[cat]) {
      lastmodByCategory[cat] = iso;
    }
    if (!globalLastmod || iso > globalLastmod) {
      globalLastmod = iso;
    }
  }

  const sitemaps = [
    { loc: `${SITE.url}/sitemap-pages.xml`, lastmod: globalLastmod },
    ...CATEGORIES.map((c) => ({
      loc: `${SITE.url}/sitemap-${c.slug}.xml`,
      lastmod: lastmodByCategory[c.slug],
    })),
    { loc: `${SITE.url}/news-sitemap.xml`, lastmod: globalLastmod },
  ];

  return xmlResponse(renderSitemapIndex(sitemaps));
}
