"""
Math Mentor API – answers mathematics questions for grades 1–12
aligned to USA Common Core State Standards.
"""
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
