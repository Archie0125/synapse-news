export const prerender = false;

import { Redis } from '@upstash/redis';
import type { APIRoute } from 'astro';

const redis = new Redis({
  url: import.meta.env.UPSTASH_REDIS_REST_URL || process.env.UPSTASH_REDIS_REST_URL || '',
  token: import.meta.env.UPSTASH_REDIS_REST_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN || '',
});

// POST /api/views — increment view count for a slug
export const POST: APIRoute = async ({ request }) => {
  try {
    const { slug } = await request.json();
    if (!slug || typeof slug !== 'string') {
      return new Response(JSON.stringify({ error: 'slug required' }), { status: 400 });
    }

    const key = `views:${slug}`;
    const count = await redis.incr(key);

    return new Response(JSON.stringify({ slug, views: count }), {
      headers: { 'Content-Type': 'application/json' },
    });
  } catch {
    return new Response(JSON.stringify({ error: 'failed' }), { status: 500 });
  }
};

// GET /api/views?slugs=slug1,slug2,slug3 — get view counts
export const GET: APIRoute = async ({ url }) => {
  try {
    const slugsParam = url.searchParams.get('slugs');
    if (!slugsParam) {
      return new Response(JSON.stringify({ error: 'slugs param required' }), { status: 400 });
    }

    const slugs = slugsParam.split(',').slice(0, 50);
    const keys = slugs.map(s => `views:${s}`);
    const counts = await redis.mget<number[]>(...keys);

    const result: Record<string, number> = {};
    slugs.forEach((slug, i) => {
      result[slug] = counts[i] ?? 0;
    });

    return new Response(JSON.stringify(result), {
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, s-maxage=60',
      },
    });
  } catch {
    return new Response(JSON.stringify({ error: 'failed' }), { status: 500 });
  }
};
