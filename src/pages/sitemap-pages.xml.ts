import { SITE } from '../data/site';
import { CATEGORIES } from '../lib/categories';
import { renderUrlset, xmlResponse, type SitemapEntry } from '../lib/sitemap';

export const prerender = true;

export async function GET() {
  const entries: SitemapEntry[] = [
    { loc: `${SITE.url}/`, changefreq: 'daily', priority: 1.0 },
    { loc: `${SITE.url}/en/`, changefreq: 'daily', priority: 0.9 },
    { loc: `${SITE.url}/zh/`, changefreq: 'daily', priority: 0.9 },
    ...CATEGORIES.flatMap((c): SitemapEntry[] => [
      { loc: `${SITE.url}/en/${c.slug}/`, changefreq: 'daily', priority: 0.8 },
      { loc: `${SITE.url}/zh/${c.slug}/`, changefreq: 'daily', priority: 0.8 },
    ]),
    { loc: `${SITE.url}/en/threads/`, changefreq: 'weekly', priority: 0.5 },
    { loc: `${SITE.url}/zh/threads/`, changefreq: 'weekly', priority: 0.5 },
  ];

  return xmlResponse(renderUrlset(entries));
}
