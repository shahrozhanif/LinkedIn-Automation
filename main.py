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
    global latest_post

    if payload.status == "rejected":
        N8N_WEBHOOK = "http://n8n:5678/webhook/f5323699-6a4f-474c-a0c7-9ab1bff6b7d3"
        async with httpx.AsyncClient() as client:
            await client.post(N8N_WEBHOOK, json=payload.model_dump())
    
    # Clear the post regardless of approve or reject
    latest_post = {"title": "", "body": ""}
    
    return {"status": payload.status}

# Serve the React frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")