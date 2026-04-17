"""Shared JSON for API health / LLM config hints (no secrets)."""
import os

from backend.openai_env import (
    create_openai_client,
    get_llm_credentials,
    normalize_openai_api_key,
    use_vercel_ai_gateway,
)


def _strip_optional_quotes(value: str) -> str:
    s = value.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1].strip()
    return s


def _probe_llm(api_key: str, base_url: str) -> dict:
    """One lightweight call to verify auth; error text truncated, no secrets."""
    if not api_key:
        return {"ok": False, "error": "no_api_key"}
    try:
        client = create_openai_client(api_key=api_key, base_url=base_url)
        page = client.models.list()
        if getattr(page, "data", None):
            return {"ok": True, "error": None}
        return {"ok": True, "error": None}
    except Exception as e:
        return {"ok": False, "error": str(e)[:500]}


def openai_health_status(*, probe: bool = False) -> dict:
    key, base, provider = get_llm_credentials()
    model_raw = os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
    out = {
        "ok": True,
        "llm_provider": provider,
        "llm_base_url": base,
        "llm_key_configured": bool(key),
        "llm_key_last4": key[-4:] if len(key) >= 4 else None,
        "use_vercel_ai_gateway": use_vercel_ai_gateway(),
        "openai_api_key_present": bool(normalize_openai_api_key(os.getenv("OPENAI_API_KEY"))),
        "ai_gateway_api_key_present": bool(normalize_openai_api_key(os.getenv("AI_GATEWAY_API_KEY"))),
        "openai_model": _strip_optional_quotes(model_raw),
        "openai_org_set": bool((os.getenv("OPENAI_ORGANIZATION") or os.getenv("OPENAI_ORG_ID") or "").strip()),
        "openai_project_set": bool((os.getenv("OPENAI_PROJECT") or os.getenv("OPENAI_PROJECT_ID") or "").strip()),
    }
    if probe:
        out["llm_probe"] = _probe_llm(key, base)
    return out
