from flask import Blueprint, request, jsonify
import json, requests, os

api_bp = Blueprint("api", __name__)


@api_bp.route("/ask", methods=["POST"])
def ask():
  user_input = request.json.get("message")

  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
      "Content-Type": "application/json",
    },
    data=json.dumps({
      "model": "nvidia/nemotron-nano-9b-v2:free",
      "messages": [
        {
          "role": "Juno",
          "content": {user_input}
        }
      ], 
    })
  )

  result = response.json()
