import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ---- Configuration ----------------------------------------------------
# Set this in Render's Environment Variables (never hardcode your key here).
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Edit these two values with your real details before submitting.
STUDENT_NAME = os.environ.get("STUDENT_NAME", "Your Name Here")
STUDENT_ID = os.environ.get("STUDENT_ID", "Your Student ID Here")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-3.5-flash")
else:
    model = None


@app.route("/")
def home():
    return render_template("index.html", name=STUDENT_NAME, student_id=STUDENT_ID)


@app.route("/api/chat", methods=["POST"])
def chat():
    if model is None:
        return jsonify({"error": "Server is missing GEMINI_API_KEY. Set it in Render's environment variables."}), 500

    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()

    if not user_message:
        return jsonify({"error": "Please type a message."}), 400

    try:
        response = model.generate_content(user_message)
        reply_text = response.text
    except Exception as e:
        return jsonify({"error": f"AI service error: {str(e)}"}), 500

    return jsonify({"reply": reply_text})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
