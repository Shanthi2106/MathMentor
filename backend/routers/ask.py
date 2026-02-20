"""
API for asking the math tutor a question.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field

from backend.services.tutor import answer_question

router = APIRouter()


class AskRequest(BaseModel):
    grade: int = Field(..., ge=1, le=12, description="Student grade (1–12)")
    question: str = Field(..., min_length=1, description="Math question")
    domain_id: str | None = Field(None, description="Optional Common Core domain id (e.g. OA, NBT)")


class AskResponse(BaseModel):
    answer: str
    error: str | None = None


@router.post("/", response_model=AskResponse)
def ask(req: AskRequest):
    """Submit a math question for the given grade. Response is aligned to USA Common Core."""
    answer, err = answer_question(grade=req.grade, question=req.question, domain_id=req.domain_id)
    return AskResponse(answer=answer, error=err)
