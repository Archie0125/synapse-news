import { Redis } from '@upstash/redis';

// Vercel's Upstash Marketplace integration may inject either the classic
// UPSTASH_* names or the Vercel-KV-style KV_REST_API_* names depending on the
// prefix chosen at provisioning time — accept both so the choice can't
// silently break the API routes. Empty-string fallbacks keep the client
// constructible when nothing is configured; requests then fail and callers'
// catch blocks degrade gracefully (counters show "—").
function env(name: string): string | undefined {
  return (import.meta.env as Record<string, string | undefined>)[name] ?? process.env[name];
}

export const redis = new Redis({
  url: env('UPSTASH_REDIS_REST_URL') || env('KV_REST_API_URL') || '',
  token: env('UPSTASH_REDIS_REST_TOKEN') || env('KV_REST_API_TOKEN') || '',
});
