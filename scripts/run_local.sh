#!/bin/zsh
# launchd entry: 14:00 & 02:00 Asia/Taipei. CLI-only, never opens a browser.
# Push to origin only when ROUTER_PUSH=1 (set in launchd plist when approved).
set -u
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/Applications/Codex.app/Contents/Resources:$HOME/.nvm/versions/node/v22.23.1/bin:/usr/bin:/bin"
export BROWSER=none
cd "$HOME/Projects/synapse-news" || exit 1
mkdir -p logs; LOG="logs/run-$(date +%Y%m%d-%H%M).log"
exec >>"$LOG" 2>&1
echo "== start $(date)"; BR=auto/local-pipeline
git checkout -q "$BR" 2>/dev/null || git checkout -q -b "$BR"
.venv/bin/python scripts/run_local.py "$@"; RC=$?
echo "== pipeline rc=$RC"
if [ $RC -eq 0 ]; then
  git add data/ src/content/articles/ 2>/dev/null
  if ! git diff --staged --quiet; then
    git -c user.name="Synapse Bot" -c user.email="bot@synapse-news.ai" commit -q -m "chore: local pipeline run $(date +%Y-%m-%d_%H%M)"
    echo "committed $(git rev-parse --short HEAD) on $BR"
    if [ "${ROUTER_PUSH:-0}" = "1" ]; then
      npx astro build >/dev/null && git push origin "$BR:master" && echo "pushed to origin/master"
    else echo "push disabled (ROUTER_PUSH!=1)"; fi
  else echo "no new articles"; fi
else
  osascript -e "display notification \"FAQ pipeline failed rc=$RC, see $LOG\" with title \"synapse-news\"" 2>/dev/null
fi
echo "== end $(date) rc=$RC"; exit $RC
