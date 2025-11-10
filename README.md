# Cartesia Line Agent

Ultra-minimal FastAPI app for Cartesia Line “Connect Your Code”.

## Endpoints
- `GET /healthz` → `{ "ok": true }`
- `POST /` with body `{ "messages":[{"role":"user","content":"hi"}], "emotion":"warm" }`
  → `{ "text": "<emotion value=\"warm\" /> …" }`

Cartesia handles STT/WS/TTS; this app returns short text (with optional `<emotion>` tag).
