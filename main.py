from fastapi import FastAPI, Request
import os

app = FastAPI()

def _last_user_text(messages):
    if not isinstance(messages, list):
        return ""
    for m in reversed(messages):
        if isinstance(m, dict):
            role = m.get("role")
            txt = m.get("content") or m.get("message") or ""
            if role in ("user", "sim_user") and isinstance(txt, str):
                return txt.strip()
    return ""

def _shorten(s, n=140):
    return s if len(s) <= n else s[:n-1] + "…"

@app.get("/healthz")
async def healthz():
    return {"ok": True}

@app.post("/")
async def handle(req: Request):
    try:
        body = await req.json()
    except Exception:
        body = {}
    u = _last_user_text(body.get("messages") or [])
    emo = (body.get("emotion") or "warm")
    if not u:
        text = f'<emotion value="{emo}" /> Hi! I’m Samantha. Ask me anything—I’ll keep it brief.'
    elif "story" in u.lower():
        text = f'<emotion value="{emo}" /> Tiny tale: a shy dragon found her voice by singing to the moon.'
    else:
        text = f'<emotion value="{emo}" /> ' + _shorten(f"Got it: {u}. I’ll keep answers super short and fun.")
    return {"text": text}

# --- Cartesia builder requires an explicit uvicorn.run() ---
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
