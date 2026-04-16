import { getCollection } from 'astro:content';
import { SITE } from '../data/site';

export const prerender = true;

function xmlEscape(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

export async function GET() {
  const articles = await getCollection('articles');
  // Google News crawls articles published in the last ~2 days.
  // Use start-of-day 2 days ago so midnight-timestamped articles are included.
  const cutoff = new Date();
  cutoff.setUTCHours(0, 0, 0, 0);
  cutoff.setUTCDate(cutoff.getUTCDate() - 2);
  const cutoffMs = cutoff.getTime();

  const recent = articles
    .filter((a) => a.data.publishedAt.getTime() >= cutoffMs)
    .sort((a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());

  const items = recent
    .map((a) => {
      const url = `${SITE.url}/${a.data.lang}/${a.data.category}/${a.id}/`;
      const language = a.data.lang === 'zh' ? 'zh-TW' : 'en';
      return `  <url>
    <loc>${xmlEscape(url)}</loc>
    <news:news>
      <news:publication>
        <news:name>${xmlEscape(SITE.name)}</news:name>
        <news:language>${language}</news:language>
      </news:publication>
      <news:publication_date>${a.data.publishedAt.toISOString()}</news:publication_date>
      <news:title>${xmlEscape(a.data.title)}</news:title>
    </news:news>
  </url>`;
    })
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
${items}
</urlset>
`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml; charset=UTF-8' },
  });
}
