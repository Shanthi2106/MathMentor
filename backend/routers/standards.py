"""
API for Common Core math standards (grades and domains).
"""
from fastapi import APIRouter

from backend.health_payload import openai_health_status
from backend.standards import COMMON_CORE_MATH_BY_GRADE, STANDARDS_FOR_MATHEMATICAL_PRACTICE

router = APIRouter()


@router.get("/health")
def health_check(probe: bool = False):
    """Same payload as GET /api/health. ?probe=true runs a live auth check to the LLM base URL."""
    return openai_health_status(probe=probe)


@router.get("/grades")
def list_grades():
    """Return list of supported grades (1–12)."""
    return {"grades": list(COMMON_CORE_MATH_BY_GRADE.keys())}


@router.get("/grade/{grade_id}")
def get_grade_standards(grade_id: int):
    """Return domains and topics for a given grade."""
    if grade_id not in COMMON_CORE_MATH_BY_GRADE:
        return {"error": f"Grade {grade_id} not supported. Use 1–12."}
    return COMMON_CORE_MATH_BY_GRADE[grade_id]


@router.get("/practices")
def get_practices():
    """Return the eight Standards for Mathematical Practice."""
    return {"practices": STANDARDS_FOR_MATHEMATICAL_PRACTICE}
