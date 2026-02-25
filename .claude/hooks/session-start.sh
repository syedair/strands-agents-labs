#!/bin/bash
set -euo pipefail

# Only run in remote Claude Code on the web sessions
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install project dependencies using uv
cd "${CLAUDE_PROJECT_DIR:-$(pwd)}"
uv sync
