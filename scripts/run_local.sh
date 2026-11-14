#!/bin/zsh
# launchd entry: 02:00 Asia/Taipei. CLI-only, never opens a browser.
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
    echo "== validating production build"
    if ! npx astro build; then
      RC=4
      echo "ERROR: production build failed; staged changes were not committed or pushed"
    else
      git -c user.name="Synapse Bot" -c user.email="bot@synapse-news.ai" commit -q -m "chore: local pipeline run $(date +%Y-%m-%d_%H%M)"
      echo "committed $(git rev-parse --short HEAD) on $BR"
      if [ "${ROUTER_PUSH:-0}" = "1" ]; then
        if git push origin "$BR:master"; then
          echo "pushed to origin/master"
        else
          RC=5
          echo "ERROR: push to origin/master failed"
        fi
      else
        echo "push disabled (ROUTER_PUSH!=1)"
      fi
    fi
  else echo "no new articles"; fi
else
  osascript -e "display notification \"FAQ pipeline failed rc=$RC, see $LOG\" with title \"synapse-news\"" 2>/dev/null
fi
if [ $RC -ne 0 ]; then
  osascript -e "display notification \"FAQ daily update failed rc=$RC, see $LOG\" with title \"synapse-news\"" 2>/dev/null
fi
echo "== end $(date) rc=$RC"; exit $RC
