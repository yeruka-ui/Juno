import json
from youtube_search import YoutubeSearch
from .command_helper import newJson


def get_play(command, confidence, topic='General'):
    data = YoutubeSearch(topic, max_results=1).to_json()
    data = json.loads(data)

    video_id = data["videos"][0]["id"]
    title = data["videos"][0]["title"]

    url = f"https://www.youtube.com/watch?v={video_id}"

    embed_url = f"https://www.youtube.com/embed/{video_id}"

    content = {
        "title": title,
        "url": url,
        "embed_url": embed_url
    }

    return newJson(command, confidence, content)
