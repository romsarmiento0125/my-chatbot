# 🤖 My Chatbot

A simple chatbot UI powered by Google Gemini API, containerized with Docker for easy homelab deployment.

## Architecture

```
┌─────────────────────────────────┐
│  Browser                        │
│  ┌───────────────────────────┐  │
│  │  Chat UI (HTML/CSS/JS)    │  │
│  └─────────────┬─────────────┘  │
└────────────────┼────────────────┘
                 │ POST /api/chat
                 ▼
┌─────────────────────────────────┐
│  Docker Container (homelab)     │
│  ┌───────────────────────────┐  │
│  │  Flask + Gunicorn         │  │
│  │  (app.py)                 │  │
│  └─────────────┬─────────────┘  │
└────────────────┼────────────────┘
                 │ HTTPS
                 ▼
┌─────────────────────────────────┐
│  Google Gemini API              │
│  gemini-2.0-flash               │
└─────────────────────────────────┘
```

## Prerequisites

- Docker & Docker Compose
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/romsarmiento0125/my-chatbot.git
cd my-chatbot

# 2. Set up your API key
cp .env.example .env
nano .env   # paste your Gemini API key

# 3. Launch with Docker
docker-compose up -d

# 4. Open in browser
# http://localhost:5000 or http://your-server-ip:5000
```

## Running Without Docker

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set your API key
export GEMINI_API_KEY=your_key_here

# Run the app
python app.py
```

## Configuration

| Variable | Description | Required |
|---|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |

## Features

- 🎨 Clean dark-themed chat interface
- 💬 Conversation history with context
- 📝 Markdown rendering for AI responses
- 📱 Responsive design (desktop & mobile)
- 🐳 Docker ready for homelab deployment
- ⚡ Lightweight — no database needed

## Future Plans

- 🔗 n8n integration for front desk automation
- 🗄️ Database-connected agent for company data queries
- 🔐 Authentication layer

## License

MIT
