from .command_helper import newJson
import requests

def get_wiki(command, confidence, topic):
    topic_clean = topic.strip().replace(' ', '_')
    api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic_clean}"

    headers = {
        "User-Agent": "JunoBot/1.0 (https://dummy-link.local; contact@dummy.local)"
    }

    try:
        res = requests.get(api_url, headers=headers, timeout=5)
        res.raise_for_status()
        data = res.json() if res.text else {}
    except Exception as e:
        return newJson(command, confidence, {"error": f"Request failed: {e}"})

    if not data or 'title' not in data:
        return newJson(command, confidence, {"error": "No results found."})

    content = {
        "title": data.get("title", "Unknown"),
        "thumbnail": data.get("thumbnail", {}).get("source", ""),
        "body": data.get("extract", "No summary available."),
        "url": data.get("content_urls", {}).get("desktop", {}).get("page", "")
    }
    return newJson(command, confidence, content)
