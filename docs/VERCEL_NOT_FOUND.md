# Resolving Vercel NOT_FOUND (404)

## 1. Fix (what to change)

### If you see 404 when opening the app or when the app calls the API

**A. Frontend (Vite/React) on Vercel**

- **SPA fallback** is already set in `frontend/vercel.json`: requests that don’t match static files are served `index.html`. That avoids 404s when opening the app or refreshing on a client route.
- **API calls** use `/api` locally (proxied by Vite to your backend). On Vercel there is no backend, so `/api/...` returns **404 NOT_FOUND**.

**Do this:**

1. **Deploy the backend** somewhere (e.g. Railway, Render, Fly.io, or Vercel serverless) and get its URL, e.g. `https://math-mentor-api.onrender.com`.
2. **Point the frontend at that URL** using an env var:
   - In Vercel: Project → Settings → Environment Variables → add:
     - `VITE_API_ORIGIN` = `https://your-backend-url.com` (no trailing slash)
   - Redeploy the frontend so the build picks up `VITE_API_ORIGIN`.
3. **Allow the Vercel origin in the backend** so the browser allows requests:
   - On the backend host, set env var: `FRONTEND_ORIGIN` = `https://your-app.vercel.app` (your real Vercel URL).
   - Restart the backend so CORS includes that origin.

After this, the app on Vercel will call your deployed API and you should no longer get NOT_FOUND for `/api/...`.

**B. If the deployment or a specific URL is “not found”**

- Check the deployment URL for typos (e.g. wrong project name or path).
- In Vercel: Project → Deployments and confirm the deployment exists and that you’re opening the correct deployment URL (production or preview).
- Ensure the project’s **Root Directory** is set to `frontend` (so Vercel builds the Vite app and uses `frontend/vercel.json`).

---

## 2. Root cause

- **What the code does**
  - Frontend uses a single base URL for the API: locally it’s `/api` (same origin); in production it was still `/api` on the Vercel domain.
  - Vite’s `server.proxy` only runs in **development**. The built app is static; there is no proxy on Vercel.
  - So in production, requests to `https://your-app.vercel.app/api/standards/...` go to **Vercel**. Vercel serves the static frontend and has no handler for `/api/*`, so it returns **404 NOT_FOUND**.

- **What was needed**
  - In production, `/api` requests must go to your **real backend** (different host). That means either:
    - Using a different base URL for the API in production (e.g. `VITE_API_ORIGIN`), or
    - Proxying `/api` from Vercel to your backend (rewrites or serverless).

- **What triggered the error**
  - Deploying only the frontend to Vercel.
  - Keeping the API base as `/api` (same origin) while the backend runs elsewhere.
  - First API call (e.g. standards or ask) to `your-app.vercel.app/api/...` → Vercel has no resource for that path → 404.

- **Misconception**
  - Treating “same-origin `/api`” in production the same as in dev, where the dev server proxies `/api` to the backend. In production there is no proxy unless you configure it or call the backend URL directly.

---

## 3. Underlying idea

- **Why this error exists**
  - 404 means “this URL has no resource here.” Vercel is correct: on the frontend deployment there is no `/api/...` resource. The platform doesn’t guess that you meant another server.

- **Mental model**
  - **Development**: One origin (e.g. `localhost:5173`). Proxy or backend on same machine can handle `/api` so the frontend can use relative `/api`.
  - **Production**: Frontend (Vercel) and backend (another host) are two different origins. The browser sends API requests to the frontend origin unless you use the backend’s full URL (or a proxy that forwards to it).

- **In the framework**
  - Vite’s proxy is dev-only. Build output is static files + optional env. Production routing (SPA fallback) and “where does `/api` go?” are deployment concerns (Vercel config + env).

---

## 4. What to watch for

- **Relative API base in production**
  - Using `/api` or a relative path when the backend is on another domain will 404 in production unless you add a proxy (rewrites/serverless) on the frontend host.

- **Assuming dev proxy in production**
  - Any `proxy` in `vite.config.js` (or similar) does not run in the built app. You must configure production (env + CORS or proxy) explicitly.

- **Similar mistakes**
  - Forgetting to set `VITE_*` (or equivalent) in the Vercel project and redeploying, so the built app still uses the wrong API URL.
  - Forgetting CORS on the backend for the Vercel origin, causing browser errors (often CORS, not 404, but same root cause: frontend and backend origins differ).

- **Code smells**
  - Hardcoded `/api` or `localhost` in frontend with no env-based override for production.
  - No `vercel.json` (or similar) for SPA fallback when the app has client-side routes.

---

## 5. Alternatives and trade-offs

| Approach | Trade-offs |
|----------|------------|
| **Env var for API origin** (e.g. `VITE_API_ORIGIN`) | Simple, no Vercel proxy. Backend must set CORS for the frontend origin. You manage backend URL per environment. |
| **Vercel rewrites** (proxy `/api` to backend URL in `vercel.json`) | Same-origin `/api` from the browser; CORS less visible. Backend URL is in config (or you need a serverless layer to read env). Slightly more moving parts. |
| **Vercel serverless functions** under `/api` | Backend logic or a thin proxy on Vercel. Keeps one deployment surface; more code and cold starts. |
| **Backend on same domain (e.g. Vercel + serverless API)** | Single origin; no CORS for that domain. Requires implementing or adapting API as serverless functions. |

The changes in this repo use **env var + CORS** so you can deploy the frontend to Vercel and the backend anywhere, with minimal config and no proxy on Vercel.
