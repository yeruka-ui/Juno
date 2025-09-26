from flask from flask import Blueprint, request, jsonify
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
            "messages": [{"role": "user", "content": user_input}],
        },
    )

    try:
        result = response.json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON from OpenRouter", "details": str(e), "raw": response.text}), 500

    if "choices" not in result:
        return jsonify({"error": result}), 500

    return jsonify({"reply": result["choices"][0]["message"]["content"]})
