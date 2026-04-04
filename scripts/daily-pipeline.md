# Daily FAQ Pipeline Prompt

Run the full daily news pipeline for FAQ. Follow these steps exactly:

## Step 1: Fetch RSS articles
```bash
cd C:/Users/A7/Desktop/news && python -m pipeline.main --phase fetch
```

## Step 2: Read raw articles and generate news
Read the raw articles saved in `data/raw/` (today's date folder). For each category (ai-ml, startups, products, policy, industry, developer-tools, hardware), pick the top 3 most newsworthy articles and write bilingual commentary articles.

For each article:
- Read the raw markdown file to understand the source material
- Write an EN version and a ZH version as separate files in `src/content/articles/`
- Follow the KOL commentary style in `prompts/generate_analysis.md`
- Filename format: `YYYY-MM-DD-slug-en.md` and `YYYY-MM-DD-slug-zh.md`
- Include proper frontmatter: title, summary, category, publishedAt, lang, sources, tags
- ZH version should be rewritten for Taiwanese readers, not translated
- Each article: 500-800 words, opinionated, with "What to Watch" section

## Step 3: Update site data
```bash
cd C:/Users/A7/Desktop/news && python -m pipeline.threads.poster --status
```

## Step 4: Build and verify
```bash
cd C:/Users/A7/Desktop/news && npx astro build
```

Report: how many articles were created, which categories, any errors.
