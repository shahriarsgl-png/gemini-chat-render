# AI Chat Assistant — Render Deployment (Flask + Google Gemini)

Satisfies "Assignment 1": a simple Render-based cloud service with a functioning
AI feature (chatbot) powered by the Google Gemini free tier.

## 1. Get a free Gemini API key
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with a Google account and click "Create API key" (free tier).
3. Copy the key — you'll paste it into Render as an environment variable.

## 2. Test locally (optional)
```bash
pip install -r requirements.txt
export GEMINI_API_KEY=your_key_here
export STUDENT_NAME="Your Name"
export STUDENT_ID="Your Student ID"
python app.py
```
Visit http://localhost:5000

## 3. Push to GitHub
Create a new GitHub repo and push this whole folder to it. Render deploys
straight from a GitHub repo.

## 4. Deploy on Render
1. Go to https://render.com and sign in (free account).
2. Click **New +** → **Web Service**.
3. Connect your GitHub repo.
4. Settings:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Under **Environment**, add these environment variables:
   - `GEMINI_API_KEY` = your Gemini key from step 1
   - `STUDENT_NAME` = your real name
   - `STUDENT_ID` = your real student ID
6. Click **Create Web Service**. Render will build and give you a live URL
   like `https://your-app.onrender.com`.

## What's included
- Home page shows your name and student ID (from environment variables, no
  need to edit code).
- A working chatbot: type a message, it's sent to `/api/chat`, which calls
  the Gemini API and returns the AI's reply.
- `Procfile` + `gunicorn` so Render can run it in production.

## Before you submit
- Make sure `STUDENT_NAME` and `STUDENT_ID` are set correctly in Render's
  environment variables (not left as placeholders).
- Open the live Render URL and confirm the chatbot actually replies —
  Render's free tier can take ~30–60 seconds to "wake up" on first load.
