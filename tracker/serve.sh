#!/usr/bin/env bash
# Local dashboard server with saved progress. Run: ./tracker/serve.sh
set -euo pipefail
cd "$(dirname "$0")"
PORT="${PORT:-8765}"

if pids=$(lsof -tiTCP:"${PORT}" -sTCP:LISTEN 2>/dev/null); then
  echo "Stopping existing process on port ${PORT}..."
  kill ${pids} 2>/dev/null || true
  sleep 0.5
fi

exec python3 server.py
