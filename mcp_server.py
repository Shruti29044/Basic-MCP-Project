from fastapi import FastAPI, Request
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # <- Load .env variables

app = FastAPI()

SLACK_WEBHOOK_URL = os.getenv("https://hooks.slack.com/services/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")



app = FastAPI()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

@app.post("/tool/pr-template")
async def suggest_template(request: Request):
    body = await request.json()
    changed_files = body.get("files", [])
    if any("docs/" in f for f in changed_files):
        return {"template": "📄 Documentation Update"}
    elif any("test/" in f for f in changed_files):
        return {"template": "🧪 Test Improvement"}
    else:
        return {"template": "✨ Feature Implementation"}

@app.post("/prompt/slack-notify")
async def slack_notify(request: Request):
    data = await request.json()
    message = data.get("message", "Deployment status unknown.")
    if SLACK_WEBHOOK_URL:
        requests.post(SLACK_WEBHOOK_URL, json={"text": message})
        return {"status": "sent"}
    return {"status": "failed", "reason": "No webhook URL set"}
