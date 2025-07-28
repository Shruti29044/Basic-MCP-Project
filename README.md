# MCP Python Project

## Features
- Claude-compatible MCP server
- PR template suggestion tool
- Slack notifications via webhook

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and set your Slack webhook:
```bash
cp .env.example .env
```

3. Run the server:
```bash
uvicorn mcp_server:app --port 8080
```

4. Use Cloudflare Tunnel to expose it:
```bash
cloudflared tunnel --url http://localhost:8080
```

## Endpoints
- `POST /tool/pr-template` — Suggests a PR template based on changed files
- `POST /prompt/slack-notify` — Sends Slack message
