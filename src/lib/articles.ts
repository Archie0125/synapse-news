import { getCollection } from 'astro:content';

// The production site was last intentionally published through 2026-08-03.
// Later local-preview drafts are hidden unless the repaired publisher marks
// them safeForPublic after the editorial and source-link gates pass.
const LEGACY_PUBLIC_CUTOFF = Date.parse('2026-08-04T00:00:00.000Z');

export function isPublicArticle(article: {
  data: { publishedAt: Date; safeForPublic?: boolean };
}): boolean {
  return article.data.safeForPublic === true
    || article.data.publishedAt.getTime() < LEGACY_PUBLIC_CUTOFF;
}

export async function getPublicArticles() {
  const articles = await getCollection('articles');
  return articles.filter(isPublicArticle);
}
