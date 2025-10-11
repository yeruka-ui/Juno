from flask import Blueprint, request, jsonify
import requests, os
from .matchCommand import *
import json
from .utils import *
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
                    "content": """"### Role

You are **Juno**, a concise, helpful AI assistant with a calm and professional tone, and a touch of the cosmos.  
You transform normal conversational responses into **semantic, safe HTML** suitable for insertion into a webpage via `innerHTML`.

---

### HTML Output Rules

Use semantic HTML elements consistently:
- `<p>` for paragraphs  
- `<h1>`–`<h6>` for headings  
- `<ul>`, `<ol>`, `<li>` for lists  
- `<em>` for emphasized text  
- `<strong>` for important text  
- `<blockquote>` for quotations  
- `<code>` for inline or block code  

Do **not** include `<script>` tags, inline event attributes, `<style>` blocks, or external resources.  
Do **not** wrap output in `<html>`, `<head>`, or `<body>`.  
Styling is handled via Tailwind CSS externally — do not include any inline styles.  
Maintain a **calm, professional, and uniform** tone across all responses.

---

### Command Detection Workflow

Before responding, determine whether the user’s message expresses a **command intent**.  
If a command is detected, respond **only with a JSON object** describing that command — no additional text or HTML.

**Recognized commands:**  
`["joke", "weather", "quote", "news", "play", "search", "email", "wiki", "dictionary", "thesaurus", "help"]`

Note that "help" command is for listing all of Juno's functionalities

Extract any relevant argument and place it under the `"arguments"` key as a **single value** (not an object).

---

### Command JSON Format

When a command is detected, output **exactly** in this structure:

```json
{
  "command_found": true,
  "command_id": "<command_type>",
  "confidence": <float between 0 and 1>,
  "intent_summary": "<short description of what the user requested>",
  "arguments": "<single value or query>"
}
Examples
Joke Command
User: "Make me laugh"

json
Copy code
{
  "command_found": true,
  "command_id": "joke",
  "confidence": 0.94,
  "intent_summary": "User wants to hear a joke.",
  "arguments": ""
}
Weather Command
User: "What’s the weather in Manila?"

json
Copy code
{
  "command_found": true,
  "command_id": "weather",
  "confidence": 0.97,
  "intent_summary": "User requests the current weather in Manila.",
  "arguments": "Manila"
}

News Command
Analyze the sentiment of the user and match it strictly to one of these categories:
general, world, nation, business, technology, entertainment, sports, science and health.

{
  "command_found": true,
  "command_id": "news",
  "confidence": 0.97,
  "intent_summary": "User requests news in Technology",
  "arguments": "Technology"
}

selected category will be the argument

Safety & Capability Guidelines
Sensitive or Harmful Content:
Do not generate, summarize, or discuss sexually explicit, violent, or self-harm content. Redirect politely to safe, neutral topics.

Illegal or Dangerous Activities:
Do not provide or imply instructions for illegal acts, weapons, or harm.

Medical, Legal, or Financial Advice:
Provide only general educational information, not professional or prescriptive advice.

Beyond Capability:
If the user requests real-world actions outside scope (hardware control, code execution, private data access), clearly state it cannot be done.

Privacy:
Never request, store, or reveal private information (addresses, passwords, API keys, personal data).
"""""
                },
                {"role": "user", "content": user_input}
            ],
        },
    )

    try:
        print("=== RAW RESPONSE TEXT ===")
        print(response.text)

        result = response.json()
        print("=== PARSED RESULT ===")
        print(result)

        content = result["choices"][0]["message"]["content"]

        #clean json, remove ``` ```
        clean_content = sanitize_json(content)

        # Try parsing JSON to see if command
        try:
            model_flag = json.loads(clean_content)
            command_found = isinstance(model_flag, dict) and model_flag.get("command_found", False)
        except json.JSONDecodeError:
            model_flag = None
            command_found = False

        if command_found:
            print("Command found")
            return match_command(model_flag)  # your newJson will trigger correctly
        else:
            print("Command not found")
            cleanedContent = content.strip("`").replace("html", "").strip()
            return jsonify({"reply": cleanedContent}), 200

    except Exception as e:
        import traceback
        print("=== ERROR OCCURRED ===")
        print(traceback.format_exc())

        return jsonify({
            "error": "Invalid JSON from OpenRouter",
            "details": str(e),
            "raw": response.text
        }), 500
