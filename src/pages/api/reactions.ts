export const prerender = false;

import type { APIRoute } from 'astro';
import { redis } from '../../lib/redis';

type Reaction = 'like' | 'dislike';
const REACTIONS: Reaction[] = ['like', 'dislike'];

const clamp = (n: unknown) => Math.max(0, Number(n) || 0);

function isValidVote(v: unknown): v is Reaction | null {
  return v === null || REACTIONS.includes(v as Reaction);
}

// POST /api/reactions — apply a vote transition for a slug.
// Body: { slug, vote: 'like'|'dislike'|null, prev: 'like'|'dislike'|null }
// The server derives the counter deltas from (prev → vote), so a client can
// never move a counter by more than 1 per request.
export const POST: APIRoute = async ({ request }) => {
  try {
    const { slug, vote, prev } = await request.json();
    if (!slug || typeof slug !== 'string' || slug.length > 200) {
      return new Response(JSON.stringify({ error: 'slug required' }), { status: 400 });
    }
    if (!isValidVote(vote) || !isValidVote(prev)) {
      return new Response(JSON.stringify({ error: 'invalid vote' }), { status: 400 });
    }

    const likesKey = `likes:${slug}`;
    const dislikesKey = `dislikes:${slug}`;

    const pipeline = redis.pipeline();
    if (vote !== prev) {
      if (prev) pipeline.decr(`${prev}s:${slug}`);
      if (vote) pipeline.incr(`${vote}s:${slug}`);
    }
    pipeline.get(likesKey);
    pipeline.get(dislikesKey);
    const results = await pipeline.exec<(number | string | null)[]>();

    // An untracked client can DECR a counter it never incremented; reset
    // anything that went negative so counts stay honest.
    const likes = Number(results[results.length - 2]) || 0;
    const dislikes = Number(results[results.length - 1]) || 0;
    if (likes < 0) redis.set(likesKey, 0).catch(() => {});
    if (dislikes < 0) redis.set(dislikesKey, 0).catch(() => {});

    return new Response(
      JSON.stringify({ slug, likes: clamp(likes), dislikes: clamp(dislikes) }),
      { headers: { 'Content-Type': 'application/json' } },
    );
  } catch {
    return new Response(JSON.stringify({ error: 'failed' }), { status: 500 });
  }
};

// GET /api/reactions?slugs=a,b,c — batch-read like/dislike counts
export const GET: APIRoute = async ({ url }) => {
  try {
    const slugsParam = url.searchParams.get('slugs');
    if (!slugsParam) {
      return new Response(JSON.stringify({ error: 'slugs param required' }), { status: 400 });
    }

    const slugs = slugsParam.split(',').slice(0, 50);
    const keys = slugs.flatMap(s => [`likes:${s}`, `dislikes:${s}`]);
    const counts = await redis.mget<(number | null)[]>(...keys);

    const result: Record<string, { likes: number; dislikes: number }> = {};
    slugs.forEach((slug, i) => {
      result[slug] = { likes: clamp(counts[i * 2]), dislikes: clamp(counts[i * 2 + 1]) };
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
