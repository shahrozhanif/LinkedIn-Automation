from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store
latest_post = {"title": "", "body": ""}

class Post(BaseModel):
    title: str
    body: str

class ApprovalPayload(BaseModel):
    status: str
    reason: Optional[str] = None

@app.post("/post")
def receive_post(post: Post):
    latest_post["title"] = post.title
    latest_post["body"] = post.body
    return {"status": "received"}

@app.get("/post")
def get_post():
    return latest_post

@app.post("/approve")
async def approve(payload: ApprovalPayload):
    import httpx
    N8N_WEBHOOK = "http://n8n:5678/webhook-test/16723437-e7f7-419c-9a2d-8bef08a74489"
    async with httpx.AsyncClient() as client:
        await client.post(N8N_WEBHOOK, json=payload.dict())
    return {"status": "forwarded"}

# Serve the React frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")