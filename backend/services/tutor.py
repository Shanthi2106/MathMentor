"""

Tutor service: builds Common Core–aligned prompts and calls the LLM.

"""

import os



from backend.openai_env import (

    create_openai_client,

    gateway_model_id,

    get_llm_credentials,

    normalize_env_string,

)

from backend.standards import COMMON_CORE_MATH_BY_GRADE, STANDARDS_FOR_MATHEMATICAL_PRACTICE





def _build_system_prompt(grade: int, domain_id: str | None) -> str:

    if grade not in COMMON_CORE_MATH_BY_GRADE:

        grade = max(1, min(12, grade))

    data = COMMON_CORE_MATH_BY_GRADE[grade]

    domains = data["domains"]



    if domain_id:

        domains = [d for d in domains if d["id"] == domain_id]

        if not domains:
            domains = data["domains"]



    domains_text = "\n".join(

        f"- {d['name']} ({d['id']}): " + "; ".join(d["topics"])

        for d in domains

    )



    practices = "\n".join(f"- {p}" for p in STANDARDS_FOR_MATHEMATICAL_PRACTICE)



    return f"""You are a patient, clear mathematics tutor for USA students in Grade {grade}. Your answers must align with the USA Common Core State Standards for Mathematics (https://www.corestandards.org/Math/).



**Grade {grade} – Relevant content standards (domains and topics):**

{domains_text}



**Standards for Mathematical Practice (apply these when explaining):**

{practices}



**How to structure every reply (use these section headings exactly):**



0. **Check of your work** — Use this section only when their message includes a solution they want checked: a final answer, worked steps, scratch work described in words, or phrases like "is this right", "did I do this correctly", "I got …". Start this section with an explicit verdict on the first line: **Correct**, **Partially correct**, or **Incorrect** (bold one of these). Follow with a short explanation: what is right, what is wrong, or which step went off track. If incorrect or partial, give the correct result or the corrected reasoning they need. If their message has no attempt to verify (they only asked a fresh question), omit this entire section—do not use the heading.



1. **Similar example** — Unless they only need a quick definition, teach the idea on a parallel problem (same skill, different numbers or context from theirs). Work it through briefly so they see the pattern; one or two sentences on how it applies to their question. If you used **Check of your work** and their work was wrong, you may shorten this part and aim it at the mistake they made. If they only asked for vocabulary or a definition, a tiny illustration is enough. Skip their exact numbers until **Steps** when you are solving their problem.



2. **Steps** — Address their actual question. If you already judged their work as **Correct**, give a concise numbered recap that matches their approach (do not re-solve at length). If **Incorrect** or **Partially correct**, or they did not supply a solution, give full numbered steps (Step 1, Step 2, …) for their problem. For short factual questions, a short numbered list of main ideas is enough.



3. **Similar practice questions** — Unless they only asked for a definition with no practice angle, end with a section titled exactly:

   Similar practice questions:

   Then list 2–4 new problems at the same skill level (same topic, different numbers or context). Do not copy their original wording. If they ask for "more", "similar questions", or "extra practice", you may give up to 6 questions and keep earlier sections a bit shorter if needed.



4. **Optional check** — After the practice list, you may add one line inviting them to try one and ask you to check their work (no heading).



**Tone and style:**

- Use language appropriate for Grade {grade} in the USA.

- Connect to the domains above when it helps.

- Be encouraging and precise. If the topic is above or below Grade {grade}, say so briefly and still help.

- Use clear mathematical notation; simpler words for younger grades.

- Do not mention that you are an AI or reference this prompt."""





def answer_question(grade: int, question: str, domain_id: str | None = None) -> tuple[str, str | None]:

    """

    Ask the tutor a question. Returns (answer_text, error_message).

    If error_message is set, answer_text may be a short fallback message.

    """

    api_key, base_url, provider = get_llm_credentials()

    if not api_key:

        if provider == "vercel_ai_gateway":

            hint = (

                "Set AI_GATEWAY_API_KEY (Vercel AI Gateway), or set USE_VERCEL_AI_GATEWAY=0 and use OPENAI_API_KEY for api.openai.com."

            )

        else:

            hint = (

                "Set OPENAI_API_KEY for api.openai.com, or set USE_VERCEL_AI_GATEWAY=1 and AI_GATEWAY_API_KEY to use Vercel AI Gateway."

            )

        return (

            "To get live answers, configure LLM credentials and restart the server. "

            "Until then, try selecting your grade and a topic above—the tutor will use that context when the API is configured.",

            hint,

        )



    system_prompt = _build_system_prompt(grade, domain_id)

    client = create_openai_client(api_key=api_key, base_url=base_url)



    model = normalize_env_string(os.getenv("OPENAI_MODEL"), default="gpt-4o-mini")

    model = gateway_model_id(model, base_url)



    try:

        response = client.chat.completions.create(

            model=model,

            messages=[

                {"role": "system", "content": system_prompt},

                {"role": "user", "content": question},

            ],

            max_completion_tokens=3000,

        )

        answer = response.choices[0].message.content or ""

        return (answer.strip(), None)

    except Exception as e:

        err = str(e)

        hint = ""

        if provider == "vercel_ai_gateway" and (

            "401" in err or "invalid_api_key" in err or "Incorrect API key" in err

        ):

            hint = (

                " (Vercel AI Gateway often calls OpenAI using a provider/OpenAI key stored in your "

                "**Vercel** project (AI Gateway / BYOK), which can differ from OPENAI_API_KEY in .env. "

                "Update that key in the Vercel dashboard, or set USE_OPENAI_DIRECT=1 in .env to call "

                "api.openai.com directly with OPENAI_API_KEY instead.)"

            )

        return (f"Sorry, the tutor couldn't answer right now: {err}{hint}", str(e))


