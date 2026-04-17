# Math Mentor

A mathematics tutor for **grades 1–12** that answers questions in line with **USA Common Core State Standards** (CCSS). Students pick their grade (and optional topic), ask any math question, and get step-by-step explanations at the right level.

## What’s included

- **Backend (FastAPI)**  
  - Serves grade-level standards and an “ask” endpoint.  
  - Uses the **OpenAI API** (e.g. GPT-4) to generate answers. Responses are prompted with the relevant Common Core domains and topics for the selected grade.

- **Frontend (React + Vite)**  
  - Grade selector (1–12).  
  - Optional topic/domain dropdown (from Common Core).  
  - Simple chat UI: type a question, get an answer.

- **Standards data**  
  - Domains and topics for grades 1–12 are embedded from [Common Core State Standards for Mathematics](https://www.corestandards.org/Math/).

## Quick start

### 1. Backend

From the **project root** (`Tutor`):

**Install dependencies**

- If `pip install` fails (e.g. "Unable to create process using... python.exe"), use the Windows Python launcher with a working Python (e.g. 3.13):
  ```powershell
  py -3.13 -m pip install -r backend\requirements.txt
  ```
- Otherwise:
  ```bash
  pip install -r backend/requirements.txt
  ```

**Set your OpenAI API key** (required for live answers):

- **Windows (PowerShell):**  
  `$env:OPENAI_API_KEY = "your-key-here"`
- **Mac/Linux:**  
  `export OPENAI_API_KEY=your-key-here`

Optional: create a `.env` in the project root with:

```
OPENAI_API_KEY=your-key-here
OPENAI_MODEL=gpt-4o-mini
```

**Run the API** (from project root):

- **Easiest on Windows:**  
  `.\run-backend.ps1` (PowerShell; uses Python 3.13 and sets PYTHONPATH)
- **Or manually:**
  ```powershell
  $env:PYTHONPATH = "."
  py -3.13 -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8001
  ```
- **Mac/Linux:**
  ```bash
  export PYTHONPATH=.
  uvicorn backend.main:app --reload --host 127.0.0.1 --port 8001
  ```

API docs: **http://127.0.0.1:8001/docs**

### 2. Frontend

In a second terminal, from the project root:

```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173**. Use the grade and topic dropdowns, then ask a math question.

## How answers are aligned to USA standards

- The app uses **Common Core State Standards for Mathematics** (grades 1–12).
- For each request, the backend builds a **system prompt** that includes:
  - The **grade** (1–12).
  - The **domains and topics** for that grade (and optional chosen domain).
  - The **Standards for Mathematical Practice**.
- The model is instructed to use age-appropriate language, show steps, and tie explanations to these standards when relevant.

## Project layout

```
Tutor/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── requirements.txt
│   ├── routers/
│   │   ├── ask.py           # POST /api/ask/
│   │   └── standards.py     # GET /api/standards/...
│   ├── services/
│   │   └── tutor.py         # Prompt building + OpenAI call
│   └── standards/
│       └── common_core_math.py   # Grade 1–12 domains/topics
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js       # Proxies /api to backend
│   └── src/
│       ├── App.jsx
│       ├── App.css
│       ├── main.jsx
│       └── index.css
└── README.md
```

## API summary

| Endpoint | Description |
|----------|-------------|
| `GET /api/standards/grades` | List grades 1–12 |
| `GET /api/standards/grade/{id}` | Domains and topics for a grade |
| `GET /api/standards/practices` | Eight Standards for Mathematical Practice |
| `POST /api/ask/` | Body: `{ "grade": 1–12, "question": "...", "domain_id": "OA" \| null }` → `{ "answer": "...", "error": null \| "..." }` |

## License

MIT.
