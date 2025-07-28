<<<<<<< HEAD
<<<<<<< HEAD
# MCP Python Project

## Features
- Claude-compatible MCP server
- PR template suggestion tool
- Slack notifications via webhook

## Setup

1. Install dependencies:
=======
# Basic MCP Server (Python)

This project is a simple starter implementation of an **MCP-compatible** server for use with tools like **Claude Code**. It includes:

- 🛠 A basic tool: `/tool/pr-template`
- 🔔 A basic prompt endpoint: `/prompt/slack-notify`
- ✅ Slack integration via webhook

---

## 🚀 Features

### ✅ Endpoints

| Endpoint                  | Description                              |
|---------------------------|------------------------------------------|
| `POST /tool/pr-template`  | Suggests a PR template based on file names |
| `POST /prompt/slack-notify` | Sends a plain Slack message              |

---

## 🧰 Setup Instructions

### 1. Clone or extract this repo

```bash
cd mcp_project
````

### 2. Install dependencies

>>>>>>> 3d17cbafbdc3190d8bf1c35880751c5a4d622c7a
```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
2. Copy `.env.example` to `.env` and set your Slack webhook:
```bash
cp .env.example .env
```

3. Run the server:
=======
### 3. Configure `.env`

Create your `.env` file from the example:

```bash
copy .env.example .env  # On Windows
# OR
cp .env.example .env    # On Linux/macOS
```

Then open `.env` and paste your actual Slack webhook URL:

```env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/real/webhook
```

---

### 4. Run the server

>>>>>>> 3d17cbafbdc3190d8bf1c35880751c5a4d622c7a
```bash
uvicorn mcp_server:app --port 8080
```

<<<<<<< HEAD
4. Use Cloudflare Tunnel to expose it:
```bash
cloudflared tunnel --url http://localhost:8080
```

## Endpoints
- `POST /tool/pr-template` — Suggests a PR template based on changed files
- `POST /prompt/slack-notify` — Sends Slack message
=======
Your server will be live at:
[http://localhost:8080](http://localhost:8080)

---

## 🧪 Test the Endpoints

### Send PR Template Request

```bash
curl -X POST http://localhost:8080/tool/pr-template ^
  -H "Content-Type: application/json" ^
  -d "{\"files\": [\"docs/README.md\", \"src/app.py\"]}"
```

### Send Slack Notification

```bash
curl -X POST http://localhost:8080/prompt/slack-notify ^
  -H "Content-Type: application/json" ^
  -d "{\"message\": \"✅ Hello from my MCP server!\"}"
```

You should see the message appear in your Slack channel.

---

## 📌 Notes

* This project is based on the **MCP model** used by Claude Code and Hugging Face's automation tutorials.
* `.env` variables are loaded using `python-dotenv`.
* The Slack webhook is used via a POST request — don't share it publicly!

---

## 🧠 Next Steps

* Add GitHub webhook integration
* Format Slack messages with Block Kit or markdown
* Create MCP-compliant prompts for automated workflows

```
=======
>>>>>>> 410f9820a3c82b4e881e63a9721e640f409072a8

>>>>>>> 3d17cbafbdc3190d8bf1c35880751c5a4d622c7a
