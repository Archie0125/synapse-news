export type Lang = 'en' | 'zh';

export const LANGS: Lang[] = ['en', 'zh'];

export const DEFAULT_LANG: Lang = 'en';

export const LANG_LABELS: Record<Lang, string> = {
  en: 'English',
  zh: '繁體中文',
};

const translations = {
  en: {
    // Site
    'site.name': 'FAQ',
    'site.tagline': 'AI News',
    'site.description': 'AI-powered tech news, autonomously researched and published daily',
    'site.powered_by': 'Powered by AI',
    'site.all_content_ai': 'All content AI-generated.',

    // Navigation
    'nav.home': 'Home',
    'nav.search': 'Search',
    'nav.all': 'All',

    // Categories
    'cat.ai-ml': 'AI & ML',
    'cat.startups': 'Startups',
    'cat.products': 'Products',
    'cat.policy': 'Policy',
    'cat.industry': 'Industry',
    'cat.developer-tools': 'Dev Tools',
    'cat.hardware': 'Hardware',

    // Homepage
    'home.trending': 'Trending',
    'home.latest': 'Latest',
    'home.top_stories': 'Top Stories',
    'home.categories': 'Categories',
    'home.see_all': 'See all',
    'home.stay_updated': 'Stay updated',
    'home.subscribe_rss': 'Subscribe via RSS',

    // Article
    'article.analysis': 'Analysis',
    'article.sources': 'Sources',
    'article.related': 'Related Stories',
    'article.min_read': 'min read',
    'article.just_now': 'Just now',
    'article.minutes_ago': 'm ago',
    'article.hours_ago': 'h ago',
    'article.days_ago': 'd ago',

    // Sort
    'sort.label': 'Sort',
    'sort.latest': 'Latest',
    'sort.oldest': 'Oldest',
    'sort.featured': 'Featured',
    'sort.trending': 'Trending',
    'sort.analysis': 'Analysis',

    // All articles page
    'all.title': 'All Articles',
    'all.description': 'Browse every article published on this site.',

    // Category page
    'category.no_articles': 'No articles yet. The pipeline will populate this category soon.',

    // Footer
    'footer.rss': 'RSS',

    // Newsletter
    'newsletter.title': 'Weekly Top 10',
    'newsletter.description': 'Get the 10 most-read articles delivered every weekend.',
    'newsletter.placeholder': 'your@email.com',
    'newsletter.subscribe': 'Subscribe',
    'newsletter.thanks': 'Thanks for subscribing!',
  },
  zh: {
    // Site
    'site.name': 'FAQ',
    'site.tagline': 'AI 新聞',
    'site.description': '由 AI 驅動的科技新聞，每日自主研究與發佈',
    'site.powered_by': 'AI 驅動',
    'site.all_content_ai': '所有內容均由 AI 生成。',

    // Navigation
    'nav.home': '首頁',
    'nav.search': '搜尋',
    'nav.all': '全部',

    // Categories
    'cat.ai-ml': 'AI 與機器學習',
    'cat.startups': '新創公司',
    'cat.products': '產品',
    'cat.policy': '政策',
    'cat.industry': '產業',
    'cat.developer-tools': '開發工具',
    'cat.hardware': '硬體',

    // Homepage
    'home.trending': '熱門話題',
    'home.latest': '最新報導',
    'home.top_stories': '精選文章',
    'home.categories': '分類',
    'home.see_all': '查看全部',
    'home.stay_updated': '追蹤最新消息',
    'home.subscribe_rss': '訂閱 RSS',

    // Article
    'article.analysis': '深度分析',
    'article.sources': '資料來源',
    'article.related': '相關報導',
    'article.min_read': '分鐘閱讀',
    'article.just_now': '剛剛',
    'article.minutes_ago': '分鐘前',
    'article.hours_ago': '小時前',
    'article.days_ago': '天前',

    // Sort
    'sort.label': '排序',
    'sort.latest': '最新',
    'sort.oldest': '最舊',
    'sort.featured': '精選',
    'sort.trending': '熱門',
    'sort.analysis': '深度分析',

    // All articles page
    'all.title': '全部文章',
    'all.description': '瀏覽本站所有已發佈的文章。',

    // Category page
    'category.no_articles': '目前尚無文章，管線將很快補充此分類的內容。',

    // Footer
    'footer.rss': 'RSS 訂閱',

    // Newsletter
    'newsletter.title': '每週精選十大',
    'newsletter.description': '每週末收到最多人閱讀的 10 篇文章。',
    'newsletter.placeholder': 'your@email.com',
    'newsletter.subscribe': '訂閱',
    'newsletter.thanks': '感謝訂閱！',
  },
} as const;

type TranslationKey = keyof typeof translations.en;

export function t(lang: Lang, key: TranslationKey): string {
  return translations[lang]?.[key] ?? translations.en[key] ?? key;
}

export function getCategoryName(lang: Lang, slug: string): string {
  const key = `cat.${slug}` as TranslationKey;
  return t(lang, key);
}

export function getLocalizedUrl(lang: Lang, path: string): string {
  // Remove existing lang prefix if present
  const cleanPath = path.replace(/^\/(en|zh)\//, '/');
  return `/${lang}${cleanPath === '/' ? '/' : cleanPath}`;
}

export function formatDateLocalized(date: Date, lang: Lang): string {
  const locale = lang === 'zh' ? 'zh-TW' : 'en-US';
  return date.toLocaleDateString(locale, {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}

export function getRelativeTimeLocalized(date: Date, lang: Lang): string {
  const now = new Date();
  const diff = now.getTime() - date.getTime();
  const minutes = Math.floor(diff / (1000 * 60));
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);

  if (minutes < 1) return t(lang, 'article.just_now');
  if (minutes < 60) {
    const sep = lang === 'zh' ? ' ' : '';
    return `${minutes}${sep}${t(lang, 'article.minutes_ago')}`;
  }
  if (hours < 24) {
    const sep = lang === 'zh' ? ' ' : '';
    return `${hours}${sep}${t(lang, 'article.hours_ago')}`;
  }
  if (days < 7) {
    const sep = lang === 'zh' ? ' ' : '';
    return `${days}${sep}${t(lang, 'article.days_ago')}`;
  }
  return formatDateLocalized(date, lang);
}

export function getReadingTimeLocalized(content: string, lang: Lang): string {
  const words = content.trim().split(/\s+/).length;
  const minutes = Math.max(1, Math.round(words / 230));
  return `${minutes} ${t(lang, 'article.min_read')}`;
}

export function getAlternateUrl(currentPath: string, fromLang: Lang, toLang: Lang): string {
  if (currentPath === '/' || currentPath === '') return `/${toLang}/`;
  let alt = currentPath.replace(`/${fromLang}/`, `/${toLang}/`);
  // Swap slug language suffix (-en/-zh) at end of path
  alt = alt.replace(new RegExp(`-${fromLang}(\/?)$`), `-${toLang}$1`);
  return alt || `/${toLang}/`;
}
