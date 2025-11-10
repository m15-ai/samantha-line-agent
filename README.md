# Samantha Line Agent

## Description

Ultra-minimal FastAPI application for Cartesia Line "Connect Your Code". It handles incoming requests and generates short text responses, optionally with emotion tags. Cartesia manages STT, WebSocket, and TTS components.

## Features

- **Health Check Endpoint**: GET /healthz returns { "ok": true }.
- **Message Processing Endpoint**: POST / accepts JSON body like { "messages": [{"role": "user", "content": "hi"}], "emotion": "warm" } and returns a response like { "text": "<emotion value=\"warm\" /> Response text..." }.

## Installation

1. Clone the repository:

   text

   ```
   git clone https://github.com/m15-ai/samantha-line-agent.git
   cd samantha-line-agent
   ```

2. Install dependencies:

   text

   ```
   pip install -r requirements.txt
   ```

3. Set environment variables (e.g., GEMINI_API_KEY for Google GenAI integration).

## Usage

Run the app:

text

```
python main.py
```

Deploy to Cartesia using:

text

```
cartesia deploy --agent-id <your-agent-id> .
```

Test endpoints with tools like curl or Postman.

## License

MIT
