import re, json

def sanitize_json(content: str):
    """
    Remove code fences (``` or ```json) and whitespace.
    Returns a JSON object or None.
    """
    # Remove ```json or ``` fences
    content = re.sub(r"^```(?:json)?\s*", "", content)
    content = re.sub(r"\s*```$", "", content)
    content = content.strip()

    try:
        return content
    except json.JSONDecodeError:
        return None