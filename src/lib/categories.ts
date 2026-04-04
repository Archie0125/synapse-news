export type CategorySlug = 'ai-ml' | 'startups' | 'products' | 'policy' | 'industry' | 'developer-tools' | 'hardware';

export interface Category {
  slug: CategorySlug;
  name: string;
  color: string;
}

export const CATEGORIES: Category[] = [
  { slug: 'ai-ml', name: 'AI & ML', color: '#8B5CF6' },
  { slug: 'startups', name: 'Startups', color: '#F59E0B' },
  { slug: 'products', name: 'Products', color: '#10B981' },
  { slug: 'policy', name: 'Policy', color: '#EF4444' },
  { slug: 'industry', name: 'Industry', color: '#3B82F6' },
  { slug: 'developer-tools', name: 'Dev Tools', color: '#06B6D4' },
  { slug: 'hardware', name: 'Hardware', color: '#F97316' },
];

export function getCategoryBySlug(slug: string): Category {
  return CATEGORIES.find(c => c.slug === slug) ?? CATEGORIES[4]; // default to industry
}

export function getCategoryColor(slug: string): string {
  return getCategoryBySlug(slug).color;
}
