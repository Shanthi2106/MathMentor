"""
Math Mentor API – answers mathematics questions for grades 1–12
aligned to USA Common Core State Standards.
"""
from pathlib import Path
import os
from dotenv import load_dotenv

# override=True: values in project-root .env win over stale OPENAI_API_KEY in the shell/Windows user env.
load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.health_payload import openai_health_status
from backend.routers import standards, ask

app = FastAPI(
    title="Math Mentor API",
    description="Mathematics tutor for grades 1–12 aligned to Common Core State Standards.",
    version="1.0.0",
)

# Allow frontend origin from env (e.g. Vercel URL); keep local dev origins.
_frontend_origin = os.getenv("FRONTEND_ORIGIN", "").strip()
_origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
if _frontend_origin:
    _origins.append(_frontend_origin.rstrip("/"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(standards.router, prefix="/api/standards", tags=["standards"])
app.include_router(ask.router, prefix="/api/ask", tags=["ask"])


@app.get("/")
def root():
    return {"message": "Math Mentor API", "docs": "/docs"}


@app.get("/api")
def api_index():
    """Browsing /api alone returns 404 without this; lists real routes."""
    return {
        "message": "Math Mentor API",
        "docs": "/docs",
        "endpoints": {
            "health": "GET /api/health?probe=true (alias: /api/standards/health?probe=true)",
            "standards_grades": "GET /api/standards/grades",
            "standards_grade": "GET /api/standards/grade/{1-12}",
            "standards_practices": "GET /api/standards/practices",
            "ask": "POST /api/ask/",
        },
    }


@app.get("/api/health")
def api_health(probe: bool = False):
    """Non-secret LLM hints. Add ?probe=true to run a live models.list auth check."""
    return openai_health_status(probe=probe)
