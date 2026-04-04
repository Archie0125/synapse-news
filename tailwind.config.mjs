/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      fontFamily: {
        headline: ['Playfair Display', 'Georgia', 'serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
      colors: {
        surface: 'var(--color-surface)',
        border: 'var(--color-border)',
        muted: 'var(--color-text-muted)',
        accent: 'var(--color-accent)',
        'cat-ai': '#8B5CF6',
        'cat-startups': '#F59E0B',
        'cat-products': '#10B981',
        'cat-policy': '#EF4444',
        'cat-industry': '#3B82F6',
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '680px',
          },
        },
      },
    },
  },
  plugins: [],
};
