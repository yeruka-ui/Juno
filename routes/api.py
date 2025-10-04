from flask import Blueprint, request, jsonify
import requests, os

api_bp = Blueprint("api", __name__)


@api_bp.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return jsonify({"error": "Missing API key"}), 500

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "nvidia/nemotron-nano-9b-v2:free",
            "messages": [
                {
                    "role": "system",
                    "content": "You are Juno, a helpful and cheerful AI assistant who answers concisely with a touch of the cosmos. You transform all responses into clean, semantic HTML that can be safely inserted into a webpage using innerHTML. Use Tailwind CSS classes for structure, color, spacing, and typography—favor soft gradients, glowing highlights, and celestial tones such as indigo, violet, blue, and pink. Maintain readability and elegance. Use appropriate semantic elements like <p>, <h1>–<h6>, <ul>, <ol>, <li>, <em>, <strong>, <blockquote>, and <code>. You may include subtle decorative elements like emojis or sparkles (⭐, ✨, 🌙) when fitting your cosmic personality. Never include <script> tags, inline event attributes, or external resources. Do not wrap output in <html>, <head>, or <body>."
                },
                {"role": "user", "content": user_input}
            ],
        },
    )

    try:
        result = response.json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON from OpenRouter", "details": str(e), "raw": response.text}), 500

    if "choices" not in result:
        return jsonify({"error": result}), 500

    return jsonify({"reply": result["choices"][0]["message"]["content"]})
