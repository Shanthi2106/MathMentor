"""OpenAI-compatible client from environment (direct OpenAI or Vercel AI Gateway)."""
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

VERCEL_AI_GATEWAY_URL = "https://ai-gateway.vercel.sh/v1"
# Tutor/backend/openai_env.py -> parents[1] == project root (same .env as backend/main.py).
_PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _refresh_env_from_dotenv() -> None:
    """Re-read .env on each LLM call so uvicorn workers and key edits stay aligned."""
    load_dotenv(_PROJECT_ROOT / ".env", override=True)


def normalize_openai_api_key(raw: str | None) -> str:
    """Strip BOM/whitespace and optional wrapping quotes from .env values."""
    s = (raw or "").strip().lstrip("\ufeff")
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        s = s[1:-1].strip()
    return s


def normalize_env_string(raw: str | None, *, default: str) -> str:
    """Same normalization for non-secret env values (e.g. OPENAI_MODEL)."""
    t = normalize_openai_api_key(raw)
    return t if t else default


def use_vercel_ai_gateway() -> bool:
    """
    Vercel AI Gateway: AI_GATEWAY_API_KEY + https://ai-gateway.vercel.sh/v1

    Precedence (avoids 401s from a bad OpenAI key stored only in Vercel BYOK):
    - USE_OPENAI_DIRECT=1 → always api.openai.com with OPENAI_API_KEY
    - USE_VERCEL_AI_GATEWAY=1 (or OPENAI_USE_GATEWAY) → gateway if AI_GATEWAY_API_KEY is set
    - Otherwise → if OPENAI_API_KEY is set, use direct OpenAI; else gateway if AI_GATEWAY_API_KEY is set
    """
    if (os.getenv("USE_OPENAI_DIRECT") or "").strip().lower() in ("1", "true", "yes"):
        return False
    gk = normalize_openai_api_key(os.getenv("AI_GATEWAY_API_KEY"))
    ok = normalize_openai_api_key(os.getenv("OPENAI_API_KEY"))
    flag = (os.getenv("USE_VERCEL_AI_GATEWAY") or os.getenv("OPENAI_USE_GATEWAY") or "").strip().lower()
    gateway_forced = flag in ("1", "true", "yes")
    if gateway_forced:
        return bool(gk)
    if ok:
        return False
    return bool(gk)


def is_vercel_gateway_base(url: str) -> bool:
    return "ai-gateway.vercel.sh" in (url or "")


def get_llm_credentials() -> tuple[str, str, str]:
    """
    Returns (api_key, base_url, provider).
    provider is \"vercel_ai_gateway\" or \"openai_direct\".
    """
    _refresh_env_from_dotenv()
    if use_vercel_ai_gateway():
        key = normalize_openai_api_key(os.getenv("AI_GATEWAY_API_KEY"))
        return key, VERCEL_AI_GATEWAY_URL, "vercel_ai_gateway"
    base = (os.getenv("OPENAI_BASE_URL") or "").strip() or "https://api.openai.com/v1"
    key = normalize_openai_api_key(os.getenv("OPENAI_API_KEY"))
    return key, base, "openai_direct"


def gateway_model_id(model: str, base_url: str) -> str:
    """Vercel AI Gateway expects provider-prefixed ids (e.g. openai/gpt-4o-mini)."""
    if not is_vercel_gateway_base(base_url):
        return model
    if "/" in model:
        return model
    return f"openai/{model}"


def create_openai_client(*, api_key: str, base_url: str) -> OpenAI:
    """
    Build the SDK client. Org/project headers apply only to direct OpenAI, not the gateway.
    """
    kwargs: dict = {"api_key": api_key, "base_url": base_url}
    if not is_vercel_gateway_base(base_url):
        org = (os.getenv("OPENAI_ORGANIZATION") or os.getenv("OPENAI_ORG_ID") or "").strip() or None
        project = (os.getenv("OPENAI_PROJECT") or os.getenv("OPENAI_PROJECT_ID") or "").strip() or None
        if org:
            kwargs["organization"] = org
        if project:
            kwargs["project"] = project
    return OpenAI(**kwargs)
